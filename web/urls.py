from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()
import web.users.urls
import web.auctions.urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pennyauction.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(web.users.urls)),
    url(r'^', include(web.auctions.urls)),
)
