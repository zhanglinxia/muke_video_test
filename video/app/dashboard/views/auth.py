# coding:utf-8
from django.views.generic import View
from django.shortcuts import render,redirect,reverse
from app.dashboard.forms.auth import AuthForm
from django.contrib.auth import login,logout
from app.dashboard.libs.base_render import render_to_response
class LoginView(View):
    TEMPLATE = 'dashboard/login.html'
    def get(self,request):
        # if request.user.is_authenticated:
        #     return redirect(reverse('dashboard_index'))
        to = request.GET.get('to')
        print(111,to)
        # x_cookie = request.META['CSRF_COOKIE']

        return render_to_response(request,self.TEMPLATE,{'to':to})

    def post(self,request):
        """
        如果校验成功，登陆
        否则抛出错误信息
        :param request:
        :return:
        """

        authForm = AuthForm(request.POST)
        # user = authForm.cleaned_data.get('user')
        if not authForm.is_valid():
            data = {}
            error = authForm.non_field_errors
            data['error'] = error
            return render(request,self.TEMPLATE,data)

        login(request,authForm.cleaned_data['user'])
        to = request.GET.get('to')
        if to:
            return redirect('/dashboard/admin-manager')
        return redirect(reverse('dashboard_index'))

class LogoutView(View):
    def get(self,request):
        logout(request)
        return redirect(reverse('login'))
