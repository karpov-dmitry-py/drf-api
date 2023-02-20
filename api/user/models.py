from django.db import models
from django.contrib.auth import models as auth_models


class UserManager(auth_models.BaseUserManager):

    def create_user(self,
                    first_name,
                    last_name,
                    email: str,
                    password: str = None,
                    is_staff: bool = False,
                    is_super_user: bool = False) -> 'User':

        if not email:
            raise ValueError('User must have an email')

        if not first_name:
            raise ValueError('User must have a first name')

        if not last_name:
            raise ValueError('User must have a last name')

        user = self.model(email=self.normalize_email(email))
        user.first_name = first_name
        user.last_name = last_name
        user.set_password(password)
        user.is_active = True
        user.is_staff = is_staff
        user.is_superuser = is_super_user
        user.save()

        return user

    def create_superuser(self,
                         first_name,
                         last_name,
                         email: str,
                         password: str = None) -> 'User':
        user = self.create_user(
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password,
            is_staff=True,
            is_super_user=True,
        )

        return user


class User(auth_models.AbstractUser):
    first_name = models.CharField(verbose_name='First name', max_length=255)
    last_name = models.CharField(verbose_name='Last name', max_length=255)
    email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
    password = models.EmailField(verbose_name='Password', max_length=255)
    username = None
    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']
