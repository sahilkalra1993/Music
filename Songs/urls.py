from django.conf.urls import url
from . import views


app_name = 'songs'
urlpatterns = [
    # 127.0.0.1/Songs/
    url(r'^$', views.IndexView.as_view(), name='index'),
    
    # 127.0.0.1/Songs/23/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    
    # 127.0.0.1/Songs/23/favorite/
    #url(r'^(?P<album_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    
    url(r'^album/add$', views.AlbumCreate.as_view(), name = 'album-add'),
    
    url(r'^album/(?P<pk>[0-9]+)$', views.AlbumUpdate.as_view(), name='album-update'),
    
    url(r'^album/(?P<pk>[0-9]+)/delete$', views.AlbumDelete.as_view(), name='album-delete'),
]
