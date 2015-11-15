from django.conf.urls import url
import polls

urlpatterns = [
    # Examples:
    # url(r'^$', 'poll_site.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'polls.views.questions', name='questions'),
    url(r'^(?P<question_id>\d+)/$', 'polls.views.details', name='details'),
]
