import functools
from django.shortcuts import redirect,reverse
def login_authenticate(func):
    def wrapper(self,request,*args,**kwargs):
        user = request.user
        if not user.is_authenticated or not user.is_superuser:
            _login = reverse('login')
            redirect_uri = '{}?to={}'.format(_login,request.path)
            return redirect(redirect_uri)
        return func(self,request,*args,**kwargs)

    return wrapper