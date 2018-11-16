import math

from django.views.generic import View
from django.views.generic.list import ListView
from django.shortcuts import render, redirect

from sinabro.views.base import LoginRequiredView
from sinabro.models import ConsultationRequest, PaymentLog
from sinabro.forms.consultant import ConsultationRequestForm


class PaymentView(LoginRequiredView):

    def get(self, request, request_id):
        consultation = ConsultationRequest.objects.select_related(
            'consultant'
        ).get(
            id=request_id,
            user=request.user  # User가 신청한 내역만 결제 가능함.
        )

        return render(
            request,
            'payment/paytment_register.html',
            {
                'consultation': consultation
            }
        )

    def post(self, request, request_id):
        consultation = ConsultationRequest.objects.select_related(
            'consultant'  # Db query 중 inner join 을 사용하기 위함.
        ).get(
            id=request_id,
            user=request.user
        )

        # 결제로그 데이터 저장
        PaymentLog.objects.create(
            request=consultation,
            user=request.user,
            price=consultation.consultant.price, # 상담사가 설정한 가격을 넣음
        )
        # 상담 신청 상태를 결제 완료로 변경
        consultation.status = "결제 완료"
        consultation.save()

        # 상담 신청 리스트 페이지로 연결
        return redirect('consultations', page=1)
    

