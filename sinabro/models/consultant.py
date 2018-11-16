import uuid
from django.db import models
from sinabro.models.user import User


"""
    ID는 UUID 작업함.
    실제 실무에서는 server to server api 통신이 잦기 때문에 integer 형태의 id는 겹칠 위혐이 있음.
    때문에 Id가 중복 될 위험이 적은 uuid를 사용하는게 일반적임.
"""


class Consultant(models.Model):
    class Meta:
        verbose_name = '상담사'
        verbose_name_plural = verbose_name

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(
        max_length=20,
        verbose_name='이름',
        blank=True
    )
    description = models.CharField(
        max_length=100,
        verbose_name='설명',
        blank=True
    )
    education = models.TextField(
        verbose_name='학력',
        blank=True
    )
    experience = models.TextField(
        verbose_name='경력',
        blank=True
    )
    price = models.PositiveIntegerField(
        default=0,
        verbose_name='가격'
    )

    profile_image = models.ImageField(
        null=True
    )

    def __str__(self):
        return self.name


class ConsultationRequest(models.Model):
    class Meta:
        verbose_name = '상담 신청'
        verbose_name_plural = verbose_name

    RegionChoices = (
        ('Ganam', '강남 본점'),
        ('Busan', '부산 센터'),
        ('Ulsan', '울산 센터'),
        ('Changwon', '창원 센터'),
        ('Gangdong', '강동 센터'),
    )

    StatusChoices = (
        ('요청 완료', '요청 완료'),
        ('결제 완료', '결제 완료 '),
        ('상담 취소', '상담 취소'),
        ('상담 완료', '상담 완료'),
    )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    consultant = models.ForeignKey(
        'Consultant',
        related_name='requests',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='requests',
        on_delete=models.CASCADE
    )
    region = models.CharField(
        verbose_name='지역',
        choices=RegionChoices,
        max_length=100,
        default='Ganam'
    )
    name = models.CharField(
        verbose_name='이름',
        max_length=10,
        blank=True
    )
    phone_number = models.CharField(
        verbose_name='전화번호',
        max_length=11,
        blank=True
    )
    status = models.CharField(
        verbose_name='상태',
        max_length=20,
        choices=StatusChoices,
        default='요청 완료'
    )
    note = models.TextField(
        verbose_name='상담 신청 사유',
        blank=True
    )
    reservation_time = models.DateTimeField(
        verbose_name='예약 날짜'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='예약 신청 일자'
    )
    deleted_at = models.DateTimeField(
        verbose_name='예약 취소 일자',
        null=True,
        blank=True
    )


class PaymentLog(models.Model):
    class Meta:
        verbose_name = '결제 내역'
        verbose_name_plural = verbose_name

    StatusChoices = (
            ('D', '결제 완료'),
            ('C', '결제 취소'),
        )

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    request = models.ForeignKey(
        'ConsultationRequest',
        related_name='payment_logs',
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        related_name='payment_logs',
        on_delete=models.CASCADE
    )
    price = models.PositiveIntegerField(
        verbose_name='가격',
        default=0
    )

    status = models.CharField(
        verbose_name='결제 상태',
        max_length=2,
        choices=StatusChoices,
        default='D'
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='결제 내역 생성일자'
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='결제 취소 일자'
    )

    
