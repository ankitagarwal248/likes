from django.conf.urls import patterns, include, url
from likes import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='default'),
        url(r'^register/$', views.user_register, name='register'),
        url(r'^login/$', views.user_login, name='login'),
        url(r'^logout/$', views.user_logout, name='logout'),
        url(r'^advertiser/$', views.advertiser, name='advertiser'),
        url(r'^advertiser/create_campaign/$', views.create_campaign, name='create_campaign'),
        url(r'^advertiser/activate_campaign/(?P<id>\d+)/$', views.activate_campaign, name='activate_campaign'),
        url(r'^advertiser/deactivate_campaign/(?P<id>\d+)/$', views.deactivate_campaign, name='deactivate_campaign'),
        url(r'^advertiser/delete_campaign/(?P<id>\d+)/$', views.delete_campaign, name='delete_campaign'),
        url(r'^publisher/$', views.publisher, name='publisher'),
        url(r'^publisher/create_post/$', views.create_post, name='create_post'),
        url(r'^publisher/delete_post/(?P<id>\d+)/$', views.delete_post, name='delete_post'),
        url(r'^publisher/share_article/$', views.share_article, name='share_article'),
        url(r'^(?P<username>\w+)/$', views.page, name='page'),
)
