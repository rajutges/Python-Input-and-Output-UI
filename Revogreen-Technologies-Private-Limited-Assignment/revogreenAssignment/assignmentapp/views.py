from django.shortcuts import render
from .models import Inputdata
from django.http import HttpResponseRedirect 

# Create your views here.
def inputView(request):
    if request.method == 'POST':
            if request.POST.get('textdata') and request.POST.get('slider'):
                post=Inputdata()
                post.textdata= request.POST.get('textdata')
                post.slider= request.POST.get('slider')
                post.save()
                return render(request, 'input.html')

            else:
                return render(request, 'input.html')
    return render(request, 'input.html')




def outputView(request):
    output_data = Inputdata.objects.all()
    return render(request, 'output.html',
    {'all_items':output_data})


def deletedataView(request, i):
    y = Inputdata.objects.get(id= i)
    y.delete()
    return HttpResponseRedirect('/output/') 