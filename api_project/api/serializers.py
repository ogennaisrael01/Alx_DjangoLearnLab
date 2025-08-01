from api.models import Book
from rest_framework.serializers import ModelSerializer, DateTimeField
import datetime
class BookSerializer(ModelSerializer):
    created_at = DateTimeField(default=datetime.datetime.now().strftime("%Y-%m-%d  %H,%M,%S"))
    class Meta:
        model = Book
        fields = ["title", "author", "created_at"]
        read_only_fields = ["created_at"]

    