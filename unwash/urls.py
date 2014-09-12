from django.conf.urls import patterns, url


urlpatterns = patterns(
    '',

    url(r'salon$', 'unwash.views.salon'),
)
