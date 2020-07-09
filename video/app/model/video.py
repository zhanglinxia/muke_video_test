# coding:utf-8
from django.db import models
from enum import Enum

class VideoType(Enum):
    movie = 'movie'
    comic = 'comic'
    variety = 'variety'
    episode = 'episode'
    documentary = 'documentary'
    other = 'other'
VideoType.movie.label = '电影'
VideoType.documentary.label = '纪录片'
VideoType.comic.label = '动漫'
VideoType.variety.label = '综艺'
VideoType.episode.label = '剧集'
VideoType.other.label = '其他'

class NationalityType(Enum):
    china = 'china'
    america = 'america'
    japan = 'japan'
    other = 'other'

NationalityType.china.label = '中国'
NationalityType.america.label = '美国'
NationalityType.japan.label = '日本'
NationalityType.other.label = '其他'

class FromType(Enum):
    youku = 'youku'
    tencent = 'tencent'
    customr = 'customer'

FromType.youku.label = '优酷'
FromType.tencent.label = '腾讯'
FromType.customr.label = '站内'

class RoleType(Enum):
    leading = 'leading'
    supporting = 'supporting'
    actor = 'actor'
RoleType.leading.label = '主角'
RoleType.supporting.label = '配角'
RoleType.actor.label = '导演'


class Video(models.Model):
    name = models.CharField(max_length=50)
    image = models.CharField(max_length=300)
    video_type = models.CharField(max_length=20,default=VideoType.other.value)
    nationality = models.CharField(max_length=20,default=NationalityType.china.value)
    from_to = models.CharField(max_length=20,default=FromType.customr.value)
    info = models.TextField()
    status = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''.format(self.name)

    class Meta:
        unique_together = [('name','video_type','nationality','from_to')]

class VideoStar(models.Model):
    video = models.ForeignKey(
        Video,
        related_name='video_stars',
        null = True,
        on_delete=models.SET_NULL,blank=True
    )
    role = models.CharField(max_length=20,default='')
    name = models.CharField(max_length=100)
    identify = models.CharField(max_length=50,default='')

    class Meta:
        unique_together = [('video','name')]

class VideoSub(models.Model):
    video = models.ForeignKey(
        Video,
        related_name='vedeo_subs',
        on_delete=models.SET_NULL,
        null=True,blank=True
    )
    number = models.IntegerField(default=1)
    url = models.CharField(max_length=300)
    class Meta:
        unique_together=[('video','number')]

    def __str__(self):
        return 'video:{} number:{}'.format(self.video.name,self.number)
