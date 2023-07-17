from django.contrib import admin
from .models import Message, Room
# c'est dans ce fichier que nous allons répertorié les différentes table de la base de données

admin.site.register(Message)
admin.site.register(Room)