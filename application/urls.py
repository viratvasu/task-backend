from django.urls import path
from .views import parse_file_data, get_all_data, initial_handshake
urlpatterns = [
    path('parse_and_save_data/', parse_file_data),
    path('get_all/', get_all_data),
    path('handshake/', initial_handshake)
]
