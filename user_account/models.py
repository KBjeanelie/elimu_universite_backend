from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

class UserType(models.Model):
    
    label = models.CharField(max_length=20, unique=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Type d'utilisateur : {self.label}"

# Create your models here.
class UserManager(BaseUserManager):
    def create_user(self, username, user_type, password=None,):
        """
        Creates and saves a User with the given username, password.
        """
        user = self.model(
            username=username,
            user_type = user_type
        )

        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, username, password=None):
        """
        Creates and saves a superuser with the given email, and password.
        """
        user = self.create_user(
            password=password,
            username=username,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


#  Custom User Model
class User(AbstractBaseUser, PermissionsMixin):
    
    username = models.CharField(max_length=255, unique=True,)
    
    user_type = models.ForeignKey(UserType, on_delete=models.DO_NOTHING, null=True, blank=True)

    is_active = models.BooleanField(default=True)
    
    is_admin = models.BooleanField(default=False)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'


    def __str__(self):
        return f"Utilisateur : {self.username}"

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
