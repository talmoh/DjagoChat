from datetime import datetime
from django.db import models

# Ce fichier défini la structure de la base de données en utilisant des modéles d'objets

class Room(models.Model): #cest la classe qui représente le groupe de discussion
    name=models.CharField(max_length=2000)

class Message(models.Model): #c'est la classe qui représente les messages
    value=models.CharField(max_length=1000000) #la valeur du message (combien es quil contient de caractères)
    date = models.DateTimeField(default= datetime.now , blank = True) #date du message par défaut ça sera la date actuelle
    user = models.CharField(max_length=1000000) #l'utilisateur qui a envoyer le message
    room = models.CharField(max_length=1000000) #ce champ contient l'ID de la classe room et permet de relier les deux classes