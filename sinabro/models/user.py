import uuid

from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import PermissionsMixin


"""
    User에 포함되어야할 필드, Point, PhoneNumber등 의 필드를 만족시키기 위해 
    Custom User model을 정의함
    Django Admin에 필수적인 내용들을 만족시키기 위해 manager를 따로 생성함.
"""


class MyUserManager(BaseUserManager):
    use_in_migration = True

    def _create_user(self, username, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')
        username = self.model.normalize_username(username)
        user = self.model(username=username, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, password, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username=username, password=password, **extra_fields)

    def create_superuser(self, username, password, **extra_fields):
        """
            python manage.py createsuperuser를 실행 할 때 사용하는 method
        """
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    USERNAME_FIELD = 'username'

    class Meta:
        verbose_name = '회원'
        verbose_name_plural = verbose_name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    username = models.CharField(
        max_length=31, 
        unique=True, 
        verbose_name='아이디',
    )
    name = models.CharField(
        max_length=10, 
        null=True, 
        verbose_name='이름',
    )
    gender = models.CharField(
        max_length=10,
        blank=True
    )
    phone_company = models.CharField(
        max_length=20,
        blank=True
    )
    phone_number = models.CharField(
        max_length=15,
        null=True,
        blank=True,
        verbose_name='핸드폰 번호'
    )
    birthday = models.DateField(
        null=True
    )
    address = models.CharField(
        max_length=100,
        blank=True
    )
    email = models.EmailField(
        null=True, 
        verbose_name='이메일',
    )
    point = models.PositiveIntegerField(
        verbose_name='보유금',
        default=0
    )
    description = models.TextField(
        blank=True
    )
    interests = models.TextField(
        blank=True
    )

    is_staff = models.BooleanField(
        default=False
    )

    objects = MyUserManager()  # 위에서 작성한 Manager 을 사용하도록 명시. Db Query를 생성할때 이 Object를 사용함.

