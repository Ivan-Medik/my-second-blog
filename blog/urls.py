from django.urls import path
from .views import *


urlpatterns = [
    path('', posts_list, name="posts_list_url"),
    path('contact/', contact, name="contact_url"),
    path('post/create/', PostCreate.as_view(), name='post_create_url'),
    path('post/<str:slug>/', PostDetail.as_view(), name="post_detail_url"),
    path('post/<str:slug>/update/', PostUpdate.as_view(), name="post_update_url"),
    path('post/<str:slug>/delete/', PostDelete.as_view(), name="post_delete_url"),
    #path('post/<str:slug>/leave_comment/', views.detail, name="post_comment_url"),
    path('tags/', tags_list, name="tags_list_url"),
    path('tag/create/', TagCreate.as_view(), name = "tag_create_url"),
    path('tags/<str:slug>/', TagDetail.as_view(), name="tag_detail_url"),
    path('tags/<str:slug>/update/', TagUpdate.as_view(), name="tag_update_url"),
    path('tags/<str:slug>/delete/', TagDelete.as_view(), name="tag_delete_url"),
]
