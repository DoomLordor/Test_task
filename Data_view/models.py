# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class TypeInstitutions(models.Model):
    """Модель базы со справочником Типов учереждения"""

    outside_id = models.IntegerField('outside_id')
    name_type = models.TextField('Тип учреждения')

    class Meta:
        managed = True
        db_table = 'type_institutions_manual'
        unique_together = ('id', 'outside_id')
        verbose_name = 'Наименование типа учреждения'


class TypeOrganizations(models.Model):
    """Модель базы со справочником Типов организаций"""
    outside_id = models.IntegerField('outside_id')
    name_type = models.TextField('Тип организации')

    class Meta:
        managed = True
        db_table = 'type_organizations_manual'
        unique_together = ('id', 'outside_id')
        verbose_name = 'Наименование типа организации'


class StatusEGRUL(models.Model):
    """Модель базы со справочником статусов ЕГРУЛ"""
    outside_id = models.IntegerField('outside_id')
    name_status = models.TextField('Статус ЕГРЮЛ')

    class Meta:
        ordering = ['id']
        managed = True
        db_table = 'status_egrul_manual'
        unique_together = ('id', 'outside_id')
        verbose_name = 'Наименование статуса ЕГРЮЛ'


class StatusRYBPNYBP(models.Model):
    """Модель базы со справочником статусами РУБПНУБП"""
    outside_id = models.IntegerField('outside_id')
    name_status = models.TextField('Статус РУБПНУБП')

    class Meta:
        managed = True
        db_table = 'status_rybpnybp_manual'
        unique_together = ('id', 'outside_id')
        verbose_name = 'Наименование статуса РУБПНУБП'


class IndustrySpecificTyping(models.Model):
    """Модель базы со справочником Отраслевых типизаций"""
    name_typing = models.TextField('Отраслевая типизация')

    class Meta:
        managed = True
        db_table = 'industry_specific_typing_manual'
        unique_together = ('id',)
        verbose_name = 'Наименование отраслевой типизации'


class BudgetLevel(models.IntegerChoices):
    not_defined = 0, 'Не определен'
    federal_budget = 1, 'Федеральный бюджет'
    budget_subject_RF = 2, 'Бюджет субъекта Российской Федерации'
    local_budget = 3, 'Местный бюджет'
    budget_city_district = 4, 'Бюджет городского округа'
    budget_municipal_district = 5, 'Бюджет муниципального района'
    budget_urban_settlement = 6, 'Бюджет городского поселения'
    budget_rural_settlement = 7, 'Бюджет сельского поселения'
    budget_state_extra_budgetary_fund_RF = 8, 'Бюджет государственного внебюджетного фонда Российской Федерации'
    budget_pension_fund_RF = 9, 'Бюджет Пенсионного фонда Российской Федерации'
    budget_social_insurance_fund_RF = 10, 'Бюджет Фонда социального страхования Российской Федерации'
    budget_federal_compulsory_medical_insurance_fund = 11, 'Бюджет Федерального фонда обязательного медицинского ' \
                                                           'страхования '
    budget_territorial_state_extra_budgetary_fund = 12, 'Бюджет территориального государственного внебюджетного фонда'
    budget_city_district_with_intra_city_division = 13, 'Бюджет городского округа с внутригородским делением'
    local_budget_municipality_city_federal_significance = 14, 'Бюджет внутригородского муниципального образования ' \
                                                              'города федерального значения '
    budget_inner_city_district = 15, 'Бюджет внутригородского района'


class HeadByBK(models.Model):
    """Модель базы с кодами по БК и их наименованиями"""
    code_head_by_bk = models.CharField('Код главы по БК', db_column='code_head_by_BK', max_length=3)
    name_head_by_bk = models.TextField('Наименование главы по БК', db_column='name_head_by_BK')

    class Meta:
        managed = True
        db_table = 'head_by_bk_manual'
        unique_together = ('id',)
        verbose_name = 'Наименование главы по БК'


class Data(models.Model):
    """Модель базы с обзорными данными"""
    id_institutions = models.IntegerField('Код учреждения', primary_key=True)

    name_institutions = models.TextField('Наименование организации')

    inn = models.CharField('ИНН', db_column='INN', max_length=10)

    kpp = models.CharField('КПП', db_column='KPP', max_length=9)

    budget_level = models.IntegerField(choices=BudgetLevel.choices, default=BudgetLevel.not_defined)

    type_institutions = models.ForeignKey(TypeInstitutions, on_delete=models.PROTECT,
                                          verbose_name='Код типа учреждения')

    type_organizations = models.ForeignKey(TypeOrganizations, on_delete=models.PROTECT,
                                           verbose_name='Код типа организации')

    status_egrul = models.ForeignKey(StatusEGRUL, on_delete=models.PROTECT, verbose_name='Код статуса ЕГРЮЛ')

    status_rybpnybp = models.ForeignKey(StatusRYBPNYBP, on_delete=models.PROTECT, verbose_name='Код статуса РУБПНУБП')

    industry_specific_typing = models.ForeignKey(IndustrySpecificTyping, on_delete=models.PROTECT,
                                                 verbose_name='Код отраслевой типизации')

    head_by_bk = models.ForeignKey(HeadByBK, on_delete=models.PROTECT, verbose_name='Код уровня бюджета')

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
