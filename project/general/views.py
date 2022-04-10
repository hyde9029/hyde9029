
from django.http import HttpResponse

# Create your views here.


def aaa(request):
    return HttpResponse(request,'index.html')