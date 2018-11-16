import math

from django.views.generic import View
from django.shortcuts import render, redirect

from sinabro.views.base import LoginRequiredView
from sinabro.models import Consultant, ConsultationRequest
from sinabro.forms.consultant import ConsultationRequestForm


class ConsultantListView(View):
    """
        상담사 리스팅
        Web에서 pagination을 위해 page number을 Url 파라미터로 받음. 디폴트는 1
    """

    def get(self, request, page=1):
        consultants = Consultant.objects.all()

        size = 9  # page size는 시안을 따라 9개로 설정
        pages = [i+1 for i in range(int(math.ceil(consultants.count()/size)))]

        return render(
            request,
            'consultant/consultant_list.html',
            {
                'consultants': consultants[(page-1)*size:page*size],
                'pages': pages,
                'current_page': page,
            }
        )


class ConsultantDetailView(View):

    def get(self, request, consultant_id):
        return render(
            request,
            'consultant/consultant_detail.html',
            {
                'consultant': Consultant.objects.get(id=consultant_id)
            }
        )


class ConsultationRequestRegisterView(LoginRequiredView):
    def get(self, request, consultant_id):
        """
            get method일 때, Form을 리턴함.
        """
        form = ConsultationRequestForm()

        return render(
            request,
            'consultation/consultation_register.html',
            {
                'form': form,
                'consultant': Consultant.objects.get(id=consultant_id)
            }
        )

    def post(self, request, consultant_id):
        """
            상담 요청 생성
        """
        form = ConsultationRequestForm(request.POST)
        consultant = Consultant.objects.get(id=consultant_id)

        if form.is_valid():
            form.save(commit=False)
            form.instance.consultant = consultant
            form.instance.user = request.user
            form.save()

        return redirect('consultations', page=1)


class ConsultationRequestListView(LoginRequiredView):
    def get(self, request, page=1):
        requests = ConsultationRequest.objects.filter(
            user=request.user
        ).order_by(
            '-created_at'
        ).all()

        size = 20
        pages = [i+1 for i in range(int(math.ceil(requests.count()/size)))]

        return render(
            request,
            'consultation/consultation_request_list.html',
            {
                'consultation_requests': requests,
                'pages': pages,
                'current_page': page
            }
        )


class ConsultationRequestDetailView(LoginRequiredView):
    def get(self, request, request_id):

        consultation = ConsultationRequest.objects.get(id=request_id)
        form = ConsultationRequestForm(instance=consultation)
        return render(
            request,
            'consultation/consultation_request_detail.html',
            {
                'form': form
            }
        )

    def post(self, request, request_id):

        consultation = ConsultationRequest.objects.get(id=request_id)
        form = ConsultationRequestForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()

        return redirect('consultation', request_id=consultation.id)


class ConsultationRequestDeleteView(LoginRequiredView):

    def post(self, request, request_id):

        ConsultationRequest.objects.get(id=request_id).delete()
        return redirect('consultations', page=1)
