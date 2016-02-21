import rest_framework.serializers as rest_serializers
from .models import Article


class ArticleListSerializer(rest_serializers.ListSerializer):
    pass


class ArticleSerializer(rest_serializers.ModelSerializer):
    code = rest_serializers.CharField(max_length=140, trim_whitespace=True, read_only=True)
    subject = rest_serializers.CharField(max_length=140, trim_whitespace=True)
    body = rest_serializers.CharField(trim_whitespace=True)
    published_at = rest_serializers.DateTimeField(
        format='iso-8601', input_formats=['iso-8601'], required=False)

    class Meta:
        model = Article
        fields = (
            'code',
            'subject',
            'body',
            'published_at',
            )
        list_serializer_class = ArticleListSerializer

    def create(self, validated_data):
        return self.Meta.model.objects.create(
            subject=validated_data['subject'],
            body=validated_data['body'],
            published_at=validated_data.get('published_at'),
            )
