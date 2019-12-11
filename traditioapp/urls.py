from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

from . import views
from .views import create_post, create_trad, create_songs, create_latest, about, search_results

urlpatterns = [
    path('', views.index, name='index'),
    path('signup/', views.signup, name='signup'),
    path('account/', include('django.contrib.auth.urls')),
    path('add_post', create_post, name='add_post'),
    path('add_trad', create_trad, name='add_trad'),
    path('add_song', create_songs, name='add_song'),
    path('add_latest', create_latest, name='add_latest'),
    path('profile/<username>', views.profile, name='profile'),
    path('profile/<username>/edit/', views.edit_profile, name='edit_profile'),
    path('search/', search_results, name='search_results'),
    path('about', about, name='about'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
