from django.conf.urls import include, url
from django.contrib import admin
from .views import ApiEndpoint

urlpatterns = [
    # Examples:
    # url(r'^$', 'DrReminders.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^o/', include('oauth2_provider.urls', namespace='oauth2_provider')),
    url(r'^api/hello', ApiEndpoint.as_view()),  # and also a resource server!
    url(r'^secret$', 'DrReminders.views.secret_page', name='secret'),
    url(r'^login$', 'DrReminders.views.login', name='login'),
]
