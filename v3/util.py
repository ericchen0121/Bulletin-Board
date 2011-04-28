def HtmlHeader(title, header_title=None): 
    """
    HTML_header prints the opening HTML tags including the title and
    the header. It sets the <title> in the head, and optionally the header.
    If no header is provided, it defaults to the title.
    """
    if header_title is None:
        header_title = title
        
    print """
    <html>
        <head>
            <title>%s</title>
        </head>
        <body>
            <h1>%s</h1>
            """ % (title, header_title)

def HtmlFooter(): 
    print """
        </body>
    </html>
    """
