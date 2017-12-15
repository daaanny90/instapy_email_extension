import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

def gmail_send_err(e):
    s = str(e)

    fromaddr = "YOUR_EMAIL"
    toaddr = "YOUR_EMAIL"
    msg = MIMEMultipart()
    msg['From'] = "InstaPy"
    msg['To'] = toaddr
    msg['Subject'] = "Instapy encourred in a problem!"

    body = "There was a problem with instapy: " + str(e)
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "YOUR_PASSWORD")

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()

def gmail_send_start():
    fromaddr = "YOUR_EMAIL"
    toaddr = "YOUR_EMAIL"
    msg = MIMEMultipart()
    msg['From'] = "InstaPy"
    msg['To'] = toaddr
    msg['Subject'] = "InstaPy is starting!"

    body = "InstaPy is starting!"
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "YOUR_PASSWORD")

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
    
def gmail_send_end():
    fromaddr = "YOUR_EMAIL"
    toaddr = "YOUR_EMAIL"
    msg = MIMEMultipart()
    msg['From'] = "InstaPy"
    msg['To'] = toaddr
    msg['Subject'] = "Instabot did the job!"

    body = "InstaPy did everything, session ended."
    msg.attach(MIMEText(body, 'plain'))

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, "YOUR_PASSWORD")

    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()