from django.db import models

# class EstoqueGeral(models.Model):


class Equipamento(models.Model):
    objects = None
    patrimonio = models.IntegerField('Patrimonio', primary_key=True)
    modelo = models.CharField('Modelo', max_length=100)
    numeroserie = models.CharField('Numero de Serie', max_length=100)
    especificacao = models.CharField('Especificacao', max_length=200)
    preco = models.DecimalField('Preço', decimal_places=2, max_digits=8)
    situacao = models.CharField('Situacao', max_length=50)
#   begin_date = models.DateTimeField(auto_now_add=True)
#    user = models.ForeignKey(User, on_delete=models.CASCADE, default='')

    def __str__(self):
        return f'{self.patrimonio, self.modelo, self.numeroserie, self.especificacao, self.preco, self.situacao}'


class Entregas(models.Model):
    CONTRATO_CHOICES = [
        ('EA', 'EQUIPE AGEIS'),
        ('TD', 'TRANSFORMACAO DIGITAL'),
        ('CDS_SP', 'PMSP'),
        ('NC', 'NAO CRITICAS')
    ]
    matricula_func = models.IntegerField('Matricula')
    nome_func = models.CharField('Nome', max_length=100)
    sobrenome = models.CharField('Sobre nome', max_length=100)
    email = models.EmailField('E-mail', max_length=100)
    telefone = models.IntegerField('Telefone')
    contrato = models.CharField(choices=CONTRATO_CHOICES, default='available', max_length=32)
    data_admissao = models.DateField('Data Admissao')
#   data_entrega = models.DateField('Data da Entrega')
#   begin_date = models.DateTimeField(auto_now_add=True, default='')
#    active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.matricula_func, self.nome_func, self.sobrenome, self.email, self.telefone,self.contrato, self.data_admissao}'