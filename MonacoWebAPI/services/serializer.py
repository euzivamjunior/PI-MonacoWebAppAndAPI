from rest_framework import serializers
from services.models import Formulario


class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        # fields = '__all__'
        exclude = ('confirmado', 'servico_realizado')  # disponibiliza todos os dados, exceto estes.
