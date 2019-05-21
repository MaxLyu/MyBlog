from django.db import models
from django.utils import timezone


# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=200)                # 标题
    slug = models.CharField(max_length=200)                 # 文章的网站
    content = models.TextField()                            # 文章的内容
    pub_date = models.DateTimeField(default=timezone.now)   # 发布的时间
    author = models.CharField(max_length=100)               # 作者

    class Meta:
        # 设置文章显示的顺序是以 pub_date 为依据
        ordering = ('-pub_date',)

    # 以文章标题作为显示的内容
    def __unicode__(self):
        return self.title
