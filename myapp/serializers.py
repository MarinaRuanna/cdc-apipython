from .models import Autor
from rest_framework import serializers


class AutorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Autor
        fields = ('name', 'email', 'descricao')
