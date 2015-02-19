from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'main.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'main.views.home.index', name='home'),
    url(r'^candidates/', 'main.views.candidates.index', name='candidates'),
    url(r'^admin/', include(admin.site.urls)),
<<<<<<< HEAD
    url(r'^free_stuff_form/', 'main.views.views.free_stuff_form', name='free_stuff_form'),
    url(r'^candidates/(?P<candidate_id>\d+)/$','main.views.views.Candidates'),
    url(r'^confirmation/', 'main.views.confirmation.index', name='Confirmation'),
    url(r'^democrat_list/', 'main.views.democrat_list.democrat_list', name='Confirmation'),

=======
    url(r'^post_form_upload', 'main.views.views.post_form_upload', name='post_form_upload'),
    url(r'^aboutcandidates/(?P<candidate_id>\d+)/$','main.views.views.Candidates'),
>>>>>>> d6753f66465fd1eb6a38d35472bafc097f4e0b4e
)
