from django.urls import path, include, re_path
from simplemooc.core import views as core_views

app_name = 'core'

urlpatterns = [
    re_path(r'^$', core_views.home, name='home'),
    re_path(r'^contato/$', core_views.contact, name='contact'),
]