from django.conf.urls import patterns, url

from unwash.views import SalonListView, SalonSelectView


urlpatterns = patterns(
    '',

    url(r'salon/$', SalonListView.as_view(), name='salon'),
    url(r'salon/select/(?P<slug>[^/]+)/(?P<pk>[0-9a-f-]+)/$', SalonSelectView.as_view(), name='select_salon'),
)
