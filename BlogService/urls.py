from django.urls import path
from .views import BlogPostCreateView,BlogPostDeleteView,BlogPostUpdateView

urlpatterns=[
    path('users/create-post/',BlogPostCreateView.as_view(), name='blogpost-create'),
    path('users/update-post/<int:pk>/', BlogPostUpdateView.as_view(), name='blogpost-update'),
    path('users/delete-post/<int:pk>/', BlogPostDeleteView.as_view(), name='blogpost-delete'),
]