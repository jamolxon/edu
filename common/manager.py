from educoin.helpers import generate_unique_username
from django.contrib.auth import get_user_model
from django.contrib.auth.base_user import BaseUserManager


class UserManager(BaseUserManager):
    def create_user(
        self, username=None, full_name="", password=None, **extra_fields
    ):
        """
        Creates and saves a User with the given email
        """
        user = self.model(
            username=username,
            full_name=full_name,
        )
        user.set_password(password)
        for (key, value) in extra_fields.items():
            setattr(user, key, value)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, full_name, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(username, full_name, password=password)

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
