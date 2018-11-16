import datetime

from django.views.generic import View

from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate, logout

from sinabro.models import User, Notice
from sinabro.views.base import ExemptCsrfView

from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.utils.translation import ugettext as _
from django.http import HttpResponse

   

class LoginRequiredView(LoginRequiredMixin, View):
    login_url = 'login'
    redirect_field_name = 'main'


class LoginView(View):

    def get(self, request):
        return render(
            request,
            'registration/login.html',
        )

    def post(self, request):
        user = authenticate(
            request,
            username=request.POST['username'],
            password=request.POST['password']
        )
        if not user:
            return render(
                request,
                'registration/login.html',
                {
                    'errors': 'error'
                }
            )

        login(request, user)
        return redirect('main')


class LogoutView(View):

    def get(self, request):
        logout(request)
        return redirect('login')


class UserCreateView(View):
    def get(self, request):
        return render(
            request,
            'registration/signup.html',
            {
                'birth_year': [2000 + i for i in range(19)],
                'birth_month': [i for i in range(1, 13)],
                'birth_day': [i for i in range(1, 32)]
            }
        )

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if not (username and password):
            return HttpResponse('You must give username and password')

        if password != password2:
            return HttpResponse('Incorrect password')

        try:
            birthday = datetime.date(
                int(request.POST['birth_year']),
                int(request.POST['birth_month']),
                int(request.POST['birth_day'])
            )
        except ValueError:
            birthday = datetime.date(
                int(request.POST['birth_year']),
                int(request.POST['birth_month']),
                int(request.POST['birth_day']) - 1
            )

        user = User(
            username=username,
            name=request.POST.get('name'),
            birthday=birthday,
            gender=request.POST['gender'],
            email=request.POST.get('email'),
            address=f"{request.POST.get('address')} {request.POST.get('detail_address')}",
            phone_company=request.POST['phone_company'],
            phone_number=request.POST.get('phone_number'),
            interests=','.join([i for i in request.POST.getlist('interests')]),
            description=request.POST.get('description')
        )
        user.set_password(password)
        user.save()

        return render(
            request,
            'registration/register_done.html'
        )


class DuplicateUsername(ExemptCsrfView):

    def post(self, request):
        if User.objects.filter(username=request.POST.get('username')).exists():
            return HttpResponse(status=400)
        return HttpResponse(status=200)
    
    
    
class MypageView(View):
    
    def get(self, request):
        return render(request, 'registration/mypage.html')
      
    def post(self, request):
        return render(request, 'registration/mypage.html')  

 
class ChangePassword(View):
    
    def get(self, request):
        user = request.user
        password_form = PasswordChangeForm(user)

        return render(request, 'registration/change.html', {'user': user,
                                                            'password_form': password_form})

    def post(self, request):
        user = request.user
        password_form = PasswordChangeForm(user, request.POST)
        if password_form.is_valid():
            changed_user = password_form.save()
            update_session_auth_hash(request, changed_user)
            messages.success(request, "비밀번호를 성공적으로 변경하였습니다.")
            return redirect('main')
        else:
            messages.error(request, "다시 시도해주시기 바랍니다.")

        return render(request, 'registration/change.html', {'user': user,
                                                            'password_form': password_form}) 





class SearchView(View):
   
   
    def search_form(self, request):
        return render(request, 'sinabro/search_form.html')
   
    def search(self, request):
        if 'q' in request.GET:
           message = 'You searched for: %r' % request.GET['q']
        else:
           message = 'You submitted an empty form.'
        return HttpResponse(message)
