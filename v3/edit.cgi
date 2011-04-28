#!c:\python27\python.exe

print 'Content-type: text/html\n'

import cgitb; cgitb.enable()
import util

import sqlite3
conn = sqlite3.connect(r'c:\python27\scripts\db\bulletinboard.db')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()
reply_to = form.getvalue('reply_to')

util.HtmlHeader("Yap Compose Message", "Yap, Yap, Yap")

print """
        <form action='save.cgi' method='POST'>
        """

subject = ''

# if reply_to is supplied in the CGI requets, keep it hidden in the edit form
# set the subject variable to the reply_to subject line
if reply_to is not None: 
    print '<input type="hidden" name="reply_to" value="%s" />' % reply_to
    curs.execute('SELECT subject FROM messages WHERE id = %s' % reply_to)
    subject = curs.fetchone()[0]
    if not subject.startswith('Re: '):
        subject = 'Re: ' + subject


print """
    <b>Subject:</b><br />
    <input type='text' size='40' name='subject' value = '%s' /><br />
    <b>Sender:</b><br />
    <input type='text' size='40' name='sender' /><br />
    <b>Message:</b><br />
    <textarea name='text' cols='40' rows='20'></textarea><br />
    <input type='submit' value='Save'/>
    </form>
    <hr />
    <a href='main.cgi'>Back to the main page</a>
""" % subject     

util.HtmlFooter()
