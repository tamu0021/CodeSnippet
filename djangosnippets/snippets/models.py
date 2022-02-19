from tabnanny import verbose
from turtle import update
from django.db import models
from django.conf import settings

class Snippet(models.Model):
    # タイトルカラム。
    title = models.CharField('タイトル', max_length=128)
    # ソースコードを格納するカラム。
    code = models.TextField('コード', blank=True)
    # ソースコードに対する説明を格納するカラム。
    description = models.TextField('説明', blank=True)
    # スニペットの投稿者。投稿者が分かるように、ユーザモデルへの主キーを持つ。
    created_by = models.ForeignKey( settings.AUTH_USER_MODEL,
                                    verbose_name="投稿者",
                                    on_delete=models.CASCADE)
    # 投稿日カラム。
    created_at = models.DateTimeField("投稿日", auto_now_add=True)
    # 更新日カラム。
    updated_at = models.DateTimeField("更新日", auto_now=True)

    def __str__(self):
        return self.title