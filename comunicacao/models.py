from django.db import models
from gerenciamento.models import Funcionario

class Servico(models.Model):    
    descricao = models.CharField(max_length=100, blank=True, null=True, default='')
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Serviços Funcionários'
    def __str__(self):
        return self.descricao


class Atendimento(models.Model):
    funcionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.CASCADE)
    pedido = models.TextField(max_length=200, blank=False, null=False)
    servico = models.ForeignKey(Servico, blank=True, null=True, on_delete=models.CASCADE)  
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    is_active = models.BooleanField(default=False)
    class Meta:
        ordering = ['created_on']
        verbose_name_plural = 'Atendimentos'

    def __str__(self):
        return self.pedido