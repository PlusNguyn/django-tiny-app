from django.urls import path
from . import views
<<<<<<< HEAD
from .views import CustomLoginView
=======

>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
urlpatterns = [
    path('', views.index, name='blog-index'),
    path('post_detail/<int:pk>/', views.post_detail, name='blog-post-detail'),
    path('post_edit/<int:pk>/', views.post_edit, name='blog-post-edit'),
    path('post_delete/<int:pk>/', views.post_delete, name='blog-post-delete'),
<<<<<<< HEAD
    path('login/', CustomLoginView.as_view(), name='login'),
=======
>>>>>>> c9d53560519aa7997bdcdb498b8a0989ca5cb426
]