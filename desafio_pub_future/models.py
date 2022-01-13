from django.db import models
from django.contrib.auth.models import User


class Income(models.Model):
    class ITypes(models.IntegerChoices):
        BON = 1, 'Bonus'
        INV = 2, 'Invesimentos'
        OTH = 3, 'Outros'
        GIF = 4, 'Presente'
        SAL = 5, 'Salario'

    class RInterval(models.IntegerChoices):
        NA = 1, 'Não se aplica'
        DAY = 2, 'Dias'
        WEK = 3, 'Semanas'
        MON = 4, 'Meses'
        YEA = 5, 'Anos'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='incomes')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveIntegerField(choices=ITypes.choices)
    comment = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.id} - {self.type} - {self.date.strftime("%D/%m/&y")}'

    class Meta:
        verbose_name_plural = 'incomes'


class Expense(models.Model):
    class ETypes(models.IntegerChoices):
        HOM = 1, 'Casa'
        EDU = 2, 'Educação'
        ELE = 3, 'Eletrônicos'
        REC = 4, 'Lazer'
        OTH = 5, 'Outros'
        CAR = 6, 'Transporte'
        RES = 7, 'Restaurante'
        CLO = 8, 'Roupas'
        HEA = 9, 'Saúde'
        SER = 10, 'Serviços'
        SUP = 11, 'Supermercado'
        TRA = 12, 'Viajem'

    class RInterval(models.IntegerChoices):
        NA = 1, 'Não se aplica'
        DAY = 2, 'Dias'
        WEK = 3, 'Semanas'
        MON = 4, 'Meses'
        YEA = 5, 'Anos'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='expenses')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveIntegerField(choices=ETypes.choices)
    comment = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Expense {self.id} - {self.type} - {self.date.strftime("%D/%m/&y")}'

    class Meta:
        verbose_name_plural = 'Expenses'


class Balance(models.Model):
    class BType(models.IntegerChoices):
        CUR = 1, 'Corrente'
        SAV = 2, 'Poupança'

    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='balances')
    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.PositiveIntegerField(choices=BType.choices)
    date = models.DateField()
    comment = models.TextField(null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Balance {self.id} - {self.type}'

    class Meta:
        verbose_name_plural = 'Balances'
