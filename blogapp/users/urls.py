from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
<<<<<<< HEAD
<<<<<<< HEAD
from .views import delete_selected_posts
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426

urlpatterns = [
    path('signup/', views.sign_up, name='users-signup'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html')
         , name='users-login'),
    path('logout/', views.logout_view, name='users-logout'),
    path('profile/', views.profile, name='users-profile'),
<<<<<<< HEAD
<<<<<<< HEAD
    path("delete-selected/", delete_selected_posts, name="delete-selected-posts"),
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
]