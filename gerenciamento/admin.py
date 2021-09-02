from django.contrib import admin
from gerenciamento.models import Empresa, Funcionario, Quadro
# Register your models here.
@admin.register(Empresa)
class Empresa(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'whatsapp', 'cidade', 'uf', )  

@admin.register(Funcionario)
class Funcionario(admin.ModelAdmin):
    list_display = ('nome', 'email', 'telefone', 'whatsapp', 'cidade', 'uf', 'empresa', )  

@admin.register(Quadro)
class Quadro(admin.ModelAdmin):
    list_display = ('aviso', 'video', 'is_active',  )  
