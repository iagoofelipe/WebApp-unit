from django.db import models

class Login(models.Model):
    user_login = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    name = models.CharField(max_length=45)

    def __str__(self) -> str:
        return self.name
        