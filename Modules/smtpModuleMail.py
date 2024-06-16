#Sending mail using Smtp Module

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import sys


message = MIMEMultipart() #passing mail properties to message

message["From"] = "zeysnpek@gmail.com"
message["To"] = "zeysnepk@gmail.com"
message["Subject"] = "SMTP"

text = "Hello myself!\nLong time no see :("

textBody = MIMEText(text, "plain")
message.attach(textBody)  #attaching text to message

try:
    mail = smtplib.SMTP("smtp.gmail.com",587) #connecting smtp port
    
    mail.ehlo() #connecting smtp server
    
    mail.starttls() #encryption 
    
    mail.login("", "") #login by entering mail extension and password
    
    mail.sendmail(message["From"], message["To"], message.as_string()) #sending mail
    
    print("Mail sended successfully!")
    
    mail.close()
    
except:
    sys.stderr.write("ERROR")
    sys.stderr.flush()




