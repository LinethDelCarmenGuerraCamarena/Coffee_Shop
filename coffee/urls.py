from django.urls import path
from .views import coffee, agregar_producto, eliminar_producto, restar_producto, limpiar_carrito

app_name = 'coffee'  # ← ¡IMPORTANTE!

urlpatterns = [
    path('', coffee, name="Coffee"),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
]