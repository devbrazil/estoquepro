from django.contrib import admin

from .models import Entregas, Equipamento


class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('patrimonio', 'modelo', 'numeroserie', 'especificacao', 'preco', 'situacao',)


admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Entregas)