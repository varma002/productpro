from django.shortcuts import render
from .forms import ProductForm,UpdateForm,DeleteForm
from .models import ProductData
import datetime as dt
from django.http.response import HttpResponse
mdate=dt.datetime.now()
edate=mdate+dt.timedelta(days=365)

def home(request):
    return render(request,"productfile.html")
def insert(request):
    if request.method=='POST':
        form=ProductForm(request.POST)
        if form.is_valid():
            pid=request.POST.get('pid','')
            pname=request.POST.get('pname','')
            pcost=request.POST.get('pcost','')
            pcolor=request.POST.get('pcolor','')
            quantity=request.POST.get('quantity','')
            pclass=request.POST.get('pclass','')

            pdata=ProductData(
                pid=pid,
                pname=pname,
                pcost=pcost,
                pcolor=pcolor,
                quantity=quantity,
                pclass=pclass,
                pmdate=mdate,
                pedate=edate)
            pdata.save()
            form=ProductForm()
            return render(request,"Insertfile.html", {'form': form})


    else:
        form=ProductForm()
        return render(request,"Insertfile.html",{'form':form})


def display(request):
    data=ProductData.objects.all()
    return render(request,"displayfile.html",{'data':data})

def update(request):
    if request.method=='POST':
        uform=UpdateForm(request.POST)
        if uform.is_valid():
            pid1=request.POST.get('pid','')
            pcost1=request.POST.get('pcost','')

            productid=ProductData.objects.filter(pid=pid1)

            if not productid:
                data="<h1>Priduct is invalid</h1>" \
                     "<a href='./'>goto home</a>"
                return HttpResponse(data)
            else:
                productid.update(pcost=pcost1)
                return HttpResponse('Product cost is Update')
    else:
        uform=UpdateForm()
        return render(request,"productupdatefile.html",{'uform':uform})


def delete(request):
    if request.method=='POST':
        dform=DeleteForm(request.POST)
        if dform.is_valid():
            pid1=request.POST.get('pid','')
            productid=ProductData.objects.filter(pid=pid1)

            if not productid:
                return HttpResponse("product Not Available")
            else:
                productid.delete()
                return HttpResponse("product delete successfully")
    else:
       dform=DeleteForm()
       return render(request,"deletefile.html",{'dform':dform})