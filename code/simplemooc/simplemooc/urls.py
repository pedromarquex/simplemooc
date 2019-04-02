"""simplemooc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static

admin.autodiscover()

from simplemooc.core import urls as core_urls
from simplemooc.courses import urls as courses_urls
from simplemooc.accounts import urls as accounts_urls

urlpatterns = [
    re_path(r'^admin/', admin.site.urls),
    re_path(r'^', include(core_urls, namespace='core')),
    re_path(r'^conta/', include(accounts_urls, namespace='accounts')),
    re_path(r'^cursos/', include(courses_urls, namespace='courses')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)