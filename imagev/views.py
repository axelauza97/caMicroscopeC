from django.shortcuts import render
from django.http import HttpResponse, StreamingHttpResponse, HttpResponseRedirect
from django.views.generic import ListView, CreateView
from django.views.decorators import gzip
from django.urls import reverse_lazy
from .capture import Capture
# Create your views here.

@gzip.gzip_page
def images(request,spectr):
    capture_ = Capture(spectr)
    capture_.capture()
    return StreamingHttpResponse(capture_.generate(),content_type="multipart/x-mixed-replace;boundary=frame")

def index(request,reload=False):
    return render(request, 'index.html')

