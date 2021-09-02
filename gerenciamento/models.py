from django.db import models

class Empresa(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True, default='')
    email = models.EmailField(max_length=100, blank=False, null=False, default='')
    telefone = models.CharField(max_length=100, blank=True, null=True, default='')
    whatsapp = models.CharField(max_length=100, blank=True, null=True, default='')  
    cep = models.CharField(max_length=10, blank=True, null=True, default='')
    endereco = models.CharField(max_length=255, blank=True, null=True, default='')
    bairro = models.CharField(max_length=50, blank=True, null=True, default='')
    cidade = models.CharField(max_length=50, blank=True, null=True, default='')
    uf = models.CharField(max_length=2, blank=True, null=True, default='')    
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    nome = models.CharField(max_length=100, blank=False, null=True, default='')
    email = models.EmailField(max_length=100, blank=False, null=False, default='')
    telefone = models.CharField(max_length=100, blank=True, null=True, default='')
    whatsapp = models.CharField(max_length=100, blank=True, null=True, default='')  
    cep = models.CharField(max_length=10, blank=True, null=True, default='')
    endereco = models.CharField(max_length=255, blank=True, null=True, default='')
    bairro = models.CharField(max_length=50, blank=True, null=True, default='')
    cidade = models.CharField(max_length=50, blank=True, null=True, default='')
    uf = models.CharField(max_length=2, blank=True, null=True, default='')  
    empresa = models.ForeignKey(Empresa, blank=True, null=True, on_delete=models.CASCADE)  
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        ordering = ['nome']
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome

class Quadro(models.Model):
    aviso = models.TextField(max_length=200, blank=False, null=False)
    video = models.CharField(max_length=100, blank=True, null=True, default='')
    is_active = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True, blank=True, null=True)
    class Meta:
        verbose_name_plural = 'Quadro Avisos'
    def __str__(self):
        return self.aviso
