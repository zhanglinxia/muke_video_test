# coding:utf-8
from django.urls import path
from app.dashboard.views.index import IndexView
from app.dashboard.views.auth import LoginView,LogoutView
from app.dashboard.views.video import VideoView,VideoSubView,VideoStarView,VideoUpdateView
from app.dashboard.views.admin_manager import AdminManagerView,UpdateAdminManagerStatus
urlpatterns = [
    path('',IndexView.as_view(),name='dashboard_index'),
    path('login',LoginView.as_view(),name="login"),
    path('login-out',LogoutView.as_view(),name="logout"),
    path('admin-manager',AdminManagerView.as_view(),name='admin_manager'),
    path('admin-manager/update-status',UpdateAdminManagerStatus.as_view(),name='update_admin_manager_status'),
    path('video',VideoView.as_view(),name='dashboard_video'),
    path('video/<int:video_id>/sub',VideoSubView.as_view(),name='dashboard_video_sub'),
    path('video/star',VideoStarView.as_view(),name='dashboard_video_star'),
    path('video/<int:video_id>/update',VideoUpdateView.as_view(),name='dashboard_video_update')
]