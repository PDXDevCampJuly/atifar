from django.conf.urls import include, url
from about import views

urlpatterns = [
    url(r'^$', views.about, name='about'),
]