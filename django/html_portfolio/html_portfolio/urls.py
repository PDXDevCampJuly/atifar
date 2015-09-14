from django.conf.urls import include, url

urlpatterns = [
    url(r'^$', include('about.urls')),
    url(r'^about/', include('about.urls')),
    url(r'^javapic/', include('javapic.urls')),
    url(r'^javapic_query/', include('javapic_query.urls')),
    url(r'^zen_mockup/', include('zen_mockup.urls')),
    url(r'^forum/', include('forum.urls')),
]
