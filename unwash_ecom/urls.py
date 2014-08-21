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
from oscar.app import shop
#from stores.app import application as stores_app
#from stores.dashboard.app import application as dashboard_app


urlpatterns = [
    url(r'^i18n/', include('django.conf.urls.i18n')),
    url(r'', include(application.urls)),
    url(r'^admin/', include(admin.site.urls)),

    ## Added for Oscar-Stores support
    # basic configuration for Oscar
    #url(r'', include(shop.urls)),

    # adds URLs for the dashboard store manager
    #url(r'^dashboard/stores/', include(dashboard_app.urls)),

    # adds URLs for overview and detail pages
    #url(r'^stores/', include(stores_app.urls)),

    # adds internationalization URLs
    #(r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
]