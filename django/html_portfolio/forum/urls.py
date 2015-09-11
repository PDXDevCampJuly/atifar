from django.conf.urls import include, url
from forum import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.forum, name='forum'),
    # url(r'^corgi.html', views.corgi, name='corgi'),
]