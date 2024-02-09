from django.db import models


class Menu(models.Model):
    name_menu = models.CharField(max_length=100, verbose_name='Наименование')
    url_menu = models.CharField(max_length=100, verbose_name='URL')
    mother_menu = models.ForeignKey("Menu", on_delete=models.CASCADE, verbose_name='Родительское меню', null=True)

    def __str__(self):
        return self.name_menu


# Create your models here.
