from django.urls import path

from sinabro.views import *


urlpatterns = [
    
    path('', MainView.as_view(), name='main'),
   
    
    path('notices/', NoticeView.as_view(), name='notice'),
    path('notices/<str:notice_id>/', NoticeDetailView.as_view(), name='notice_detail'),

    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(), name='logout'),
    path('accounts/register/', UserCreateView.as_view(), name='register'),
    path('accounts/duplicate/', DuplicateUsername.as_view(), name='duplicate'),
    
    path('mypage/', MypageView.as_view(), name='mypage'),    
    path('password/', ChangePassword.as_view(), name='password'),
    path('blog/search/<uuid:consultant_id>/', ConsultantDetailView.as_view(), name='consultant_detail'),
   


    path('consultants/pages/<int:page>/', ConsultantListView.as_view(), name='consultants'),
    path('consultants/<uuid:consultant_id>/', ConsultantDetailView.as_view(), name='consultant'),
    path('consultants/<uuid:consultant_id>/request/', ConsultationRequestRegisterView.as_view(), name='consulting_reservation'),

    path('users/me/consultant/requests/<int:page>/', ConsultationRequestListView.as_view(), name='consultations'),
    path('users/me/consultant/request/<uuid:request_id>/', ConsultationRequestDetailView.as_view(), name='consultation'),
    path('users/me/consultant/request/<uuid:request_id>/delete', ConsultationRequestDeleteView.as_view(), name='consultation_delete'),
    path('users/me/consultant/request/<uuid:request_id>/payment', PaymentView.as_view(), name='payment'),
    
 
]

