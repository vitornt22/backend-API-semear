from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

# flake8: noqa: E501
# Create your models here.
ESTADOS = (('AC', 'AC'), ('AL', 'AL'), ('AP', 'AP'), ('AM', 'AM'), ('BA', 'BA'), ('CE', 'CE'), ('DF', 'DF'), ('ES', 'ES'), ('GO', 'GO'), ('MA', 'MA'), ('MT', 'MT'), ('MS', 'MS'),  # noqa
           ('MG', 'MG'), ('PA', 'PA'), ('PB', 'PB'), ('PR', 'PR'), ('PE', 'PE'), ('PI', 'PI'),  # noqa
            ('RJ', 'RJ'), ('RN', 'RN'), ('RS', 'RS'), ('RO', 'RO'), ('RR', 'RR'), ('SC', 'SC'),  # noqa
           ('SP', 'SP'), ('SE', 'SE'), ('TO', 'TO'))


class UserManager(BaseUserManager):
    def create_user(self, category, username, can_post, email, password=None):

        if not username:
            raise ValueError('Nome de Usuario é necessário')
        if not category:
            raise ValueError('Categoria é necessário')
        if not email:
            raise ValueError('Email é necessário')
        if not password:
            raise ValueError('Senha é necessária')

        user = self.model(
            can_post=can_post,
            username=username,
            category=category,
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, category, username, can_post, email, password=None):
        user = self.create_user(
            category=category,
            username=username,
            can_post=can_post,
            email=email,
            password=password,
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel (AbstractBaseUser):
    category = models.CharField(
        blank=False, null=False, verbose_name='category', max_length=15)
    username = models.CharField(
        blank=False, null=False, verbose_name='category', max_length=15)
    email = models.EmailField(blank=False, null=False,
                              verbose_name='email adress', unique=True)
    password = models.CharField(
        blank=False, null=False, verbose_name='password', max_length=100)
    phone = models.CharField(verbose_name='phone number',
                             blank=True, null=True, max_length=15)
    can_post = models.BooleanField(default=False, blank=True,)
    is_admin = models.BooleanField(blank=True, null=True, default=False)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_staff = models.BooleanField(blank=True, null=True, default=False)
    is_superuser = models.BooleanField(blank=True, null=True, default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['category', 'password', 'username']

    objects = UserManager()

    def __str__(self):
        return str(self.id) + '- ' + str(self.category)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True


class Adress (models.Model):

    id = models.BigAutoField(primary_key=True)
    adress = models.CharField(
        blank=False, null=False, verbose_name='adress', max_length=100)
    district = models.CharField(
        blank=False, null=False, verbose_name='district', max_length=15)
    zip_code = models.CharField(
        blank=False, null=False, verbose_name='zip_code', max_length=9)
    city = models.CharField(
        blank=False, null=False, verbose_name='city', max_length=60)
    state = models.CharField(
        verbose_name='uf',  blank=True, null=True, max_length=2, choices=ESTADOS)
    number = models.IntegerField(blank=True, null=True)
