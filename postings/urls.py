
from django.urls import path
from .views import BlogPostRudView


app_name='api-postings'

urlpatterns = [
    path('<int:id>', BlogPostRudView.as_view(), name='post-rud'),
]