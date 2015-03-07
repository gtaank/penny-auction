from web.users.views import dashboard, login, logout

from django.conf.urls import patterns, url


urlpatterns = patterns('',
                       url(r'^login/?$', login.login_view, name='login_page'),
                       url(r'^logout/?$', logout.logout_page, name='logout_page'),
                       url(r'^/?$', dashboard.dashboard_view, name='dashboard_page'),
)
