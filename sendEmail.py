import smtplib # create smtp server to communicate 
from email.message import EmailMessage # message object
from string import Template # substitute variables inside text with $
from pathlib import Path # similar to os.path # access index.html

with smtplib.SMTP(host = 'smtp.gmail.com', port=587) as smtp: # sending from gmail

    smtp.ehlo()
    smtp.starttls()

    smtp.login('*********************@gmail.com','*****************') # insert your email and password

    # wrapped into template to make it a template object (we can use $)
    html = Template(Path('index.html').read_text())

    with open('emailList.txt', mode='r') as inputEmails:

        while(True):
            line = inputEmails.readline()
            line = line.split(' ')
            
            # breaking out of while loop if at end of file
            if line == ['']:
                break

            # selecting information from input file (without white spaces)
            email_address = line[0].strip()
            name = line[1].strip()
            age = line [2].strip()
            city = line [3].strip()

            email = EmailMessage()
            email['from'] = name                            # name of the recipient
            email['to'] = email_address                     # email of the recipient
            email['subject'] = 'E-mail sent from Python'    # subject of the e-mail

            # creating e-mail substituting variables with values
            email.set_content(html.substitute({'name': name, 'age': age, 'city': city }), 'html')

            smtp.send_message(email)
            print('E-mail sent to --> ' + email_address)

        print('Email Sent!')
        inputEmails.close()