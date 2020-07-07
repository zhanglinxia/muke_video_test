# coding:utf-8
from django.db import models
from hashlib import md5
def hash_password(password):
    if isinstance(password,str):
        password = password.encode('utf-8')
    password = md5(password).hexdigest()
    return password


class ClientUser(models.Model):
    username = models.CharField(max_length=50,unique=True)
    password = models.CharField(max_length=200)
    avatar = models.CharField(max_length=500,null=True)
    gender = models.BooleanField(null=True, default='')
    birthday = models.DateTimeField(null=True,default='')
    status = models.BooleanField(default=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    def __str__(self):
        return ''.format(self.username)

    @classmethod
    def add(cls,username,password,avatar,gender,birthday,status):
        return cls.objects.create(
         username = username,
         password = hash_password(password),
         avatar = avatar,
         gender = gender,
         birthday = birthday
        )
    def updatestatus(self):
        status = not self.status
        self.status = status
        self.save()
        return True

    @classmethod
    def get_user(cls,username,password):
        try:
            password = hash_password(password)
            user = cls.objects.get(username=username,password=password)
            return user
        except:
            return None

