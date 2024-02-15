from django.urls import path
from .views import index_view, autor_view

urlpatterns = [
    path('', index_view),
    path('autor/<int:id>/', autor_view, name='autor_view'),
]
