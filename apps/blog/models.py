from django.db import models


class Post(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    content = models.TextField(verbose_name='Контент')
    image = models.ImageField(verbose_name='Малюнок', upload_to='post_images/')
    is_published = models.BooleanField(verbose_name='Опубліковано', default=False)
    likes = models.IntegerField(verbose_name='Вподобайки', default=0)
    dislikes = models.IntegerField(verbose_name='Дизлайки', default=0)
    views = models.IntegerField(verbose_name='Перегляди', default=0)
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)

    def __str__(self):
        return f'{self.title} - {self.created_at} - {self.is_published}'

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Пости'

        ordering = ['-created_at']


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='Пост', related_name='comments')
    author = models.CharField(verbose_name='Автор', max_length=50)
    content = models.TextField(verbose_name='Контент')
    created_at = models.DateTimeField(verbose_name='Дата створення', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Дата оновлення', auto_now=True)

    def __str__(self):
        return f'{self.author} - {self.created_at}'

    class Meta:
        verbose_name = 'Коментар'
        verbose_name_plural = 'Коментарі'
        ordering = ['created_at']
