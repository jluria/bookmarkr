from django.db import models
from django.contrib.auth.models import User

class AccountUser(models.Model):
    user = models.OneToOneField(User)
    internal_id = models.CharField(max_length=25)
    verified = models.BooleanField(default=False)
    approval_date = models.DateField()

    def __str__(self):
        return self.user.username
