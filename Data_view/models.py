# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class HeadByBK(models.Model):
    """Модель базы с кодами по БК и их названиями"""
    id = models.IntegerField('id', primary_key=True)
    code_head_by_bk = models.CharField('Код главы по БК', db_column='code_head_by_BK', max_length=3)
    name_head_by_bk = models.TextField('Наименование главы по БК', db_column='name_head_by_BK')

    class Meta:
        ordering = ['id']
        managed = True
        db_table = 'head_by_bk'
        unique_together = ('id',)


class Data(models.Model):
    """Модель базы с обзорными данными"""
    budget_level = models.TextField('Уровень бюджета')
    id_institutions = models.IntegerField('Код учреждения', primary_key=True)
    name_institutions = models.TextField('Наименование организации')
    inn = models.CharField('ИНН', db_column='INN', max_length=10)
    kpp = models.CharField('КПП', db_column='KPP', max_length=9)
    type_institutions = models.TextField('Тип учреждения')
    type_organizations = models.TextField('Тип организации')
    status_egrul = models.TextField('Статус ЕГРЮЛ', db_column='status_EGRUL')
    status_rybpnybp = models.TextField('Статус РУБПНУБП', db_column='status_RYBPNYBP')
    id_head_by_bk = models.ForeignKey(HeadByBK, on_delete=models.CASCADE, verbose_name='')
    industry_specific_typing = models.TextField('Отраслевая типизация',
                                                db_column='Industry-specific_typing')

    class Meta:
        ordering = ['id_institutions']
        managed = True
        db_table = 'data'
        unique_together = (('id_institutions', 'name_institutions', 'inn'),)

    def __str__(self):
        return self.name_institutions

    def __repr__(self):
        return self.name_institutions


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


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

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
