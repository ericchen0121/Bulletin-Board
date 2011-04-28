#!C:\python27\python.exe
# addmessage.py

import sqlite3
conn = sqlite3.connect(r'C:\python27\scripts\db\bulletinboard.db')
curs = conn.cursor()

reply_to = raw_input('Reply to: ')
subject = raw_input('Subject: ')
sender = raw_input('Sender: ')
text = raw_input('Text: ')

if reply_to:
    # query is the SQL statement for the message with reply_to id
    query = """
    INSERT INTO messages(reply_to, sender, subject, text)
    VALUES(%s, '%s', '%s', '%s')""" % (reply_to, sender, subject, text)
    
else: 
    # else query is the SQL statement for the new message
    query = """
    INSERT INTO messages(sender, subject, text)
    VALUES('%s', '%s', '%s')""" % (sender, subject, text)
    
curs.execute(query)
conn.commit()
