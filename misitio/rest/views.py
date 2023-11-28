from django.shortcuts import render
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest.serializer import UserSerializer, GroupSerializer, EventoSerializer
from .models import Evento


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class EventoViewSet(viewsets.ModelViewSet):
    queryset=Evento.objects.all()
    serializer_class = EventoSerializer



def index(request):
    title = "Inicio"

    eventos = Evento.objects.all()
    tipos = Evento.tipos
    segmentos = Evento.segmentos
    data = {
        "title": title,
        "eventos":eventos,
        "tipos": tipos,
        "segmentos": segmentos
    }

    return render(request,'miapp/index.html', data)