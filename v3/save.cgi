#!c:\python27\python.exe

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()
import util

def quote(string): 
    if string: 
        return string.replace("'", "\\'")
    else: 
        return string

import sqlite3
conn = sqlite3.connect(r'c:\python27\scripts\db\bulletinboard.db')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()

sender = quote(form.getvalue('sender'))
subject = quote(form.getvalue('subject'))
text = quote(form.getvalue('text'))
reply_to = form.getvalue('reply_to')

if not(sender and subject and text): 
    print 'Please supply sender, subject and text'
    sys.exit()

if reply_to is not None: 
    query = """
    INSERT INTO messages(reply_to, sender, subject, text)
    VALUES(%i, '%s', '%s', '%s')""" % (int(reply_to), sender, subject, text)
else: 
    query = """
    INSERT INTO messages(sender, subject, text)
    VALUES('%s', '%s', '%s')""" % (sender, subject, text)

curs.execute(query)
conn.commit()

util.HtmlHeader("Message Saved")
print """
        <hr />
        <a href='main.cgi'>Back to the main page</a>
"""
util.HtmlFooter()
