from django.db import models
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


class Feedback(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(default='default@example.com')  # Set a default value here
    message = models.TextField()

    def __str__(self):
        return self.name
    
class Contact(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phonenumber=models.CharField()
    email = models.EmailField(default='default@example.com')  # Set a default value here
    yourmessage = models.TextField()

    def __str__(self):
        return self.name
    


class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, full_name, password=None):
        if not email:
            raise ValueError("Users must have an email address")
        if not username:
            raise ValueError("Users must have a username")

        user = self.model(
            email=self.normalize_email(email),
            username=username,
            full_name=full_name,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, full_name, password=None):
        user = self.create_user(
            email=email,
            username=username,
            full_name=full_name,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30, unique=True)
    full_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = CustomUserManager()
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'full_name']

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin

class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    roll_number = models.CharField(max_length=20)
    grade = models.CharField(max_length=10)

    def __str__(self):
        return self.user.full_name
