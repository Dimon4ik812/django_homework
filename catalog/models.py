from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название', unique=True)
    description = models.TextField()


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'
        ordering = ['name']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Название')
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product') # надо разобраться должна быть связь или нет и как ее правильно настроить
    price = models.FloatField(help_text='Введите стоимость покупки')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']




