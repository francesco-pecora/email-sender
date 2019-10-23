import smtplib # create smtp server to communicate 
from email.message import EmailMessage # message object
from string import Template # substitute variables inside text with $
from pathlib import Path # similar to os.path # access index.html

# wrapped into template to make it a template object (we can use $)
html = Template(Path('index.html').read_text()) # to read html as string

email = EmailMessage()
email['from'] = 'Francesco'
email['to'] = 'francescogp9898@hotmail.com'
email['subject'] = 'Info'

email.set_content(html.substitute({'name': 'Francesco', 'age': '21', 'city': 'New York' }), 'html')

# using smtp server to log in and send email

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp:
    # setup
    smtp.ehlo() # defining server "hello"
    smtp.starttls() # encryption mechanism (secure connection)
    
    # connecting to email account
    smtp.login('francescogpecora@gmail.com','pioonerddjsX1..')
    smtp.send_message(email)
    print('Email Sent!')
