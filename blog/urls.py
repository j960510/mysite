"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from blog.views import *
from . import views
import uuid

urlpatterns = [
    
     # Example: /
    url(r'^$', PostLV.as_view(), name='index'),
     # Example: /post/ (same as /)
    url(r'^post/$', PostLV.as_view(), name='post_list'),
     # Example: /post/django-example/
    url(r'^post/(?P<slug>[-\w]+)/$', PostDV.as_view(), name='post_detail'),
     # Example: /archive/
    url(r'^archive/$', PostAV.as_view(), name='post_archive'),
     # Example: /2012/
    url(r'^(?P<year>\d{4})/$', PostYAV.as_view(), name='post_year_archive'),
     # Example: /2012/nov/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/$', PostMAV.as_view(), name='post_month_archive'),
     # Example: /2012/nov/10/
    url(r'^(?P<year>\d{4})/(?P<month>[a-z]{3})/(?P<day>\d{1,2})/$', PostDAV.as_view(), name='post_day_archive'),
     # Example: /today/
    url(r'^today/$', PostTAV.as_view(), name='post_today_archive'),
     # Example: /tag/
    url(r'^tag/$', TagTV.as_view(), name='tag_cloud'),  
     # Example: /tag/tagname/
    url(r'^tag/(?P<tag>[^/]+(?u))/$', PostTOL.as_view(), name='tagged_object_list'),
     # Example: /search/
    url (r'^search/$', SearchFormView.as_view(), name='search'),
    
     # Example: /add/
    url(r'^add/$',
        PostCreateView.as_view(), name="add",
    ),
     # Example: /change/
    url(r'^change/$',
        PostChangeLV.as_view(), name="change",
    ),
     # Example: /99/update/
    url(r'^(?P<pk>[0-9]+)/update/$',
        PostUpdateView.as_view(), name="update",
    ),
     # Example: /99/delete/
    url(r'^(?P<pk>[0-9]+)/delete/$',
        PostDeleteView.as_view(), name="delete",
    ),
     # Example: /test/
    #url(r'^test/$', TestPostLV.as_view(), name='post_test'),
    # Example: /test/word/
    url(r'^test/(?P<word>[\w]+)/$', TestPostLV.as_view(), name='post_test'),
    
    
    #--- 진단
    url(r'^post0/$', Post0LV.as_view(), name='post0'),
    url(r'^result/$', SubmitView.as_view(), name='result'),
    

    url(r'^post1/$', Post1LV.as_view(), name='post1'),
    url(r'^result1/$', Submit1View.as_view(), name='result1'),
    
    url(r'^post2/$', Post2LV.as_view(), name='post2'),
    url(r'^result2/$', Submit2View.as_view(), name='result2'),

 
    #--- 사이트소개
    url (r'^introdution/$', IntrodutionView.as_view(), name='Introdution'),
]
