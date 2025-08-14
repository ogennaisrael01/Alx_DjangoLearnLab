from rest_framework import serializers
from api.models import Author, Book
from django.utils import timezone


class BookSerializer(serializers.Serializer):
    """ Serializer for the Book model. """
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all()) # ForeignKey to Author model
    title = serializers.CharField(max_length=100)
    publication_year = serializers.IntegerField()

    def create(self, validated_data):
        """ Create a new Book instance with the validated data. """
        return Book.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        """ Update an existing Book instance with the validated data. """
        instance.author = validated_data.get("author", instance.author)
        instance.title = validated_data.get("title", instance.title)
        instance.publication_year = validated_data.get("publication_year", instance.publication_year)
        instance.save()
        return instance
    
    def validate_publication_year(self, value):
        """ Validate that the publication year is not greater than the current year. """
        if value > timezone.datetime.today().year():
            raise serializers.ValidationError(" Publication year can't be greater than today")
        return value


class AuthorSerializer(serializers.ModelSerializer):
    """ Serializer for the Author model. """
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ["name", "books"]
