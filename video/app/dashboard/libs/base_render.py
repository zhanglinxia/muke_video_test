#mymako.py
from django.template.context import Context
from django.http import HttpResponse
from mako.template import Template
from mako.lookup import TemplateLookup
from config import settings
import os

def render_to_response(t,c=None,context_instance=None):
    path = settings.TEMPLATES[0]['DIRS']
    mylookup = TemplateLookup(directories=path,output_encoding='utf-8')
    mako_temp = mylookup.get_template(t)
    if context_instance:
        context_instance.update(c)
    else:
        context_instance = Context(c)
    data = {}
    for d in context_instance:data.update(d)
    return HttpResponse(mako_temp.render(**data))