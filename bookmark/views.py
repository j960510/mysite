from django.shortcuts import render

from django.views.generic import ListView, DetailView
from bookmark.models import Bookmark

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from sinabro.views.base import LoginRequiredView

# Create your views here.

class BookmarkLV(ListView):
    model = Bookmark

class BookmarkDV(DetailView):
    model = Bookmark

class BookmarkCreateView(LoginRequiredView, CreateView):
    model = Bookmark
    fields = ['title', 'url']

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super(BookmarkCreateView, self).form_valid(form)

class BookmarkChangeLV(LoginRequiredView, ListView):
    template_name = 'bookmark/bookmark_change_list.html'

    def get_queryset(self):
        return Bookmark.objects.filter(owner=self.request.user)

class BookmarkUpdateView(LoginRequiredView, UpdateView) :
    model = Bookmark
    fields = ['title', 'url']

class BookmarkDeleteView(LoginRequiredView, DeleteView) :
    model = Bookmark

