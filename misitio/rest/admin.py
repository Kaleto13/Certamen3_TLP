from django.contrib import admin
from .models import Evento


#admin.site.register(Evento)


@admin.register(Evento)
class EventoAdmin(admin.ModelAdmin):
    list_display=('id','titulo','tipo','segmento')
    list_display_links = ('titulo',)
    list_filter = ('tipo',)
# Register your models here.
