
from django.urls import path
from .views import BlogPostRudView, BlogPostAPIView, BlogPostListView, BlogPostAPIMixView


app_name='api-postings'

urlpatterns = [
    path('', BlogPostAPIMixView.as_view(), name='post-listcreate'),
    path('<int:id>/', BlogPostRudView.as_view(), name='post-rud'),
    path('normal/', BlogPostAPIView.as_view(), name='post-list-norm'),
    path('create/', BlogPostAPIView.as_view(), name='post-create'),
]