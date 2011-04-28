#!C:\python27\python.exe
# comments by Eric S. Chen

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()

import sqlite3
conn = sqlite3.connect(r'C:\python27\scripts\db\bulletinboard.db')
curs = conn.cursor()

print """
<html>
    <head>
        <title>Yap! Forums</title>
    </head>
    <body>
        <h1>Yap! Forums</h1>
        """ 

# this SELECT SQL statement will return a list of tuples
curs.execute('SELECT * FROM messages')

# curs.description is a tuple of 7-tuples, with d[0] for each 7-tuple d being 
# the name of the column. This follows the Python Database API
names = [d[0] for d in curs.description]

# creates a list of dictionaries, each where k, v pair is db column name, value
# is each column name component of the message. Each dictionary is one message.
rows = [dict(zip(names, row)) for row in curs.fetchall()]

toplevel_message = []
children_message = {}

# if message is a reply to another... put it in another place. 
# else, put it in a toplevel_message, which is a list of dictionaries.
for row in rows: 
    parent_id = row['reply_to']
    if parent_id is None: 
        toplevel_message.append(row)
    else: 
        children_message.setdefault(parent_id, []).append(row)

def format(row): 
    print '<b>', row['subject'], '</b><br>'
    print '<i>', row['text'], '</i>'
    try: kids = children_message[row['id']]
    # what's the best way to know which error to handle? which test system?
    except KeyError: pass
    else: 
        print '<blockquote>'
        for kid in kids: 
            format(kid)
        print '</blockquote>'

print '<p>'

for row in toplevel_message: 
    format(row)

print """
        </p>    
    </body>
</html>
"""
