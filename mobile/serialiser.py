from rest_framework import serializers
from .models import Information


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = [
            'id', 'titre', 'description',
            'date_de_creation', 'source',
            'image',
        ]
