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
        user.is_active = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class UserModel (AbstractBaseUser):
    category = models.CharField(
        blank=False, null=False, verbose_name='category', max_length=15)
    username = models.CharField(
        blank=False, null=False, verbose_name='username', max_length=15)
    email = models.EmailField(blank=True, null=True,
                              verbose_name='email', unique=True)
    password = models.CharField(
        blank=True, null=True, verbose_name='password', max_length=100)
    phone = models.CharField(verbose_name='phone',
                             blank=True, null=True, max_length=16)
    can_post = models.BooleanField(default=False, blank=True,)
    is_admin = models.BooleanField(blank=True, null=True, default=True)
    is_active = models.BooleanField(blank=True, null=True, default=True)
    is_staff = models.BooleanField(blank=True, null=True, default=True)
    is_superuser = models.BooleanField(blank=True, null=True, default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['category', 'password',
                       'username', 'can_post']

    objects = UserManager()

    def __str__(self):
        return str(self.id) + '- ' + str(self.category)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def delete(self, *args, **kwargs):
        super(UserModel, self).delete(*args, **kwargs)


'''
    def save(self, *args, **kwargs):
        self.set_password(self.password)
        super(UserModel, self).save(*args, **kwargs)

'''


class Information(models.Model):
    user = models.OneToOneField(
        UserModel, on_delete=models.SET_NULL, null=True)
    photo_profile = models.ImageField(
        blank=True, null=True, upload_to='media/')
    resume = models.CharField(max_length=100, null=True, blank=True)
    site = models.CharField(max_length=100, null=True, blank=True)
    whoAreUs = models.CharField(max_length=500, null=True, blank=True)
    ourObjective = models.CharField(max_length=500, null=True, blank=True)
    photo1 = models.ImageField(blank=True, null=True, upload_to='media/')
    photo2 = models.ImageField(blank=True, null=True, upload_to='media/')
