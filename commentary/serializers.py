from commentary.models import Commentary
from rest_framework import serializers


class CommentSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Commentary
        fields = ('id', 'body', 'owner', 'post')