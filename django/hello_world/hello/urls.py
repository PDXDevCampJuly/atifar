from django.conf.urls import include, url
from hello import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.index, name='index'),
    url(r'^corgi.html', views.corgi, name='corgi'),
    url(r'^forum.html', views.forum, name='forum'),
]
