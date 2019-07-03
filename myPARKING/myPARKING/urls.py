"""
Master URL page. All apps should have their own url and
get included here
"""
from django.conf.urls import url
from django.urls import path
from django.conf.urls import include
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    url(r'', include('app.urls')),
    url(r'^admin/', admin.site.urls),
    #url(r'^admin/', include,admin.site.urls),
]
