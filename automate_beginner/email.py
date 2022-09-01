from multiprocessing import context
import smtplib
import ssl
from email.message import EmailMessage


subject = "Email from python"
body="This is a test email"
sender_email = ""
receiver_email =""
password= input("Enter a password: ")

message = EmailMessage()
message['From'] =sender_email
message['To']= receiver_email
message['Subject']= subject
message.set_content(body)


content = ssl.create_default_context()

print('send email')

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
print('Success')