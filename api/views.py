# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Restaurant
from .models import Items
from django.shortcuts import render 
from django.views.decorators.csrf import csrf_exempt
import json

# 1 st GET
@csrf_exempt
def index(request):
    latest_added_resto=Restaurant.objects.all()
    list=[]
    for r in latest_added_resto:
        rList={
            "Name":r.Rname,
            "address":r.address
            }
        list.append(rList)
        
    return HttpResponse(json.dumps(list))


# 1st POST
@csrf_exempt
def addQ(request):
    r=Restaurant(
        Rname=request.POST.get("rName"),
        address=request.POST.get("addr")
        )   #fetch name and address of restaurant in r
    r.save()
    return HttpResponse("200 OK")


#2nd POST  
@csrf_exempt
def addItems(request, restaurant_id):
    r = Restaurant.objects.get(pk=restaurant_id)
    it=Items(
        item=request.POST.get("item"),
        price=request.POST.get("price"),
        restaurant=r
        )
    it.save()
    list=[]
    t=Items.objects.filter(restaurant=r)
    for i in t:
        Idist={
            "MenuItem":i.item,
            "Price":i.price
            }
        list.append(Idist)
    
    rList={
        "Name":r.Rname,
        "address":r.address,
        "list":list
        }
    return HttpResponse(json.dumps(rList))


#2 nd GET
@csrf_exempt
def detail(request,restaurant_id):
    r = Restaurant.objects.get(pk=restaurant_id)
    t=Items.objects.filter(restaurant=r)
    list=[]
    for i in t:
        Idist={
            "MenuItem":i.item,
            "Price":i.price
            }
        list.append(Idist)
    
    rList={
        "Name":r.Rname,
        "address":r.address,
        "list":list
        }
    return HttpResponse(json.dumps(rList))

    
    
   

        

    

    
    