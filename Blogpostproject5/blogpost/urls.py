from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='homepage'),
    path('post/<slug>/', views.post, name = 'post'),
    path('post/<slug:slug>/', views.post, name='post_detail'),
    path('post/<slug:slug>/like/', views.like_post, name='like_post'),
    path('about/', views.about, name='about'),
    path('search/', views.search, name='search'),
    path('postlist/<slug>/', views.postlist, name='postlist'),
    path('posts/', views.allposts, name='allposts'),
    path('tag/', views.tag_list, name='tag_list'),
    path('weapons/', views.weapons, name='weapons'),
    path('post/<slug:slug>/favorite/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path("polls/", include("polls.urls")),
    path("admin/", admin.site.urls)
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)




