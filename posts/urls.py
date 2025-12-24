from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # Homepage with all posts
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  # Single post view
    path('create/', views.create_post, name='create_post'),  # Create post (login required)
    
    # Guest account URLs
    path('guest-signup/', views.guest_signup, name='guest_signup'),
    path('guest-login/', views.guest_login, name='guest_login'),
    path('logout/', views.user_logout, name='logout'),  # Logout URL
]
