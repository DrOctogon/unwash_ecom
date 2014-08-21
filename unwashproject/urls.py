from django.conf.urls import include, patterns, url
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf.urls.static import static
from django.views.generic.base import RedirectView

from oscar.app import shop
from oscar.views import handler500, handler404, handler403  # noqa

from stores.app import application as stores_app
from stores.dashboard.app import application as dashboard_app

from apps.sitemaps import base_sitemaps


admin.autodiscover()

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/en-us/'), name='english-site'),
    url(r'^accounts/profile/$', RedirectView.as_view(url='/en-us/accounts/profile/'), name='english-profile'),

    # Include admin as convenience. It's unsupported and you should
    # use the dashboard
    url(r'^admin/', include(admin.site.urls)),
    # i18n URLS need to live outside of i18n_patterns scope of the shop
    url(r'^i18n/', include('django.conf.urls.i18n')),
    # include a basic sitemap
    url(r'^sitemap\.xml$', 'django.contrib.sitemaps.views.index', {
        'sitemaps': base_sitemaps}),
    url(r'^sitemap-(?P<section>.+)\.xml$',
        'django.contrib.sitemaps.views.sitemap', {'sitemaps': base_sitemaps}),
]

# Prefix Oscar URLs with language codes
urlpatterns += i18n_patterns('',
    # Custom functionality to allow dashboard users to be created
    url(r'gateway/', include('apps.gateway.urls')),
    # Oscar's normal URLs
    url(r'', include(shop.urls)),
)


urlpatterns += patterns('',
    # basic configuration for Oscar
    url(r'', include(shop.urls)),

    # adds URLs for the dashboard store manager
    url(r'^dashboard/stores/', include(dashboard_app.urls)),

    # adds URLs for overview and detail pages
    url(r'^stores/', include(stores_app.urls)),

    # adds internationalization URLs
    (r'^jsi18n/$', 'django.views.i18n.javascript_catalog'),
)


if settings.DEBUG:
    import debug_toolbar

    # Server statics and uploaded media
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    # Allow error pages to be tested
    urlpatterns += [
        url(r'^403$', handler403),
        url(r'^404$', handler404),
        url(r'^500$', handler500),
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
