from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from django.db import models
from user.managers import CustomUserManager
from user.choices import USER_TYPE

class User(AbstractBaseUser, PermissionsMixin):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(_('email address'), unique=True)
    date_joined = models.DateTimeField(default=timezone.now)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)    
    user_type = models.CharField(max_length=20,choices=USER_TYPE.choices, default=USER_TYPE.STUDENT)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = [first_name, last_name, email]

    objects = CustomUserManager()

    class Meta:
        db_table = "user"
        verbose_name = "User"
        verbose_name_plural = "Users"
        default_related_name = "users"
        ordering = ["date_joined"]

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'        

    def __str__(self):
        return self.email