from rest_framework import serializers
from Newspaper.models import *

class NewspaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = [
            'name',
            'pk',
            'school',
            'description',
            'city',
            'state',
            'website'
        ]

class NewspaperSerializerWithSections(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = [
            'name',
            'pk',
            'school',
            'description',
            'city',
            'state',
            'website',
            'sections'
        ]


class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Section
        fields = [
            'parentPaper',
            'name',
            'wordpressTag',
        ]

