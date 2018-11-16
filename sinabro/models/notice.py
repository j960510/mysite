import uuid
from django.db import models
from django.utils import timezone



class Notice(models.Model):
    class Meta:
        verbose_name = '공지사항'
        verbose_name_plural = verbose_name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(
        verbose_name='제목',
        max_length=30,
        blank=True
    )
    text = models.TextField(
        verbose_name='내용',
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )


    def __str__(self):
        return self.title

    
   
