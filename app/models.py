# coding: utf-8
from django.db import models
from django.contrib import auth


class Category(models.Model):
    """
    Category Model
    """
    slug = models.SlugField(unique=True, blank=False, verbose_name='Slug')
    parent = models.ForeignKey('Category', related_name='child', verbose_name='Üst Kategori')
    name = models.CharField(max_length=100, blank=False, verbose_name='Kategori')

    class Meta:
        verbose_name = 'Kategori'
        verbose_name_plural = 'Kategoriler'

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    Model for Blog and Page Posts
    """
    slug = models.SlugField(unique=True, blank=False, verbose_name='Slug')
    title = models.CharField(max_length=255, blank=False, verbose_name='Başlık')
    author = models.ForeignKey('auth.User', related_name='author', blank=False, verbose_name='Yazar')
    thumbnail = models.ImageField(verbose_name='Resim')
    content = models.TextField(verbose_name='İçerik')
    category = models.ForeignKey('Category', related_name='category', blank=False, verbose_name='Kategori')
    tags = models.CharField(max_length=255, verbose_name='Etiket(ler)')
    is_page = models.BooleanField(default=False, verbose_name='Bu bir sayfa mı?')
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'İçerik'
        verbose_name_plural = 'İçerikler'

    def __str__(self):
        return self.title
