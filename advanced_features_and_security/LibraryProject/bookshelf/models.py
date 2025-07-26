from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomUserManager(BaseUserManager):
    def create_user(self, email=None, password=None, **kwargs):
        if not email:
            return "Please provide your email address"
        normalize_email = self.normalize_email(email)
        user = self.model(email=normalize_email, password=password, **kwargs)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password, **kwargs):
        """ Method to create super user """

        user = self.create_user(email=email, password=password, **kwargs)
        user.is_admin = True
        user.is_superuser = True
        user.is_staff = True

        user.save(using=self._db)
        return user
        


class CustomUser(AbstractBaseUser, PermissionsMixin):
    username  = models.CharField(max_length=200, help_text="Username", default="user")
    email = models.EmailField(unique=True, help_text="Enter your email")
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=200, default="first name", blank=True, null=True)
    last_name = models.CharField(max_length=200, default="last name", blank=True, null=True)
    date_of_birth = models.DateField(auto_now=True, blank=True, null=True)
    profile_photo = models.ImageField(verbose_name="profile picture", blank=True, null=True, default="")
    date_joined = models.DateTimeField(auto_now_add=True, verbose_name="date joined", help_text="date joined", null=True)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)

    @property
    def is_staff(self):
        return self.is_admin
    objects = CustomUserManager()
    USERNAME_FIELD = "email"
    EMAIL_FIELD = "email"
    REQUIRED_FIELDS = []
    
    def __str__(self):
        return self.email
    
 

        
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()

    def __str__(self):
        return f'{self.title} {self.author}'

    class Meta:
        permissions = [
            ("can_create_books", "can add books"),
            ("can_edit_books", "can edit books"),
            ("can_delete_books", "can delete books"),
            ("can_view_books", "can view books"),
        ]