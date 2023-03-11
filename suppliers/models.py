from django.db import models


class Contact(models.Model):
    email = models.EmailField(max_length=100, verbose_name="Почта")
    contry = models.CharField(max_length=250, default='Russia', verbose_name="Страна")
    city = models.CharField(max_length=200, default='Moscow', verbose_name="Город")
    street = models.CharField(max_length=200, null=True, verbose_name="Улица")
    house = models.IntegerField(null=True, verbose_name="Дом")

    class Meta:
        verbose_name = 'Контакт'
        verbose_name_plural = 'Контакты'

    def __str__(self):
        return self.email


class Product(models.Model):
    product_name = models.CharField(max_length=200, verbose_name="Наименование Продукта")
    model_product = models.CharField(max_length=200, null=True, verbose_name="Модель")
    date_start_sale = models.DateField(null=True, verbose_name="Дата старта продаж")

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.product_name


class BaseNetwork(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название")
    contact = models.ForeignKey(Contact, on_delete=models.PROTECT, verbose_name="Контакт")
    product = models.ManyToManyField(Product, verbose_name="Продукт")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Suppliers(BaseNetwork):
    class Meta:
        verbose_name = 'Завод'
        verbose_name_plural = 'Заводы'


class RetailNetwork(BaseNetwork):
    provider = models.ForeignKey(Suppliers, on_delete=models.PROTECT, verbose_name="Поставщик")
    debt = models.DecimalField(decimal_places=2, max_digits=6, default=0.00, verbose_name="Задолженность")

    class Meta:
        verbose_name = 'Розничная сеть'
        verbose_name_plural = 'Розничные сети'


class IndividualEntrepreneur(BaseNetwork):
    provider = models.ForeignKey(RetailNetwork, on_delete=models.PROTECT, verbose_name="Поставщик")
    debt = models.DecimalField(decimal_places=2, max_digits=6, default=0.00, verbose_name="Задолженность")

    class Meta:
        verbose_name = 'Индивидульный пердприниматель'
        verbose_name_plural = 'Индивидульные предприниматели'
