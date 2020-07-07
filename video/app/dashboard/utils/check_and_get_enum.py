# coding:utf-8
from app.model.video import VideoType,FromType,NationalityType

def check_and_get_enum(ins,value):
    try:
        obj = ins[value]
    except:
        obj = None

    return obj
