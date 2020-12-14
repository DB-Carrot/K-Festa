# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.utils import timezone


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey('account.User', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

def festival_number():
    num = Festival.objects.count()
    if num == None:
        return 1
    else:
        return num + 1

class Festival(models.Model):
    festival_key = models.IntegerField(primary_key=True, default=festival_number)
    region_key = models.ForeignKey('FestivalRegion', models.DO_NOTHING, db_column='region_key')
    category_key = models.ForeignKey('FestivalCategory', models.DO_NOTHING, db_column='category_key')
    format_key = models.ForeignKey('Format', models.DO_NOTHING, db_column='format_key')
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    image = models.CharField(max_length=100, blank=True, null=True, default='http://sarac33.dothome.co.kr/images/default.png')
    content = models.TextField()

    class Meta:
        db_table = 'festival'


class FestivalCategory(models.Model):
    category_key = models.IntegerField(primary_key=True)
    category_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'festival_category'


class FestivalRegion(models.Model):
    region_key = models.IntegerField(primary_key=True)
    region_name = models.CharField(max_length=10)

    class Meta:
        db_table = 'festival_region'\

    
def number():
    num = FestivalReview.objects.count()
    if num == None:
        return 1
    else:
        return num + 1


class FestivalReview(models.Model):
    review_key = models.IntegerField(primary_key=True, default=number)
    user = models.ForeignKey('account.User', models.DO_NOTHING)
    festival_key = models.ForeignKey(Festival, models.DO_NOTHING, db_column='festival_key', related_name='reviews')
    content = models.CharField(max_length=10)
    date = models.DateField(default=timezone.now())

    
    def __str__(self):
        return self.content
    
    
    class Meta:
        db_table = 'festival_review'


class Format(models.Model):
    format_key = models.CharField(primary_key=True, max_length=15)
    format = models.CharField(max_length=15)

    class Meta:
        db_table = 'format'

