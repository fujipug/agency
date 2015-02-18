from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'main.views.home.index', name='home'),
    #url(r'^candidates/', 'main.views.candidates.index', name='candidates'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^post_form_upload', 'main.views.views.post_form_upload', name='post_form_upload'),
    url(r'^Candidate_1', 'main.views.views.Candidate_1'),
    url(r'^candidates/(?P<candidate_id>\d+)/$','main.views.views.Candidates'),
)
