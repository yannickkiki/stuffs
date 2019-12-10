import smtplib

# command used to find this address: dig mx gmail.com +short
server = smtplib.SMTP('gmail-smtp-in.l.google.com', 25)

sender_mail = "seyive.kiki@gmail.com"
receiver_mail = "seyive@trellix.io"

message = f"""
    Subject: Hi Yann
    To: {receiver_mail}
    From: {sender_mail}
    
    Hello it's Yannick.
"""

server.sendmail(
    from_addr=sender_mail,
    to_addrs=[receiver_mail],
    msg=message
)
