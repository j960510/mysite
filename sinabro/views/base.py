import math

from django.views.generic import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify




class ExemptCsrfView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


class LoginRequiredView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'main'


def add_paginator(posts=None, page=1, size=15, key=None):

    pages = [i+1 for i in range(int(math.ceil(posts.count()/size)))]
    content = {
        'posts': posts[(page-1)*size:page*size],
        'pages': pages[page-5:page+5] if page >= 10 else pages[:10],
        'current_page': page,
        'prv_page': (page - 1) or 1,
        'next_page': page + 1 if len(pages) > page else page
    }

    if key:
        content[key] = content['posts']

    return content

