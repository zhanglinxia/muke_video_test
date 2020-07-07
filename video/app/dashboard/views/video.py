from django.shortcuts import redirect,reverse
from app.dashboard.libs.base_render import render_to_response
from django.views.generic import View
from app.model.video import Video,VideoType,FromType,NationalityType
from app.dashboard.utils.check_and_get_enum import check_and_get_enum

class VideoView(View):
    TEMPLATE = 'dashboard/video.html'
    def get(self,request):
        data = {}
        error = request.GET.get('error','')
        data['error'] = error
        videos = Video.objects.all()
        data['videos'] = videos
        return render_to_response(request,self.TEMPLATE,data)

    def post(self,request):
        data={}
        params = request.POST
        name = params.get('name')
        image = params.get('image')
        from_to = params.get('from_to')
        nationality = params.get('nationality')
        video_type = params.get('video_type')
        info = params.get('info')
        if not all([name,image,'sss',nationality,video_type]):
            url = '{}?error={}'.format(reverse('dashboard_video'),'缺少必要字段')
            return redirect(url)
        from_to_obj = check_and_get_enum(FromType, from_to)
        if not from_to_obj:
            url = '{}?error={}'.format(reverse('dashboard_video'), '视频来源字段非法')
            return redirect(url)
        Video.objects.create(
            name = name,
            image = image,
            video_type = video_type,
            from_to = from_to,
            nationality = nationality,
            info = info
        )
        return redirect(reverse('dashboard_video'))

class VideoSubView(View):
    TEMPLATE = 'dashboard/video_sub.html'
    def get(self,request):
        return render_to_response(request,self.TEMPLATE)
