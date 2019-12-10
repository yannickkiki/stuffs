import smtplib

# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls()
  
# Authentication
# https://myaccount.google.com/lesssecureapps
s.login("yannickbeanstests@gmail.com", "xxx")
  
# message to be sent 
message = "Hello from pythone"
  
# sending the mail 
server.sendmail("yan@trybeans.com", "git.epac.academ@gmail.com", message) 
  
# terminating the session 
s.quit()

# ---------------------

fromaddr = 'yannickbeanstests@gmail.com'
toaddrs = ['git.epac.academ@gmail.com']
# string inside msg below must have "Subject: <subject line>\n"
# for a subject to be sent, and "To: " for the recipient to be shown in the email
msg = '''To: receiving@gmail.com
    Subject: Subject line here\n
    The body goes here
    .
'''

msg = msg.format(fromaddr=fromaddr, toaddr=toaddrs[0])
# The actual mail send

server = smtplib.SMTP('plus.smtp.mail.yahoo.com', 25)
server = smtplib.SMTP('gmail-smtp-in.l.google.com', 25)
server.starttls()
server.ehlo("google.com")
server.mail(fromaddr)
server.rcpt(toaddrs[0])
server.data(msg)
server.quit()

# -----------------------------------------------------------
import smtplib

sender = "Private Person <from@smtp.mailtrap.io>"
sender = "yannickbeanstests@gmail.com"
receiver = "A Test User <to@smtp.mailtrap.io>"
receiver = "git.epac.academ@gmail.com"

message = f"""\
Subject: Hi Mailtrap
To: {receiver}
From: {sender}

This is a second test e-mail message."""

with smtplib.SMTP("smtp.mailtrap.io", 2525) as server:
    server.login("xxx", "xxx")
    server.sendmail(sender, receiver, message)

# ------------------------------------------------------------------------
import smtplib
server = smtplib.SMTP('plus.smtp.mail.yahoo.com', 25)
server.starttls()
server.ehlo("yahoo.com")
server.mail('yannick.kiki@yahoo.com')
server.rcpt('yannickbeanstests@gmail.com')
msg = '''To: 'yannickbeanstests@gmail.com'
    Subject: Subject line here\n
    The body goes here
    .
'''
server.data(msg)
server.sendmail("yannick.kiki@yahoo.com", "yannickbeanstests@gmail.com", message)


# --------------------------------------------------------------------------------------------------------------#
import smtplib

# command used to find this address: dig mx gmail.com +short
server = smtplib.SMTP('192.168.8.111', 25)

sender_mail, receiver_mail = "corentin@trybeans.com", "yan@trybeans.com"

message = f"""\
Subject: Little Hack
To: {receiver_mail}
From: {sender_mail}

Hello it's Yannick, not Corentin but don't afraid. It happens!
"""

server.sendmail(
    from_addr=sender_mail,
    to_addrs=[receiver_mail],
    msg=message
)
