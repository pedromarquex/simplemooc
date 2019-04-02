from django.urls import path, include, re_path
from django.contrib.auth.views import login as auth_login
from django.contrib.auth.views import logout as auth_logout

from simplemooc.accounts.views import register as view_register
from simplemooc.accounts.views import dashboard as view_dashboard
from simplemooc.accounts.views import edit as view_edit
from simplemooc.accounts.views import edit_password as view_edit_password

app_name = 'accounts'

urlpatterns = [
    re_path(r'^$', view_dashboard, name='dashboard'),
    re_path(r'^entrar/$', auth_login, {'template_name': 'accounts/login.html'}, name='login'),
    re_path(r'^sair/$', auth_logout, {'next_page': 'core:home'}, name='logout'),
    re_path(r'^cadastre-se/$', view_register, name='register'),
    re_path(r'^editar/$', view_edit, name='edit'),
    re_path(r'^editar-senha/$', view_edit_password, name='edit_password'),
]