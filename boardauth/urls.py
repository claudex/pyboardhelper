from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login),
    path('oauth', views.oauth_view, name='oauth'),
    path('post_dlfp', views.post_dlfp),
    path('post_euromussels', views.post_euromussels),
]
