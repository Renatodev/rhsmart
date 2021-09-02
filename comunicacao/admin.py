from django.contrib import admin

from comunicacao.models import Servico, Atendimento
admin.site.site_header = "Integra RH"
admin.site.site_title = "Integra RH Comunicação Interna"
admin.site.index_title = "Seja bem vindo(a)"
@admin.register(Servico)
class Servico(admin.ModelAdmin):
    list_display = ( 'descricao', 'is_active', )  

@admin.register(Atendimento)
class Servico(admin.ModelAdmin):
    list_display = ( 'created_on', 'funcionario','pedido','servico', 'is_active',)  
