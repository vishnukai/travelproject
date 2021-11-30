from django.http import HttpResponse
from django.shortcuts import render
from .models import Place,Placeto


# Create your views here.
def demo(request):
    obj = Place.objects.all()
    objt = Placeto.objects.all()


    return render(request, 'index.html', {'result': obj, 'resulted':objt}  )

# def about(request):
#     name='india'req
#     return render(request,'result.html',{'obj':name})
#
# def addition(request):
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     res= x+y
#     return render(request,'result.html',{'result':res})
