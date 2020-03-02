from datetime import datetime

from django.db import models

# Create your models here.
# 定义数据库模型
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name='类别名称')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Category'
        verbose_name = '类别'
        verbose_name_plural = '类别'


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='标签')

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Tag'
        verbose_name = '标签'
        verbose_name_plural = '标签'


class Post(models.Model):
    title = models.CharField(max_length=20, verbose_name='博客标题')
    body = models.TextField(verbose_name='博客正文')
    created_time = models.DateTimeField(default=datetime.now(), verbose_name='博客创建时间')
    modified_time = models.DateTimeField(default=datetime.now(), verbose_name='博客修改时间')
    # blank = True 表示可以为空
    expert = models.CharField(max_length=50, blank=True, verbose_name='摘要')
    views = models.PositiveIntegerField(default=0, verbose_name='阅读量')
    # 类别和博客是一对多关系，一个类别可以多篇文章，一个文章属于一个类别
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING, verbose_name='所属类别')
    # 博客和标签是多对多关系
    tags = models.ManyToManyField('Tag', blank=True, verbose_name='所属标签')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def increase_views(self):
        self.views += 1

        self.save(update_fields=['views'])

    class Meta:
        db_table = 'Post'
        verbose_name = '博客信息'
        verbose_name_plural = '博客信息'
