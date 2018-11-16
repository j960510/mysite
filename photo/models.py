from django.db import models

from photo.fields import ThumbnailImageField

from sinabro.models import User


class Album(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField('One Line Description', max_length=100, blank=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )

    class Meta:
        ordering = ['name']
        
    def __str__(self):
        return self.name


class Photo(models.Model):
    album = models.ForeignKey(
        Album,
        on_delete=models.CASCADE
    )
    title = models.CharField(max_length=50)
    image = ThumbnailImageField(upload_to='photo/%Y/%m')
    description = models.TextField('Photo Description', blank=True)
    upload_date = models.DateTimeField('Upload Date', auto_now_add=True)
    owner = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True
    )
        
    class Meta:
        ordering = ['title']
        
    def __str__(self):
        return self.title
