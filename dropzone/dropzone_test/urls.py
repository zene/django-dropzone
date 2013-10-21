from django.conf.urls import patterns, url

urlpatterns = patterns('dropzone.dropzone_test.views',
    url(r'^$', 'dropzone', name='dropzone'),
    url(r'^upload/$', 'upload', name='dropzone_upload'),
    url(r'^delete/$', 'delete', name='dropzone_delete'),
)
