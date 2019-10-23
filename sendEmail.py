import smtplib # create smtp server to communicate 
from email.message import EmailMessage # message object
from string import Template # substitute variables inside text with $
from pathlib import Path # similar to os.path # access index.html

# wrapped into template to make it a template object (we can use $)
html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = '**********'        # name of the recipient
email['to'] = '*******@***.***'     # email of the recipient
email['subject'] = '*******'        # subject of the e-mail

# creating e-mail substituting vaariables with values
email.set_content(html.substitute({'name': '*****', 'age': '**', 'city': '***' }), 'html')


with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp: # sending from gmail
    # setup
    smtp.ehlo()
    smtp.starttls()
    
    # connecting to email account
    smtp.login('*************@gmail.com','*************') # insert your email and password
    smtp.send_message(email)
    
    print('Email Sent!')



