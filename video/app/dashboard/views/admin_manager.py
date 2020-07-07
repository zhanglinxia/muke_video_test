# coding:utf-8
from django.contrib.auth.models import User
from django.views.generic import View
from django.shortcuts import render,redirect,reverse
from app.dashboard.libs.base_render import render_to_response
from django.core.paginator import Paginator
from app.dashboard.utils.permissions import login_authenticate
class AdminManagerView(View):
    TEMPLATE = 'dashboard/admin_manager.html'
    per_num = 2
    @login_authenticate
    def get(self,request):
        print(request.path)
        data = {}
        users = User.objects.all()
        curr_page = request.GET.get('page',1)
        curr_page = int(curr_page)
        paginator = Paginator(users,self.per_num)
        curr_users = paginator.get_page(curr_page).object_list
        data['users'] = curr_users
        data['total'] = paginator.num_pages
        data['page'] = curr_page
        return render_to_response(request,self.TEMPLATE,data)

class UpdateAdminManagerStatus(View):
    TEMPLATE = 'dashboard/admin_manager.html'
    @login_authenticate
    def get(self,request):
        status = request.GET.get('status','off')
        id = request.GET.get('id', None)
        _status = True if status == 'on' else False
        print(request)
        user = User.objects.get(id=id)
        user.is_superuser = _status
        user.save()
        return redirect(reverse('admin_manager'))