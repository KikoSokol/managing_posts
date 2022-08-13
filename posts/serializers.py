from rest_framework import serializers
from posts import models


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = '__all__'

    def validate_title(self, value):
        if len(value) < 5:
            raise serializers.ValidationError("Title must contain at least 5 characters.")

        return value


class PostUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Post
        fields = ["title", "body"]
