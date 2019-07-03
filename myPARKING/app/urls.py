"""
app url link
"""
from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

#from django.contrib.auth.views import logout

from .forms import BootstrapAuthenticationForm
from .views import blocking
from .views import blocked
from .views import IndexPage

urlpatterns = [
    url(r'^$', view=IndexPage.as_view(), name='home'),
    url(r'^blocking/$', view=blocking, name='blocking'),
    url(r'^blocked/$', view=blocked, name='blocked'),
    url(r'^login/$',
        LoginView.as_view(template_name= 'app/login.html'),
        name='login'),
    url(r'^logout$',
        LogoutView.as_view(next_page='/'),
        name='logout'),
]
