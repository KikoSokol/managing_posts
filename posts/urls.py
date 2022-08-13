from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.PostList.as_view()),
    path('post/<int:pk>/', views.PostDetail.as_view()),
    path('user/<int:user_id>/post/', views.UserPostList.as_view())
]
