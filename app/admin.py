# -*-coding:utf-8 -*-
from django.contrib import admin
from app.models import *
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
    # fields = ('title','context',)
    # fieldsets = ((None,{'fields': ( 'title', 'context', 'desc')}),
    #              ( '高级设置', {'classes': ('collapse',), 'fields': ('click_count', 'is_recommend'), }),
    #              )
    list_display = ('title','context','click_count',)
    list_display_links = ('title', 'context')
    list_editable = ('click_count',)
    class Media:
        js = (
            '/static/kindeditor-4.1.10/kindeditor-min.js',
            '/static/kindeditor-4.1.10/lang/zh_CN.js',
            '/static/kindeditor-4.1.10/config.js',
        )
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name','index',)

class TatAdmin(admin.ModelAdmin):
    list_display = ('name',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('username','avatar','mobile')
class CommentAdmin(admin.ModelAdmin):
    list_display = ('article_id','content')
    # raw_id_fields = ("article",)
admin.site.register(User,UserAdmin)
admin.site.register(ad)
admin.site.register(Article,ArticleAdmin)
admin.site.register(Tag,TatAdmin)
admin.site.register(Comment,CommentAdmin)
admin.site.register(Links)
admin.site.register(Category,CategoryAdmin)