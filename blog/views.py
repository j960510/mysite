from django.views.generic import ListView, DetailView, TemplateView, View
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from blog.models import Post
from sinabro.models import Consultant

from tagging.models import Tag, TaggedItem
from tagging.views import TaggedObjectList

from django.views.generic.edit import FormView
from blog.forms import PostSearchForm
from django.db.models import Q
from django.shortcuts import render

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sinabro.views.base import LoginRequiredView

import math
import uuid

from django.views.generic import View
from django.shortcuts import render, redirect




# Create your views here.

#--- TemplateView
class TagTV(TemplateView) :
    template_name = 'tagging/tagging_cloud.html'
    



    
#--- ListView
class Post0LV(ListView) :
    model = Post
    template_name = 'blog/all3.html'
    context_object_name = 'post0'
    paginate_by = 2




class SubmitView(View):

    def post(self, request):
        t = []
        for k, v in request.POST.items():
            if k == 'ta1':
                continue
            if v == '예':
                t.append(t)

        return render(
            request,
            'blog/result.html',
            {
                'result': '정상' if len(t) <= 5 else '우울증'
            }
        )
    
    
    

class Post1LV(ListView) :
    model = Post
    template_name = 'blog/all1.html'
    context_object_name = 'post1'
    paginate_by = 2
    
class Submit1View(View):

    def post(self, request):
        t = []
        for k, v in request.POST.items():
            if k == 'ta1':
                continue
            if v == '예':
                t.append(t)

        return render(
            request,
            'blog/result1.html',
            {
                'result1': '정상' if len(t) <= 5 else '조울증'
            }
        )

class Post2LV(ListView) :
    model = Post
    template_name = 'blog/all2.html'
    context_object_name = 'post2'
    paginate_by = 2

class Submit2View(View):

    def post(self, request):
        t = []
        for k, v in request.POST.items():
            if k == 'ta1':
                continue
            if v == '예':
                t.append(t)

        return render(
            request,
            'blog/result2.html',
            {
                'result2': '정상' if len(t) <= 5 else '공황장애'
            }
        )

    
    
#--- ListView
class PostLV(ListView) :
    model = Post
    template_name = 'blog/post_all.html'
    context_object_name = 'posts'
    paginate_by = 2
    
class TestPostLV(ListView) :
    #model = Post
    #queryset = Post.objects.all()[:5]
    #template_name = 'blog/post_all.html'
    template_name = 'blog/post_test.html'
    context_object_name = 'posts'
    paginate_by = 2
    
    def get_queryset(self):
        return Post.objects.filter(Q(content__icontains = self.kwargs['word'])).distinct()
    def get_context_data(self, **kwargs):
        context = super(TestPostLV, self).get_context_data(**kwargs)
        context['SearchWord'] = self.kwargs['word']
        return context
    
    

class PostTOL(TaggedObjectList) :
    model = Post
    template_name = 'tagging/tagging_post_list.html'

#--- DetailView
class PostDV(DetailView) :
    model = Post

#--- ArchiveView
class PostAV(ArchiveIndexView) :
    model = Post
    date_field = 'modify_date'

class PostYAV(YearArchiveView) :
    model = Post
    date_field = 'modify_date'
    make_object_list = True

class PostMAV(MonthArchiveView) :
    model = Post
    date_field = 'modify_date'

class PostDAV(DayArchiveView) :
    model = Post
    date_field = 'modify_date'

class PostTAV(TodayArchiveView) :
    model = Post
    date_field = 'modify_date'

#--- FormView
class SearchFormView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/post_search.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        post_list = Consultant.objects.filter(Q(name__icontains=schWord) | Q(description__icontains=schWord) | Q(experience__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
  

#--- consultant detail view

class ConsultantDetailView(View):

    def get(self, request, consultant_id):
        return render(
            request,
            'consultant_detail.html',
            {
                'consultant': Consultant.objects.get(id=consultant_id)
            }
        )

#--- 사이트소개

class IntrodutionView(FormView):
    form_class = PostSearchForm
    template_name = 'blog/introdution.html'

    def form_valid(self, form) :
        schWord = '%s' % self.request.POST['search_word']
        post_list = Post.objects.filter(Q(title__icontains=schWord) | Q(description__icontains=schWord) | Q(content__icontains=schWord)).distinct()

        context = {}
        context['form'] = form
        context['search_term'] = schWord
        context['object_list'] = post_list

        return render(self.request, self.template_name, context)
    

    
    
class PostCreateView(LoginRequiredView, CreateView):
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']
    initial = {'slug': 'auto-filling-do-not-input'}

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(PostCreateView, self).form_valid(form)

class PostChangeLV(LoginRequiredView, ListView):
    template_name = 'blog/post_change_list.html'

    def get_queryset(self):
        return Post.objects.filter(owner=self.request.user)

class PostUpdateView(LoginRequiredView, UpdateView) :
    model = Post
    fields = ['title', 'slug', 'description', 'content', 'tag']

class PostDeleteView(LoginRequiredView, DeleteView) :
    model = Post

