from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone

# Create your models here.

# class User(models.Model):
#     user_id = models.CharField(primary_key=True, max_length=10)
#     password = models.CharField(max_length=10)
#     name = models.CharField(max_length=10)
#     address = models.CharField(max_length=30)
#     phone = models.CharField(max_length=15, blank=True, null=True)
#     is_active = models.IntegerField(blank=True, null=True)
#     is_admin = models.IntegerField(blank=True, null=True)
#     is_superuser = models.IntegerField(blank=True, null=True)
#     date_joined = models.DateField(blank=True, null=True)
#     last_login = models.DateField(blank=True, null=True)

#     class Meta:
#         managed = False
#         db_table = 'user'


class CustomUserManager(BaseUserManager):
    def create_user(self, user_id, phone, address, name, password = None):
        user = self.model(
            user_id=user_id,
            phone=phone,
            address=address,
            name=name,
        )
        user.set_password(password)
        user.is_active = True
        user.save(using=self._db)
        return user

    def create_superuser(self, user_id, password):
        user = self.create_user(
            password=password,
            user_id=user_id,
        )
        user.is_superuser = True
        user.is_admin = True
        user.is_active = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser, PermissionsMixin):

    object = CustomUserManager()
    
    user_id = models.CharField(primary_key=True, max_length=10)
    name = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    phone = models.CharField(max_length=15, blank=True, null=True)
    
    is_active = models.IntegerField(blank=True, null=True)
    is_admin = models.IntegerField(blank=True, null=True)
    is_superuser = models.IntegerField(blank=True, null=True)
    date_joined = models.DateField(blank=True, null=True)
    last_login = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = 'user',
        verbose_name_plural = 'users'
        db_table = 'user'

    def __str__(self):
        return self.user_id

    def get_full_name(self):
        return self.user_id

    def get_short_name(self):
        return self.user_id

    @property
    def is_staff(self):
        return self.is_superuser
    
    USERNAME_FIELD = 'user_id'


class UserGroups(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    group = models.ForeignKey('festival.AuthGroup', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_groups'
        unique_together = (('user', 'group'),)


class UserUserPermissions(models.Model):
    user = models.ForeignKey(User, models.DO_NOTHING)
    permission = models.ForeignKey('festival.AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'user_user_permissions'
        unique_together = (('user', 'permission'),)