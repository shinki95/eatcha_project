from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.post_list, name="list"),
    url(r'^post/(?P<id>\d+)/$', views.post_detail, name="detail"),
    ]