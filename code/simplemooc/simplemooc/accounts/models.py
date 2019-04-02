from django.db import models

from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager


class User(AbstractBaseUser, PermissionsMixin):

    username = models.CharField('Nome do Usuário', max_length=30, unique=True)
    email = models.EmailField('Email', unique=True)
    name = models.CharField('Nome', max_length=100, blank=True)
    is_active = models.BooleanField('Está ativo?', blank=True, default=True)
    is_staff = models.BooleanField('É da equipe?', blank=True, default=False)
    date_joined = models.DateTimeField('Data de Entrada', auto_now_add=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def __str__(self):
        return self.name or self.username


    def get_short_name(self):
        return self.username


    def get_full_name(self):
        return str(self)


    class Meta:
        verbose_name = 'Usuário'
        verbose_name_plural = 'Usuários'