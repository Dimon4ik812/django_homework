from django.db import models
from django.db.models import BooleanField

from users.models import CustomsUser


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
    description = models.TextField(null=True, blank=True, verbose_name='Описание')
    image = models.ImageField(upload_to='images/', verbose_name='Картинка')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product', verbose_name='Категория') # надо разобраться должна быть связь или нет и как ее правильно настроить
    price = models.FloatField( verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    publication_status = models.BooleanField(default=False)
    owner = models.ForeignKey(CustomsUser, verbose_name='Владелец', blank=True, null=True, on_delete=models.SET_NULL)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']
        permissions = [
            ("can_unpublish_product", "can_unpublish_product"),
        ]


class StyleFormMixin:
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        for fild_name, fild in self.fields.items():
            if isinstance(fild, BooleanField):
                fild.widget.attrs['class'] = 'form-check-input'
            else:
                fild.widget.attrs['class'] = 'form-control'


