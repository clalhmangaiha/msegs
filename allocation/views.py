from django.shortcuts import render,redirect

# Create your views here.
from .models import *
from itertools import chain
from .forms import AllocateForm,RequestForm,ReallocateForm
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.views import LoginView,LogoutView


def home(request):
    districts = District.objects.all()
    requests = Request.objects.all()
    s=int(0)
    return render(request, 'msegs/home.html', {'districts':districts,'requests':requests,'s':s})


def index(request):
  
    

    if request.user.is_superuser:
        items = Item.objects.all()
        form = AllocateForm()
        districts = District.objects.all()
        category = Category.objects.all()
        context= {'items':items,'districts':districts,'category':category,
    # 'unallocated':unallocated
         }
        return render(request,'msegs/index.html',{'context': context,'form':form,},)

    elif request.user.is_authenticated == False:
        return render(request,'account/anynomous.html',)
    else:
        l = 0
        p = Profile.objects.get(user=request.user)
        d = District.objects.get(manager=p)
        r = Reallocation.objects.filter(initiator=d)
        k = Reallocation.objects.filter(current=d)
        items = Item.objects.filter(district=d)
        s=True
        a = True
        for i in r:
            s = i.approved and s
            a = i.accepted and a
        print(s)
        
        if s == False and a == False:
            l =0
        else:
            l=1
        return render(request,'district/district_index.html',{'items':items,'d':d,'l':l})
  
def allocation(request):
    
    if request.method =="POST":
        origin_data = request.POST.dict()
        
        name = origin_data.get("name")
        district = origin_data.get("district")
        print(name,district)
        l = Item.objects.get(name=name)
        d = District.objects.get(district=district)

        print("ITEM NAME",l.name)
        l.district = d
        l.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def changestatus(request):
    if request.method == "POST":
        origin_data = request.POST.dict()
        
        name = origin_data.get("id")
        status = origin_data.get("status")
        print(name,status)
        l = Item.objects.get(id=name)
        

        print("ITEM NAME",l.name)
        l.status = status
        l.save()
        return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def changestates(request,id,status):
    p = Item.objects.get(id=id)
    p.status = status
    p.save()
    return HttpResponseRedirect(request.META.get("HTTP_REFERER"))

def add(request):
    if request.method == 'POST':
        form = AllocateForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
            
            form.save()
            print(f.name,"CORRECT")
            
            

        else:
            print("Form validation not correct")
        
        # form = AllocateForm(request.POST)
        
        # l.save()
        # print(request.POST.get('name'))

       
    else:
        form = AllocateForm()
    return redirect(index)

def item_info(request,id):
    item = Item.objects.get(id=id)
    item_info = ItemInfo.objects.get(item=item)
    print(item.name)
    return render(request, "msegs/item.html",{'item':item,'item_info':item_info})


def request_item(request):
    if request.method == "POST":
        form = RequestForm(request.POST)
        if form.is_valid():
            f = form.save(commit=False)
          
            p = Profile.objects.get(user=request.user.id)
            f.initiator = District.objects.get(manager=p)
            f.save()
            return render(request, 'district/submitted.html')
        else:
            print("Incorrect form")
    else:
        form = RequestForm()

    return render(request, "district/request_item.html",{'form':form})

def reallocation(request):
    items = Item.objects.filter(status=2)
    districts =District.objects.all()
    if request.method =="POST":
        form = ReallocateForm(request.POST)
       
        print(request.POST.get("item"),request.POST.get("initiator"),request.POST.get("approved"))
        if form.is_valid():
            form.save()
        else:
            print("incorrect form")
    else:
        form = ReallocateForm()

    return render(request, "msegs/reallocation.html",{'form':form,'items':items,'districts':districts})

def notification(request):
    p = Profile.objects.get(user=request.user)
    d = District.objects.get(manager=p)
    r = Reallocation.objects.filter(initiator=d)
    k = Reallocation.objects.filter(current=d)
   
    print(k)
    return render(request, "district/notification.html",{'r':r,'k':k,'d':d})

def mnotification(request):
    r = Request.objects.all()
    k = Reallocation.objects.all()
    return render(request, 'msegs/mnotification.html',{'r':r,'k':k,})

def accepted(request,id):
    r = Reallocation.objects.get(id=id)
    r.accepted =True
    r.save()
    # return redirect(notification)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def completed(request,id):
    r = Reallocation.objects.get(id=id)
    r.completed = True
    r.save()
    i = Item.objects.get(id=r.item.id)
    i.district = r.initiator
    i.status =True
    i.save()
    return redirect(notification)

def process(request,id):
    p = Profile.objects.get(user=request.user)
    d = District.objects.get(manager=p)
    
def district_index(request):
    p = Profile.objects.get(user=request.user)
    d = District.objects.get(manager=p)
    items = Item.objects.filter(district=d)
    return render(request,'district/district_index.html',{'items':items})

class Login(LoginView):
    template_name = 'account/login.html'

class Logout(LogoutView):
    template_name = 'account/logout.html'
    
    

def district_info(request,id):
    district = District.objects.get(id=id)
    profile = Profile.objects.get(user=district.manager)
    items = Item.objects.filter(district=district)
    return render(request,'msegs/district_info.html',{'district':district,'profile':profile,'items':items})


def re(request):
    l = Item.objects.filter(status=2)
    item = request.POST.get('name')
    initiator =request.POST.get('initiator')
    current =request.POST.get('current')
    print(item,initiator,current)
    d = District.objects.all()

    # return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request,'msegs/reallocation.html',{'l':l,'d':d,})