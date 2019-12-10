from django.contrib.auth.models import AbstractUser, UserManager as AuthUserManager


class UserManager(AuthUserManager):
    pass


class User(AbstractUser):
    pass
