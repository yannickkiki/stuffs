from sendgrid.helpers.mail import (
    Mail as Message, CustomArg, Content, Category, Personalization, Substitution, Email as EmailContact
)


def f():
    message = Message()
    message.from_email = EmailContact(email="yannick@trybeans.com", name="Yannick")
    message.subject = "New announcement"
    return message
