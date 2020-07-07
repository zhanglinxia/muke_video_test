from django.views.generic import View
from django.shortcuts import render
from django.contrib.auth.models import User
from app.dashboard.libs.base_render import render_to_response
class IndexView(View):
    TEMPLATE = 'dashboard/index.html'
    def get(self,request):
        return render_to_response(request,self.TEMPLATE)

