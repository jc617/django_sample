from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # Examples:
    # url(r'^$', 'hammer2.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
	url(r'^$', 'job.views.index', name='index'), 
	url(r'^job/', include('job.urls')),

	url(r'^admin/', include(admin.site.urls)),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

