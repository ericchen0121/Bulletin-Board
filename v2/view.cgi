#!c:\python27\python.exe

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()

import sqlite3
conn = sqlite3.connect(r'c:\python27\scripts\db\bulletinboard.db')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()

id = form.getvalue('id')

print """
<html>
    <head>
        <title>Yap View Message</title>
    </head>
    <body>
        <h1>Yap View Message</h1>
        """

try: id = int(id)
except: 
    print 'Invalid message ID'
    sys.exit()

curs.execute('SELECT * FROM messages WHERE id = %i' % id)
# next two lines replacement for curs.dictfetchall() used with import psycopg
names = [d[0] for d in curs.description]
rows = [dict(zip(names, row)) for row in curs.fetchall()]

if not rows:
    print 'Unknown message ID'
    sys.exit()

row = rows[0]

print """
        <p><b>Subject:</b> %(subject)s<br />
        <b>Sender:</b> %(sender)s<br />
        <pre> %(text)s</pre>
        </p>
        <hr />
        <a href='main.cgi'>Back to the main page</a>
        | <a href='edit.cgi?reply_to=%(id)s'>Reply</a>
    </body>
</html>
""" % row
