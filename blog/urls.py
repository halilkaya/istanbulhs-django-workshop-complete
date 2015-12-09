from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from app import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    url(r'^post/(?P<post_slug>[-_\w]+)/$', views.post_single, name='post_single'),
    url(r'^page/(?P<page_slug>[-_\w]+)/$', views.page, name='page'),
    url(r'^category/(?P<category_slug>[-_\w]+)/$', views.category, name='category_page'),
    url(r'^search/$', views.post_search, name="search_form"),
    url(r'^$', views.index, name='index'),
]
