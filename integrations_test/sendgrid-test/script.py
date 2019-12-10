# ---------- first test
# import sendgrid
# from sendgrid.helpers.mail import Email, Content, Mail, Personalization
#
# # to_email = To("test@example.com")
#
# SENDGRID_API_KEY = None
#
# sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
# from_email = Email("seyive@trellix.io")
# subject = "Sending with SendGrid is Fun"
# content = Content("text/plain", "and easy to do anywhere, even with Python")
# mail = Mail(from_email=from_email, subject=subject, content=content)
# p = Personalization()
# p.add_to(Email("seyive.kiki@gmail.com"))
# mail.add_personalization(p)
# sg.client.mail.send.post(request_body=mail.get())
#
#
# # ----------------------- #
# def _send_email_test(message):
#     SENDGRID_API_KEY = None
#     sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
#     sg.client.mail.send.post(request_body=message.get())


# ----- second test
# import sendgrid
# from sendgrid.helpers.mail import Email, Content, Mail, Personalization
#
# # Almeki
# SENDGRID_API_KEY = None
#
# mail = Mail(
#     from_email=Email("almeki.dev@gmail.com"),
#     subject="First Almeki mail",
#     content=Content("text/plain", "Here is the first mail sent my Almeki with Python Sendgrid")
# )
# p = Personalization()
# p.add_to(Email("seyive.kiki@gmail.com"))
# mail.add_personalization(p)
# sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY).client.mail.send.post(request_body=mail.get())


# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail
#
# message = Mail(
#     from_email='from_email@example.com',
#     to_emails='to@example.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient(api_key=)
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)

import sendgrid
from sendgrid.helpers.mail import Email, To, Content, Mail
import requests

SENDGRID_API_KEY = None
sg = sendgrid.SendGridAPIClient(api_key=SENDGRID_API_KEY)
from_email = Email(email="hello@almeki.tech", name="Almeki")
to_email = To("seyive.kiki@gmail.com")
subject = "Sending with Twilio SendGrid is Fun"
content = Content("text/plain", "Yannick! It's easy to do anywhere, even with Python")
mail = Mail(from_email, to_email, subject, content)

# headers = {
#     "Authorization": f'Bearer {SENDGRID_API_KEY}',
#     "User-agent": 'Almeki',
#     "Accept": 'application/json'
# }
# response = requests.post('https://api.sendgrid.com/v3/mail/send', headers=headers, json=mail.get())

response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
print(response.body)
print(response.headers)
