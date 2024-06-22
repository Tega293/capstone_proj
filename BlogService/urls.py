from django.urls import path
from .views import BlogPostList_CreateEndpoint,BlogPostByCategoryListView,BlogPostByUserListView,CategoryCreate__ListEndPoint,BlogPostDetailEndPoint

urlpatterns=[
    path('users/post/create/',BlogPostList_CreateEndpoint.as_view(), name='blogpost-create'),
    path('users/post/update/<int:pk>/', BlogPostDetailEndPoint.as_view(), name='blogpost-update'),
    path('users/post/delete/<int:pk>/', BlogPostDetailEndPoint.as_view(), name='blogpost-delete'),
     path('categories/create/', CategoryCreate__ListEndPoint.as_view(), name='category-create'),
    path('posts/category/<int:category_id>/',BlogPostByCategoryListView.as_view(),name='posts-by-category'),
    path('users/retrieve-post/<int:pk>/', BlogPostDetailEndPoint.as_view(), name='post-detail'),
    path('posts/user/<int:user_id>/', BlogPostByUserListView.as_view(), name='posts-by-user'),
    path('users/post/list/', BlogPostList_CreateEndpoint.as_view(), name='blogpost-list'),
    path('categories/list/',CategoryCreate__ListEndPoint.as_view(), name='categories-list')
]