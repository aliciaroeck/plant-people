from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='landing'),
    path('login/', views.login, name='login'),
    path('community/', views.community, name='community'),
    path('profile/', views.profile, name='profile'),
    path('edit_profile/', views.edit_profile, name='edit_profile'),
    path('<int:post_id>/edit_post/', views.edit_post, name='edit_post'),
    path('<int:post_id>/delete_post/', views.delete_post, name='delete_post'),
]