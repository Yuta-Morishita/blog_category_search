from django.db import models


class Category(models.Model):
    name = models.CharField('カテゴリー', max_length=50)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField('タイトル', max_length=50)
    text = models.TextField('テキスト')
    category = models.ForeignKey(
        Category, verbose_name='カテゴリー',
        on_delete=models.PROTECT
    )
    created_at = models.DateField('作成日', auto_now_add=True)
    updated_at = models.DateField('更新日', auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'ブログ'
        verbose_name_plural = 'ブログ'
