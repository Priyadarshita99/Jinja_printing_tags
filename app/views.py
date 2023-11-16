from django.shortcuts import render

# Create your views here.
def data_render(request):
    data='This data is our assumption'

    #d={'assumption':data}
    d={'name':'Priya','age':2}

    #return render(request,'data_render.html',context=d)
    return render(request,'login.html',context=d)