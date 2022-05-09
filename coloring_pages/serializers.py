from rest_framework import serializers

from .models import *

class ColoringPageSerializar(serializers.ModelSerializer):
    class Meta:
        model=Coloring_page
        fields=('__all__')

class TemaSerializar(serializers.ModelSerializer):
    class Meta:
        model=Tema
        fields=('__all__')

class CategorySerializar(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields=('__all__')