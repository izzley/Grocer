"""

"""
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from settings.scrapy import EMAIL

# auth credentials
fromaddress = EMAIL['fromaddress']
toaddress = EMAIL['toaddress']
mailserver_ = EMAIL['mailserver']
password = EMAIL['password']
portnumber = EMAIL['portnumber']

# msg
msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = 'My Test Mail'
message = 'What up G'
msg.attach(MIMEText(message))

# login and sendmail
mailserver = smtplib.SMTP(mailserver_, portnumber)
mailserver.login(fromaddress, password)
mailserver.sendmail(
    fromaddress,
    toaddress,
    msg.as_string()
    )
mailserver.quit()
