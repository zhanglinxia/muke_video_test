from django import forms
from django.forms import ValidationError
from django.contrib.auth import login,authenticate
from django.contrib.auth.models import User

class AuthForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True)

    def clean(self):
        username = self.cleaned_data.get('username')
        if not username:
            raise ValidationError("用户名不能为空")
        password = self.cleaned_data.get('password')
        if not password:
            raise ValidationError("密码不能为空")
        exists = User.objects.filter(username=username).exists()
        if not exists:
            raise ValidationError("用户不存在")
        user = authenticate(username=username,password=password)
        if not user:
            raise ValidationError("密码不正确")
        self.cleaned_data['user'] = user
        return self.cleaned_data