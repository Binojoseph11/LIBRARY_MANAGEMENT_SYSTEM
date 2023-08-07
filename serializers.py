from rest_framework import serializers
from book.models import book


class bookserializer(serializers.ModelSerializer):
    class Meta:
        model=book
        fields="__all__"

class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = book
        fields = '__all__'


