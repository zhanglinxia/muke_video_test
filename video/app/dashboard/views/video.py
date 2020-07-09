from django.shortcuts import redirect,reverse
from app.dashboard.libs.base_render import render_to_response
from django.views.generic import View
from app.model.video import (Video,VideoSub,VideoStar,
                             RoleType,VideoType,FromType,NationalityType)
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
        params = request.POST
        name = params.get('name')
        image = params.get('image')
        from_to = params.get('from_to')
        nationality = params.get('nationality')
        video_type = params.get('video_type')
        info = params.get('info')
        print('info',info)
        video_id = params.get('video_id')
        if not all([name,image,'sss',nationality,video_type]):
            url = '{}?error={}'.format(reverse('dashboard_video'),'缺少必要字段')
            return redirect(url)
        from_to_obj = check_and_get_enum(FromType, from_to)
        if not from_to_obj:
            url = '{}?error={}'.format(reverse('dashboard_video'), '视频来源字段非法')
            return redirect(url)
        try:
            if video_id:
              video = Video.objects.get(pk=video_id)
            else:
                video = Video()
            video.name = name
            video.image = image
            video.video_type = video_type
            video.from_to = from_to
            video.nationality = nationality
            video.info = info
            video.save()
        except Exception as e:
            print(e)
        return redirect(reverse('dashboard_video'))

class VideoSubView(View):
    TEMPLATE = 'dashboard/video_sub.html'
    def get(self,request,video_id):
        video = Video.objects.get(pk=video_id)
        data= {}
        data['video'] = video
        return render_to_response(request,self.TEMPLATE,data)
    """
    获取video的信息
    添加
    """
    def post(self,request,video_id):
        url = request.POST.get('url')
        number = request.POST.get('number')
        print(url,number.split())
        if not all([url,number]):
            return redirect(reverse('dashboard_video_sub',kwargs={'video_id':video_id}))
        if int(number) <= 0 :
            return redirect(reverse('dashboard_video_sub',kwargs={'video_id':video_id}))
        try:
            video = Video.objects.get(pk=video_id)
            video_sub = VideoSub()
            video_sub.video = video
            video_sub.url = url.split()
            video_sub.number = number.split()
            video_sub.save()
        except Exception as e:
            print(e)
        return redirect(reverse('dashboard_video_sub',kwargs={'video_id':video_id}))


class VideoStarView(View):
    def post(self,request):
        starName = request.POST.get('starName')
        role = request.POST.get('role')
        video_id = request.POST.get('video_id')
        print(video_id, starName, role)
        if not all([starName,role,video_id]):
            return redirect(reverse('dashboard_video_sub',kwargs={'video_id':video_id}))
        print(video_id, starName, role)
        role_type = check_and_get_enum(RoleType,role)
        if not role_type:
            return redirect(reverse('dashboard_video_sub',kwargs={'video_id':video_id}))
        try:
            video = Video.objects.get(pk=video_id)
            video_star = VideoStar()
            video_star.video = video
            video_star.name = starName
            video_star.role = role
            video_star.save()
        except Exception as e:
            print(e)
            return redirect(reverse('dashboard_video_sub', kwargs={'video_id': video_id}))
        return redirect(reverse('dashboard_video_sub',kwargs={'video_id':video_id}))

class VideoUpdateView(View):
        TEMPLATE = 'dashboard/video_update.html'
        def get(self,request,video_id):
            data = {}
            video = Video.objects.get(pk=video_id)
            data['video'] = video
            return render_to_response(request,self.TEMPLATE,data)
