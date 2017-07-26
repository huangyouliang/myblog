from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,render_to_response
import logging
from django.conf import settings
from app.models import *
from django.db.models import Count
from app.models import Comment
from app.forms import *
import time
from  django.db import connection
#-*-encoding:utf-8-*-
# Create your views here.
logger = logging.getLogger(__name__)
logger.info('aaa')
logger.error('error occurs')

def home(request):
    return render(request,'index.html',locals())
def login(request):
    return render_to_response('login.html')
def apply1(request):
    return  render_to_response('apply1.html')

def global_settings(request):
    SITE_NAME = settings.SITE_NAME
    SITE_DESC = settings.SITE_DESC
    category_list = Category.objects.all()
    tag_list = Tag.objects.all()
    article_list = Article.objects.all()
    archive_list = Article.objects.distinct_date()
    #博文排行
    comment_count_list = Comment.objects.values('article').annotate(comment_count=Count('article')).order_by('-comment_count')
    article_comment_list=[Article.objects.get(pk=comment['article'])for comment in comment_count_list]
    # print(article_comment_list[0].title)
    # comment_list = Article.objects.values('comment_count_list').order_by()
    return locals()


def index(request):
    # try:
        #文章归档
        #1.先要获取文件月份
        # date_D = article_list.values('date_publish').distinct()  这个只能简单去重
        # archive_list=Article.objects.raw('SELECT DISTINCT DATE_FORMAT(date_publish,"%Y-%m") as col_date from app_article ORDER BY date_publish')
        # for archive in article_list:
        #     print (archive)
        # cursor = connection.cursor()
        # cursor.execute("SELECT DISTINCT DATE_FORMAT(date_publish,'%Y-%m') as col_date from app_article ORDER BY date_publish")
        # row = cursor.fetchall()
        # print('row:',row)
    # except Exception as e:
    #     logger.error(e)

     return render(request, 'index.html', locals())

#归档文章
def archive(request):
    year = request.GET.get('year',None)
    month = request.GET.get('month',None)
    article_list = Article.objects.filter(date_publish__icontains=year+'-'+month)
    # article_list1 = Article.objects.filter(date_publish__year=year).filter(date_publish__month=month)
    # articles     = Article.objects.filter(date_publish__icontains=year + '-' + month)
    #icontains模糊查询 i 不区分大小写
    #distinct 去重
    archive_list = Article.objects.distinct_date()
    return render(request,'archive.html',locals())

#文章详情
def detail(request):
    #找出id对应的文章信息
    article = Article.objects.get(pk=request.GET.get('id', None))
    #找出文章id 在comment 表中的信息
    article_comment = Comment.objects.filter(article=article.id).all()
    #初始化comment_form
    comment_form = CommentForm()
    # print(article.title)
    return render(request,'detail.html',locals())

#文章评论
def comment(request):
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            # return HttpResponseRedirect("/app/detail")
            return HttpResponse('创建成功！')
    else:
        comment_form = CommentForm()
    return render(request,'detail.html',locals())

