from rest_framework import serializers
from . import models
from .models import Developer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        print(model)
        fields = (
            'id', 'name', 'email', 'technology', 'domain', 'location', 'experience',  'question', 'project', 'blogs',
            'score')
