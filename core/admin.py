from django.contrib import admin

import estoque_pro
from .models import Entregas, Equipamento


class EquipamentoAdmin(admin.ModelAdmin):
    list_display = ('patrimonio', 'modelo', 'numeroserie', 'especificacao', 'preco', 'situacao',)


class EstoqueAdmin(admin.ModelAdmin):
    list_display = ['nome']


admin.register(estoque_pro)
admin.site.register(Equipamento, EquipamentoAdmin)
admin.site.register(Entregas)
