"""

"""
import smtplib
from datetime import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import pandas as pd
from grocer.db.views import WooliesView
from settings.scrapy import EMAIL

# auth credentials
fromaddress = EMAIL['fromaddress']
toaddress = EMAIL['toaddress']
mailserver_ = EMAIL['mailserver']
password = EMAIL['password']
portnumber = EMAIL['portnumber']

# fetchall view -> List -> html
w_savings = WooliesView().current_savings()
savings_df = pd.DataFrame(w_savings).to_html()

# msg
msg = MIMEMultipart()
msg['From'] = fromaddress
msg['To'] = toaddress
msg['Subject'] = "html_table"

html_message = """\
    <html>
      <head></head>
      <body>
        {0}
      </body>
    </html>
    """.format(savings_df)

# @TODO add headers on table. currently missing
msg.attach(MIMEText(html_message, 'html'))

# login and sendmail
mailserver = smtplib.SMTP(mailserver_, portnumber)
mailserver.login(fromaddress, password)
mailserver.sendmail(
    fromaddress,
    toaddress,
    msg.as_string()
    )
mailserver.quit()
