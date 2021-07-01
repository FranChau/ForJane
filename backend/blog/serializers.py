from rest_framework import serializers
from .models import Article, LANGUAGE_CHOICES, STYLE_CHOICES


class ArticleListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(allow_blank=True, max_length=100)
    abstract = serializers.CharField(max_length=200)
    body = serializers.CharField(allow_blank=True)
    created = serializers.DateTimeField()
    updated = serializers.DateTimeField()

    # 代码
    code = serializers.CharField(style={'base_template': 'textarea.html'})
    linenos = serializers.BooleanField(required=False)
    language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
    style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')

    def create(self, validated_data):
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        # instance.abstract = validated_data.get('abstract', instance.abstract)
        # instance.body = validated_data.get('body', instance.body)
        instance.code = validated_data.get('code', instance.code)
        instance.linenos = validated_data.get('linenos', instance.linenos)
        instance.language = validated_data.get('language', instance.language)
        instance.style = validated_data.get('style', instance.style)
        instance.save()
        return instance
