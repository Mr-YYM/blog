from rest_framework import generics
from article.models import Article
from .permissons import IsAdminUserOrReadOnly
from article.serializers import ArticleListSerializer, ArticleDetailSerializer


class ArticleList(generics.ListCreateAPIView):
    permission_classes = [IsAdminUserOrReadOnly]

    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUserOrReadOnly]
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
