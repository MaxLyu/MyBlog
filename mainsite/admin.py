from django.contrib import admin
from .models import Article

# Register your models here.


# 文章显示的属性
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'pub_date')


admin.site.register(Article)
