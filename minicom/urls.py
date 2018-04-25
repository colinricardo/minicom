from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

import api
import admin

urlpatterns = patterns(
    # Examples:
    # url(r'^$', 'minicom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    '',
    url(r'^api/ping$', api.ping),
    url(r'^api/read$', api.mark_as_read),
    url(r'^api/send$', api.send_message),
    url(r'^admin$', admin.users),
    url(r'^api/conversation', api.conversation))
