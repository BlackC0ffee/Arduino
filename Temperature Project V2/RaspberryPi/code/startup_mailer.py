import subprocess
import smtplib
import socket
import os
from email.mime.text import MIMEText
import datetime
# Change to your own account information
to = ''
smtp_user = ''
smtp_password = ''
smtpserver = smtplib.SMTP('', 587)
smtpserver.ehlo()
smtpserver.starttls()
smtpserver.ehlo
smtpserver.login(smtp_user, smtp_password)
today = datetime.date.today()
# Very Linux Specific
arg='ip route list'
p=subprocess.Popen(arg,shell=True,stdout=subprocess.PIPE)
data = p.communicate()
split_data = data[0].split()
ipaddr = split_data[split_data.index('src')+1]
# Get the current CPU speed
f = os.popen('/opt/vc/bin/vcgencmd get_config arm_freq')
cpu = f.read()
mail_body = "CPU speed: " + cpu + "IP address: %s" % ipaddr
msg = MIMEText(mail_body)
msg['Subject'] = "RasPI @ "+ipaddr+" started up on %s" % today.strftime('%b %d %Y')
msg['From'] = smtp_user
msg['To'] = to
smtpserver.sendmail(smtp_user, [to], msg.as_string())
smtpserver.quit()