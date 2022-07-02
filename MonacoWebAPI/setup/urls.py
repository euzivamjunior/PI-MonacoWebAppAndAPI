from django.contrib import admin
from django.urls import path, include
from services.views import FormularioViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register('formulario', FormularioViewSet, basename='Formularios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
