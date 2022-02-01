from django.contrib.auth.base_user import BaseUserManager
from django.utils.translation import gettext_lazy as _
from user.choices import USER_TYPE


class CustomUserManager(BaseUserManager):
    """
    Custom user model manager where email is the unique identifiers
    for authentication instead of usernames.
    """
    def create_user(self, email, password, **extra_fields):
        """
        Create and save a User with the given email and password.
        """
        if not email:
            raise ValueError(_('The Email must be set'))
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('is_superuser', True)          
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a SuperUser with the given email and password.
        """
        
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)   
        extra_fields.setdefault('user_profile', USER_TYPE.ADMIN)

        if extra_fields.get('is_superuser') is not True:
            raise ValueError(_('Superuser must have is_superuser=True.'))
        return self.create_user(email, password, **extra_fields)

'''
from users.serializers import CustomUserSerializer
from users.models import CustomUser
d = {"email":"z@gmail.com", "password":"qwerty@123"}
c = CustomUserSerializer(data = d)
c.is_valid()
c.save()
curl -X POST -H "Content-Type: application/json" -d '{"email": "super@gmail.com", "password": "qwerty"}' http://127.0.0.1:8000/api/token
curl -X POST -H "Content-Type: application/json" -d '{"email": "z@gmail.com", "password": "qwerty"}' http://127.0.0.1:8000/api/token
'''