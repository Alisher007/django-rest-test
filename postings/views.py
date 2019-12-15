from rest_framework import generics, mixins
from django.db.models import Q
from postings.models import BlogPost
from .serializers import BlogPostSerializer
from .permissions import IsOwnerOrReadOnly

class BlogPostListView(generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()

class BlogPostAPIView(generics.CreateAPIView):
    lookup_field = 'id'
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class BlogPostAPIMixView(mixins.CreateModelMixin, generics.ListAPIView):
    lookup_field = 'id'
    serializer_class = BlogPostSerializer
    permission_class = [IsOwnerOrReadOnly]

    def get_queryset(self):
        qs = BlogPost.objects.all()
        query = self.request.GET.get('q')
        if query is not None:
            qs = qs.filter(Q(title__icontains=query)|Q(content__icontains=query)).distinct()
        return qs
    
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def get_serializer_context(self,*arg,**kwargs):
        return {"request":self.request}

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'id'
    serializer_class = BlogPostSerializer
    permission_class = [IsOwnerOrReadOnly]

    def get_queryset(self):
        return BlogPost.objects.all()
    
    