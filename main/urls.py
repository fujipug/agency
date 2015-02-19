from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'main.views.home.index', name='home'),
    url(r'^about/', 'main.views.home.about', name='about'),
    url(r'^candidates/', 'main.views.candidates.index', name='candidates'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^free_stuff_form/', 'main.views.views.free_stuff_form', name='free_stuff_form'),
    url(r'^candidates/(?P<candidate_id>\d+)/$','main.views.views.Candidates'),
    url(r'^confirmation/', 'main.views.confirmation.index', name='Confirmation'),
    url(r'^democrat_list/', 'main.views.democrat_list.democrat_list', name='Confirmation'),

    url(r'^aboutcandidates/(?P<candidate_id>\d+)/$','main.views.views.Candidates'),
)
