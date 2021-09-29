from django.urls import path, include
from rest_framework.routers import DefaultRouter
from article import views

router = DefaultRouter()
router.register(r'article', views.ArticleViewSet)

app_name = 'article'

urlpatterns = [
    path('api/', include(router.urls)),
]