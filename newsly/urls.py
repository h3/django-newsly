from django.conf.urls.defaults import *
from newsly.views import *

urlpatterns=patterns('',
    url(r'^page/(?P<page>[0-9]+)/$', NewsView.as_view(), name="newsly-index"),
    url(r'^(?P<slug>[\-\d\w]+)/$', NewsDetail.as_view(), name='newsly-detail'),
)
