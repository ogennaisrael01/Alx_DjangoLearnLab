from api.models import Book
from rest_framework import serializers
import datetime
class BookSerializer(serializers.ModelSerializer):
    created_at = serializers.DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d  %H,%M,%S"))
    class Meta:
        model = Book
        fields = ["title", "author", "created_at"]
        read_only_fields = ["created_at"]

    