from rest_framework import viewsets
from services.models import Formulario
from services.serializer import FormularioSerializer


class FormularioViewSet(viewsets.ModelViewSet):
    """Exibindo todos os formulários de serviço"""
    queryset = Formulario.objects.all()
    serializer_class = FormularioSerializer
