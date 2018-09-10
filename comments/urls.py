from django.urls import re_path
from comments import views

app_name = 'comments'
urlpatterns = [
    re_path('comment/post/(?P<post_pk>[0-9]+)/', views.post_comment, name='post_comment'),
]