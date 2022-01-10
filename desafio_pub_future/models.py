from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class MyAccountManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Usuarios precisam ter um email!')
        if not username:
            raise ValueError('Usuarios precisam ter um nome!')

        user = self.model(
            email=self.normalize_email(email),
            username=username,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, password):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Account(AbstractBaseUser):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    username = models.CharField(max_length=30)
    date_joined = models.DateTimeField(verbose_name='date joined', auto_now_add=True)
    last_login = models.DateTimeField(verbose_name='last login', auto_now=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username',]

    objects = MyAccountManager()

    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True


class Income(models.Model):
    class ITypes(models.IntegerChoices):
        SAL = 1, 'SALARY'
        BON = 2, 'BONUS'
        GIF = 3, 'GIFT'
        OTH = 4, 'OTHER'

    class RInterval(models.IntegerChoices):
        NA = 1, 'N/A'
        DAY = 2, 'DAYS'
        WEK = 3, 'WEEKS'
        MON = 4, 'MONTHS'
        YEA = 5, 'YEARS'

    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveIntegerField(choices=ITypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default=0)
    comment = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Income {self.id} - {self.type} - {self.date.strftime("%D/%m/&y")}'

    class Meta:
        verbose_name_plural = 'incomes'


class Expense(models.Model):
    class ETypes(models.IntegerChoices):
        REN = 1, 'RENT'
        BIL = 2, 'BILLS'
        CAR = 3, 'CAR'
        TRA = 4, 'TRAVEL'
        HEA = 5, 'HEALTH'
        GRO = 6, 'GROCERIES'
        FUN = 7, 'FUN'
        CLO = 8, 'CLOTHES'
        CHA = 9, 'CHARITY'

    class RInterval(models.IntegerChoices):
        NA = 1, 'N/A'
        DAY = 2, 'DAYS'
        WEK = 3, 'WEEKS'
        MON = 4, 'MONTHS'
        YEA = 5, 'YEARS'

    value = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    type = models.PositiveIntegerField(choices=ETypes.choices)
    repetitive = models.BooleanField(default=False)
    repetition_interval = models.PositiveSmallIntegerField(choices=RInterval.choices, default=1)
    repetition_time = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Expense {self.id} - {self.type} - {self.date.strftime("%D/%m/&y")}'

    class Meta:
        verbose_name_plural = 'Expenses'


class Balance(models.Model):
    class BType(models.IntegerChoices):
        CUR = 1, 'CURRENT'
        SAV = 2, 'SAVINGS'

    value = models.DecimalField(max_digits=10, decimal_places=2)
    type = models.PositiveIntegerField(choices=BType.choices)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Balance {self.id} - {self.type}'

    class Meta:
        verbose_name_plural = 'Balances'
