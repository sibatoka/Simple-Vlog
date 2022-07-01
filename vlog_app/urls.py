from django.urls import path
from .views import *

urlpatterns = [
    path('post-detail/<int:post_id>/', post_detail, name='post-detail'),
    path('edit-post/<int:post_id>', edit_post, name='edit-post'),
    path('create-post/', create_post, name='create-post'),
    path('sing-up/', registration, name='sing-up'),
    path('my-profile/', my_profile, name='my-profile'),
    path('', index, name='index'),
]
