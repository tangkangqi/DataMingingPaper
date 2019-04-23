# encoding:utf-8
__author__ = 'shiliang'
__date__ = '2019/3/6 16:46'

from django.urls import path, include, re_path
from .views import UserInfoView, UploadImageView

app_name = 'users'

urlpatterns = [
    # 课程机构列表url
    path('info/', UserInfoView.as_view(), name='user_info'),

    # 用户头像上传
    path('image/upload/', UploadImageView.as_view(), name='image_upload'),
]