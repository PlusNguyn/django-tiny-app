from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from .views import delete_selected_posts

urlpatterns = [
    path('signup/', views.sign_up, name='users-signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html')
         , name='users-login'),
    path('logout/', views.logout_view, name='users-logout'),
    path('profile/', views.profile, name='users-profile'),
    path("delete-selected/", delete_selected_posts, name="delete-selected-posts"),
]