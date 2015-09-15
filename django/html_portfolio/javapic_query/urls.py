from django.conf.urls import url
from javapic_query import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hello_world.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', views.javapic_query, name='javapic_query'),
    url(r'^join', views.join_query, name='join_query'),
    url(r'^gallery', views.gallery_query, name='gallery_query'),
]