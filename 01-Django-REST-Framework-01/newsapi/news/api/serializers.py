from rest_framework import serializers
from news.models import Article


class ArticleSerializer(serializers.Serializer):
    #! with the serializer class we are going to get a JSON representation of every field
    id = serializers.IntegerField(read_only=True)
    author = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    body = serializers.CharField()
    location = serializers.CharField()
    publication_date = serializers.DateField()
    active = serializers.BooleanField()
    created_at = serializers.DateTimeField(read_only=True)
    updated_at = serializers.DateTimeField(read_only=True)

    def create(self, validated_data):
        print("validated_data: ", validated_data)
        return Article.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.author = validated_data.get("author", instance.author)
        # this syntax .get("author",instance.author) --> means that if there is no author data, then use with the one that you already have
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.body = validated_data.get("body", instance.body)
        instance.location = validated_data.get("location", instance.location)
        instance.publication_date = validated_data.get(
            "publication_date", instance.publication_date
        )
        instance.active = validated_data.get("active", instance.active)

        instance.save()
        return instance


"""
! serialization of data with Renderers
>>> python manage.py shell
>>> from news.models import Article
>>> from news.api.serializers import ArticleSerializer

>>> article_instance = Article.objects.first()
>>> article_instance
...
>>> serializer = ArticleSerializer(article_instance)
>>> serializer
...

>>> serializer.data
--> it represents the data of our article instance

>>> from rest_framework.renderers import JSONRenderer
>>> data_json = JSONRenderer().render(serializer.data)
>>> data_json
b'{"id":1,"author":"John Doe","title":"20 years for the International Station","description":"nice description","body":"content","location":"Earth","publication_date":"2023-02-06","active":true,"created_at":"2023-02-06T10:56:51.919536Z","updated_at":"2023-02-06T10:56:51.919618Z"}'

! de-serialization of data with Parsers
--> we need to parse a string into python native data types
>>> import io
>>> from rest_framework.parsers import JSONParser

>>> stream = io.BytesIO(data_json)
>>> data = JSONParser().parse(stream)
>>> data
...

>>> serializer = ArticleSerializer(data=data)
>>> serializer.is_valid()
True
>>> serializer.validated_data
OrderedDict([('author', 'John Doe'), ('title', '20 years for the International Station'), ('description', 'nice description'), ('body', 'content'), ('location', 'Earth'), ('publication_date', datetime.date(2023, 2, 6)), ('active', True)])
>>> serializer.save()
validated_data:  {'author': 'John Doe', 'title': '20 years for the International Station', 'description': 'nice description', 'body': 'content', 'location': 'Earth', 'publication_date': datetime.date(2023, 2, 6), 'active': True}
<Article: John Doe 20 years for the International Station>
# --> we get back a clone, a new instance of the article that we previously created

>>> Article.objects.all()
<QuerySet [<Article: John Doe 20 years for the International Station>, <Article: John Doe 20 years for the International Station>]>
--> we get back a queryset with 2 instances

#! a Parser is a class that allows the rest API to accept and comprehend different kind of requests (there are different kinds of parsers, one of which is JSONParser)
# NB DRF will automatically decide what kind of parser is optimal for a specific request, based on the value that is associated with the content type header
#! a Rendere is a class that allows us to provide different kinds of responses or to personlize them
"""
