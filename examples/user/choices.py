from django.db import models
from django.utils.translation import gettext_lazy as _

class USER_TYPE(models.TextChoices):
    ADMIN = ('ADMIN',_('ADMIN'))
    TEACHER = ('TEACHER',_('TEACHER'))
    STUDENT = ('STUDENT',_('STUDENT'))
