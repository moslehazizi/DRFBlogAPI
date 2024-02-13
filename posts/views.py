from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializers, UserSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework import viewsets

class PostViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializers

class UserViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer
