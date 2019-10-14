from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.mainpage),
    url(r'^add$', views.add),
    url(r'^destroy/(?P<id>\d+)$', views.destroypage),
    url(r'destroypage/(?P<id>\d+)$', views.destroy)
]