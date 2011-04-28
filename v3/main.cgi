#!C:\python27\python.exe
# comments by Eric S. Chen

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()
import util

import sqlite3
conn = sqlite3.connect(r'C:\python27\scripts\db\bulletinboard.db')
curs = conn.cursor()

util.HtmlHeader("Yap! Forums", "Yap Until You Collapse Forum")

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
    print '<p><a href="view.cgi?id=%(id)i">%(subject)s</a></p>' % row
    try: kids = children_message[row['id']]
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
        <hr />
        <p><a href="edit.cgi">Post message</a></p>
"""

util.HtmlFooter()

