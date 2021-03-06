from django.conf.urls import url
from . import views
from django.conf import settings

urlpatterns = [
    url(r'^$', views.post_list, name="list"),
    url(r'^post/(?P<id>\d+)/$', views.post_detail, name="detail"),
    url(r'^home/$', views.post_home, name="home"),
    url(r'^tag/(?P<tag>[a-z]+)/$', views.post_tag, name='tag'),
    url(r'^rating/new/(?P<shop_pk>\d+)/$', views.rating_new, name='rating_new'),
    url(r'^recommendation/$', views.recommendation, name='recommendation'),
    url(r'^test/$', views.select_shop, name='test'),

    ]
