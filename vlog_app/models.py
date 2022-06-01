from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Post(models.Model):
    title = models.CharField(
        max_length=70,
        verbose_name='Заголовок'
    )
    img = models.ImageField(
        verbose_name='Изображение',
        upload_to='meida/%Y/%m/%d/',
    )
    description = models.TextField(
        max_length=255,
        verbose_name='Компинтарий к посту'
    )
    is_draft = models.BooleanField(
        verbose_name='Черновик',
        default=False
    )
    is_delite = models.BooleanField(
        verbose_name='Удален',
        default=False
    )
    create_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата создания'
        
    )
    update_date = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата последнего обновления'
    )
    user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT
    )