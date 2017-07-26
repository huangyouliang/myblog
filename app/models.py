# -*-encoding:utf-8-*-
from django.db import models
from  django.contrib.auth.models import AbstractUser
# Create your models here.
#用户
#1、采用集成方式扩展用户信息
#2、关联的方式
#继承admin 中的AbstractUser（用户，分组，权限）
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m',default='avatar/default.png',max_length=200,blank=True,null=True,verbose_name='用户图形' )
    qq = models.CharField(max_length=20,blank=True,null=True,verbose_name='QQ')
    mobile = models.CharField(max_length=11,blank=True,null=True,unique=True,verbose_name='电话')

    class Meta:
        verbose_name = '用户信息'    # 页面显示总的
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return self.username
#tag（标签）
class Tag(models.Model):
    name = models.CharField(verbose_name="标签名字",max_length=50)

    class Meta:
        verbose_name='标签'
        verbose_name_plural = verbose_name
    def __unicode__(self):
        # return str(self.id)
        return self.name

#分类
class Category(models.Model):
    name = models.CharField(max_length=30,verbose_name='分类名称')
    index = models.IntegerField(default=999,verbose_name='分类的排序')

    class Meta:
        verbose_name='分类'   #在admin中能看见
        verbose_name_plural=verbose_name

    def __unicode__(self):
        return self.name

# 自定义文章管理器
# 1、新加一种数据处理方法
# 2、改变原有的queryset
class ArticleManager(models.Manager):
    def distinct_date(self):
        distinct_date_list = []
        date_list = self.values('date_publish')
        for date in date_list:
            date = date['date_publish'].strftime('%Y%m')
            if date not in distinct_date_list:
                distinct_date_list.append(date)
        return distinct_date_list

#文章
class Article(models.Model):
    title = models.CharField(max_length=50,verbose_name='文章标题')
    desc = models.CharField(max_length=50,verbose_name='文章描述')
    context = models.TextField(max_length=300,verbose_name='文章内容')
    click_count = models.IntegerField(default=0,verbose_name='点击次数')
    is_recommend = models.BooleanField(default=False,verbose_name='是否推荐')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发表日期')
    user = models.ForeignKey(User,verbose_name='用户')
    category = models.ForeignKey(Category,blank=True,null=True,verbose_name='文章分类' )
    tag = models.ManyToManyField(Tag,verbose_name='标签')
#定义
    objects = ArticleManager()
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = verbose_name
        ordering = ['-date_publish']
    def __unicode__(self):
        return self.title



#评论模型
class Comment(models.Model):
    content = models.TextField(verbose_name='评论内容')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    user = models.ForeignKey(User,null=True,blank=True,verbose_name='用户')
    article = models.ForeignKey(Article,blank=True,null=True,verbose_name='文章')
    pid = models.ForeignKey('self',blank=True,null=True,verbose_name='父级评论')
    username = models.CharField(max_length=30,blank=True,null=True,verbose_name='姓名')
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='评论时间')
    class Meta:
        verbose_name = '评论'
        verbose_name_plural = verbose_name
        ordering= ['-date_publish']
    def __unicode__(self):
        return str(self.id)  #类型转化
        # return self.article
        # return ('article:%s'%(self.article))
        # dreturn('article:%s,:%s,专业:%s' % (self.article.学校, self.学院, self.专业))
#友情链接
class Links(models.Model):
    title = models.CharField(max_length=50,verbose_name='标题')
    description = models.CharField(max_length=200,verbose_name='友情链接描述')
    callback_url = models.URLField(verbose_name='url地址')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    index = models.IntegerField(default=999,verbose_name='排序顺序（从小到大）')

    class Meta:
        verbose_name = '友情链接'
        verbose_name_plural = verbose_name

    def __unicode__(self):
        return  self.title

#广告
class ad(models.Model):
    title = models.CharField(max_length=50,verbose_name='广告标题')
    description = models.CharField(max_length=200,verbose_name='广告描述')
    image_url = models.ImageField(upload_to= 'ad/%Y/%m' ,verbose_name='图片路径')
    callback_url = models.URLField(null=True,blank=True,verbose_name='回滚url')
    date_publish = models.DateTimeField(auto_now_add=True,verbose_name='发布时间')
    index = models.IntegerField(default=999,verbose_name='排序顺序（从小到大）')

    class Meta:
        verbose_name = '广告'
        verbose_name_plural = verbose_name
        ordering = ['index','id']

    def __unicode__(self):
        return self.title