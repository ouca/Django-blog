from django.db import models
from markdownx.models import MarkdownxField
from markdownx.utils import markdownify
from django.utils import timezone
import datetime
import os

# Create your models here.
class BigCategory(models.Model):
    name = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    def get_latest_post(self):
        result = Post.objects.filter(
            category__parent=self).filter(
            is_publick=True).order_by('-created_at')[:5]
        return result

class SmallCategory(models.Model):
    """ 小カテゴリー """
    name = models.CharField(max_length=255)
    parent = models.ForeignKey(BigCategory, on_delete=models.PROTECT, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    def get_latest_post(self):
        result = Post.objects.filter(
            category=self).filter(
            is_publick=True).order_by('-created_at')[:5]
        return result
    
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE, related_name="著者")
    title = models.CharField(max_length=50, verbose_name="タイトル")
    text = MarkdownxField(help_text='Markdown形式で書いてください。',verbose_name="本文")
    card_text = models.TextField(verbose_name='記事説明文',default="")
    bigCategory = models.ForeignKey(BigCategory, on_delete=models.PROTECT,  null=True, blank=True, related_name= "大カテゴリ")
    category = models.ForeignKey(SmallCategory, on_delete=models.PROTECT,  null=True, blank=True, related_name= "小カテゴリ")
    is_public = models.BooleanField(default=True, verbose_name='公開可能か')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="作成日時")
    updated_date = models.DateTimeField(auto_now=True,verbose_name="更新日時")
    published_date = models.DateField(blank=True,null=True, verbose_name="公開日時")

    class Meta:
        ordering = ['-created_date']

    def __str__(self):
        return self.title

    def text_to_markdown(self):
        return markdownify(self.text)

    def text_card_markdown(self):
        return markdownify(self.card_text)
