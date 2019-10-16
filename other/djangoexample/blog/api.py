import rest_framework.viewsets as rest_viewsets
from .models import Article
from .serializers import ArticleSerializer


class ArticleViewSet(rest_viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer

    def bulk_create(self, validated_data):
        return Article.objects.bulk_create(Article(**param) for param in validated_data)
