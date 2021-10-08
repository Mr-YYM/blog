from article.models import Article
from .permissons import IsAdminUserOrReadOnly

from rest_framework import filters
from rest_framework import viewsets
from article.serializers import ArticleSerializer
from article.serializers import ArticleDetailSerializer


from article.models import Category
from article.serializers import CategorySerializer

from article.models import Tag
from article.serializers import TagSerializer

class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [IsAdminUserOrReadOnly]

class CategoryViewSet(viewsets.ModelViewSet):
    """分类视图集"""
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [IsAdminUserOrReadOnly]


class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    permission_classes = [IsAdminUserOrReadOnly]

    filter_backends = [filters.SearchFilter]
    search_fields = ['title']

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
    
    def get_serializer_class(self):
        if self.action == 'list':
            return ArticleSerializer
        else:
            return ArticleDetailSerializer
