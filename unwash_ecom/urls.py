from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

# urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unwash_ecom.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

#    url(r'^admin/', include(admin.site.urls)),
#)


from django.conf.urls import include, url
from oscar.app import application

urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls)),
    url(r'^admin/', include(admin.site.urls)),
]