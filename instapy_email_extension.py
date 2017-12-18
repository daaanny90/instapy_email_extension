import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

#set your email account details and the email address where do you
#want to receive the emails from InstaPy. You can write your email
#address in both 'your_email_address' and 'target_email_address'. In
#this case you will send yourself an email.
#
#See the readme fom more info about the SMTP Server

your_email_address = "write your email address here"
target_email_address = "write receiver email address here"
password = "write your email account password here"
smtp_server = "write the smpt server of your email"


### extension ###

#Gmail definitions
def email_send_err(e):
    s = str(e)

    fromaddr = your_email_address
    toaddr = target_email_address
    msg = MIMEMultipart()
    msg['From'] = "InstaPy"
    msg['To'] = toaddr
    msg['Subject'] = "InstaPy encourred in a problem!"

    body = "There was a problem with InstaPy: " + str(e)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(fromaddr, password)

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def email_send_start():
    fromaddr = your_email_address
    toaddr = target_email_address
    msg = MIMEMultipart()
    msg['From'] = "InstaPy"
    msg['To'] = toaddr
    msg['Subject'] = "InstaPy is starting!"

    body = "InstaPy is starting!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(fromaddr, password)

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
def gmail_send_end():
    fromaddr = your_email_address
    toaddr = target_email_address
    msg = MIMEMultipart()
    msg['From'] = "InstaPy"
    msg['To'] = toaddr
    msg['Subject'] = "InstaPy did the job!"

    body = "InstaPy did everything, session ended."
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP(smtp_server, 587)
    server.starttls()
    server.login(fromaddr, password)

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
#Hotmail (Live) definitions