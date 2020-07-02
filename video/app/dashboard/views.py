from django.views.generic import View
from django.shortcuts import render
from app.dashboard.libs.base_render import render_to_response
class BaseView(View):
    TEMPLATE = 'base.html'
    def get(self,request):
        return render_to_response(self.TEMPLATE)
