from django.conf.urls import include, url
from hello import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^hello/', include('hello.urls')),

]
