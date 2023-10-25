from django.http import HttpResponse
from django.template import loader

def biowahyu(request):
  template = loader.get_template('home.html')
  return HttpResponse(template.render())

def tentang(request):
  template = loader.get_template('tentang.html')
  return HttpResponse(template.render())