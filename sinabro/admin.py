from django.contrib import admin

from sinabro.models import Consultant, ConsultationRequest, PaymentLog, User, Notice
from django.views.generic.list import ListView
from blog.models import Post




@admin.register(Consultant)
class ConsultantAdmin(admin.ModelAdmin):
    list_display = 'name', 'price', 


@admin.register(ConsultationRequest)
class ConsultantRequestAdmin(admin.ModelAdmin):
    list_display = 'get_username', 'get_consultant_name', 'reservation_time', 'status', 'created_at'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user', 'consultant')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = '예약 회원'

    def get_consultant_name(self, obj):
        return obj.consultant.name
    get_consultant_name.short_description = '상담사'


@admin.register(PaymentLog)
class PaymentLogAdmin(admin.ModelAdmin):
    change_list_template = 'admin/paymentlog.html'
    list_display = 'get_username', 'get_consultant_name', 'price', 'created_at'

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related('user', 'consultant')

    def get_username(self, obj):
        return obj.user.username
    get_username.short_description = '회원'

    def get_consultant_name(self, obj):
        return obj.request.consultant.name
    get_consultant_name.short_description = '상담사'

    def get_queryset(self, request):
        return super().get_queryset(request).select_related('request', 'user').order_by('-created_at')


    # 총 수입금을 계산하기위해 어드민에 데이터를 넘겨야하므로, change_view 를 override 함.
    def changelist_view(self, request, extra_context=None):
        obj = PaymentLog.objects.all()
        
        extra_context = {
            'sum': sum([row.price for row in obj]),
            'div': int((sum([row.price for row in obj]))/10),
            'pay': str(row.price for row in obj)
        }
        return super().changelist_view(request, extra_context=extra_context)
    
    

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = 'username', 'name', 'email'


@admin.register(Notice)
class NoticeAdmin(admin.ModelAdmin):
    list_display = 'title', 'get_short', 'created_at',

    def get_short(self, obj):
        return obj.text[:30]
    get_short.short_description = '내용'


    
    
