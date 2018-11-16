from django.shortcuts import render
from django.views.generic import View
from django.urls import resolve

from sinabro.models import Notice


class MainView(View):

    def get(self, request):
        current_url = resolve(request.path_info).url_name
        return render(request, 'home.html', {'current_url': current_url})


class NoticeView(View):

    def get(self, request):
        notices = Notice.objects.order_by('-created_at').all()
        return render(
            request,
            'notice.html',
            {
                'notices': notices
            }
        )


class NoticeDetailView(View):

    def get(self, request, notice_id):
        notice = Notice.objects.get(id=notice_id)
        return render(
            request,
            'notice_detail.html',
            {
                'notice': notice
            }
        )
