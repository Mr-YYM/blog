from rest_framework import generics
from article.models import Article
# 这个 ArticleListSerializer 暂时还没有
from article.serializers import ArticleListSerializer, ArticleDetailSerializer

class ArticleList(generics.ListCreateAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleListSerializer


class ArticleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
