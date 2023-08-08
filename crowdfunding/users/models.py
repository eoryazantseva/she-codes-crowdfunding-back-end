from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser): # we are defining a very sparse CustomUser model
    pass

    def __str__(self):
        return self.username