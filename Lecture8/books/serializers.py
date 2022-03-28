from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from books.models import Book, Publisher, Author
from utils.validators import num_pages_range_validation


# class BookSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField()
#     publication_date = serializers.DateTimeField()
#     num_pages = serializers.IntegerField()
#
#     def update(self, instance, validated_data):
#         instance.title = validated_data.get('title', instance.title)
#         instance.num_pages = validated_data.get('num_pages', instance.num_pages)
#         instance.publication_date = validated_data.get('publication_date', instance.publication_date)
#         instance.save()
#         return instance
#
#     def create(self, validated_data):
#         return Book.objects.create(**validated_data)


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = ('id', 'name', 'address',)


class BookSerializer(serializers.ModelSerializer):
    num_pages = serializers.IntegerField(validators=[num_pages_range_validation])

    class Meta:
        model = Book
        fields = ('id', 'title', 'publication_date', 'num_pages')

    # def validate_num_pages(self, value):
    #     if value > 1000:
    #         raise ValidationError('must be less than or equal to 1000')
    #     return value
    #
    # def validate(self, attrs):
    #     if attrs['num_pages'] > 1000:
    #         raise ValidationError({'num_pages': 'must be less than or equal to 1000'})
    #     return attrs


class BookDetailSerializer(BookSerializer):
    publisher = PublisherSerializer(read_only=True)
    book_authors = AuthorSerializer(source='authors', many=True, read_only=True)

    class Meta(BookSerializer.Meta):
        fields = BookSerializer.Meta.fields + ('publisher', 'book_authors',)
