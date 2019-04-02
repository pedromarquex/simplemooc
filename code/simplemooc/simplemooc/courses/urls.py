from django.urls import path, include, re_path
from simplemooc.courses import views as courses_views

app_name = 'courses'

urlpatterns = [
    re_path(r'^$', courses_views.index, name='index'),
    #re_path(r'^(?P<pk>\d+)/$', courses_views.details, name='details'),
    re_path(r'^(?P<slug>[\w_-]+)/$', courses_views.details, name='details'),
]