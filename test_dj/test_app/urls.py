from django.urls import path
from . import views


app_name = 'test_app'
urlpatterns = [
    path('', views.hello, name='hello'),
    path('posts/', views.posts_list, name='posts'),
    path('gposts/', views.PostListView.as_view(), name='gposts'),
    path('groups/', views.groups_list, name='groups'),
    path('post/<int:post_id>/', views.post_detail, name='post'),
    # path('group/<int:group_id>/', views.group_posts, name='group_posts'),
]