from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.core.urlresolvers import reverse
from .models import Editor
from django.views import generic
import mymodule



# Create your views here.
def index(request):

    print "*************"
    print request.method
    print "*************"

    if request.method == 'POST':
        _POST = request.POST
        # CASE 1
        if "resumableChunkNumber" in _POST:
            Resumablefile= request.FILES.get('file')
            mymodule.handler_rs_POST(_POST, Resumablefile)

        else:
            mymodule.handler_no_POST(_POST)
            return HttpResponseRedirect(reverse('upload:success'))

        return HttpResponse()


    elif request.method == 'GET':
        _GET = request.GET
        if 'resumableChunkNumber' in _GET:
            if mymodule.handler_rs_GET(_GET) == True:
                return 'ok'
            else:
                print "HTTP/1.0 404 Not Found"
                return HttpResponse('chunk not found', status=404)

    return render(request,'upload/index.html')

def success(request):
    return HttpResponse("upload success!")
