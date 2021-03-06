from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.conf import settings
from django.urls import reverse
from django.core.urlresolvers import reverse_lazy



urlpatterns = [
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', auth_views.logout, name='logout', kwargs={
        'next_page': reverse_lazy('shop:list')}),
    url(r'^profile/$', views.profile, name= 'profile'),
]
