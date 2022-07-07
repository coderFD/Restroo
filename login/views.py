from logging import LogRecord
from pickle import TRUE
import re
from django.http import HttpResponse
from django.shortcuts import render,redirect
from login.models import Dishes,Menu,Order,Searchhhh,specialdish,Review,Cart,Signup,Login,Active
from login import models
from django.contrib import messages
from django.contrib.sessions.models import Session
# Create your views here.



def index(request,):
    if request.session['loged in']:
        if request.method == 'POST':
            revv = Review()
            revv.name = request.POST.get('name')
            revv.rev = request.POST.get('msg')

            revv.save()
            return redirect("/thankyou")
            
        
        sd = specialdish.objects.all()
        
        d = Dishes.objects.all()[4:7]
        m = Menu.objects.all()
        r = Review.objects.all()
       
        res = request.session['name']
         
    
        
    
        v = {"obj":sd,"objec":d,"oob":m,"oop":r,"year":2022,"active_person":res}

        return render(request,"index.html",v)
    
        
def home(request):
    if request.method == 'POST':
        revv = Review()
        revv.name = request.POST.get('name')
        revv.rev = request.POST.get('msg')

        revv.save()
        return redirect("/thankyou")
    
    
    sd = specialdish.objects.all()
    
    d = Dishes.objects.all()[8:11]
    m = Menu.objects.all()
    r = Review.objects.all()
    v = {"obj":sd,"objec":d,"oob":m,"oop":r,"year":2022}
    a = Active.objects.get(pk=1)
   
    return render(request,"home.html",v,)
   
def dishes(request):
    if request.session['loged in']:
    
        d = Dishes.objects.all()
        d = {"d":d,"year":2022}
        a = Active.objects.get(pk=1)
        
        return render(request,"dishes.html",d,)
    
def menu(request):
    if request.session['loged in']:
        m = Menu.objects.all()
        obj = {"obj":m,"year":2022}
        a = Active.objects.get(pk=1)
    
        return render(request,"menu.html",obj)
   
def order(request):
    if request.session['loged in']:
        if request.method == 'POST':
        
            o = Order()
            o.name = request.POST.get('name')
            o.mobileno = request.POST.get('number')
            o.code = request.POST.get('code')
            o.food_name = request.POST.get('foodname')
            o.extra_food = request.POST.get('extrafood')
            o.count = request.POST.get('count')
            o.address = request.POST.get('address')
            o.msg = request.POST.get('msg')
            o.save()

            return redirect("/order/payment")
        a = Active.objects.get(pk=1)

        year = {"year":2022}
        return render(request,"order.html",year)
    
    


def pay(request):
    
    return render(request, "payment.html")
def review(request):
    if request.session['loged in']:
        if request.method == 'POST':
            revv = Review()
            revv.name = request.POST.get('name')
            revv.rev = request.POST.get('msg')

            revv.save()
            return redirect("/thankyou")
        r = Review.objects.all()
        obj = {"obj":r,"year":2022}
        year = {"year":2022}
        a = Active.objects.get(pk=1)

        return render(request,"review.html",obj)

def verify(request):
    if request.session['loged in']:
        return render(request,"verification.html")
def search(request):
    if request.session['loged in']:
        a = Active.objects.get(pk=1)
    
        return render(request,"search.html")

    
    
def about(request):
    if request.session['loged in']:
        a = Active.objects.get(pk=1)

        return render(request,"about.html",{"year":2022})
    

def signup(request):
    
    if request.session['loged in'] == True:
            
        return redirect("/index")
    if request.session['loged in'] == False:
        if request.method == 'POST':
            ss = Signup.objects.all()
            for i in ss:
                if i.name == request.POST.get('name'):
                    messages.info(request,"UserName Taken")
                
                    return redirect("/signup")
                
            s = Signup() 
            s.name = request.POST.get('name')
            s.password = request.POST.get('pwd')
            s.c_pwd = request.POST.get('c_pwd')
            if request.POST.get('pwd') == request.POST.get('c_pwd'):

                s.save()
                l = Login()
                l.name = request.POST.get('name')
                l.password = request.POST.get('c_pwd')
                l.save()
                
            
                
        
            
                request.session['name'] = l.name
                request.session['loged in'] = True
        
            
        
                

                return redirect("/index")

                
            else:
                messages.info(request,"Password Not Matched")
                return redirect("/signup")
     

    
    
        return render(request,"signup.html",{"year":2022})



    
def login(request):

    
    if request.session['loged in'] == True:
            
        return redirect("/index")
    if request.session['loged in'] == False:
        if request.method == 'POST':
            s = Signup.objects.all()
            for i in s:
                if i.name == request.POST.get('name'):
                    if i.c_pwd == request.POST.get('pwd'):
                        l = Login.objects.all()
                        for m in l:
                            if m.name == request.POST.get('name'):
                                m.name = request.POST.get('name')
                                m.password = request.POST.get('pwd')
                                m.save()
                        
                               
                              
                                request.session['name'] = m.name
                                    
                                request.session['loged in'] = True
                            
                                            
                            
                                
                            
                                    

                                return redirect("/index")
                    else:
                        messages.info(request,"invalid Password")
                        return render(request,"login.html",{"year":2022})
                
        return render(request,"login.html",{"year":2022})
    
    
def cart(request,foodcode,):

    if request.session['loged in']:
        f = Dishes.objects.get(pk=foodcode)
        cc = Cart.objects.all()
        for i in cc:
            if i.user_name == request.session['name']:
                if i.name == f.name:
                
                
                    return redirect("/dishes")
        
        
        l = Login.objects.all()
        for  i in l:
            if i.name == request.session['name']:
                c = Cart()
                c.user_name = i.name
                c.name = f.name
                c.code = f.code
                c.img  = f.img
                        
                c.prise = f.prise
                c.save()
        connn = Cart.objects.all()

        
        m_ = []
        for i in connn:
                if i.user_name == request.session['name']:
                    m_.append(i)

                        
                        
        return render(request,"cart.html",{"conn":m_})
        

        
def show_cart(request):
    if request.session['loged in']:
       c = Cart.objects.all()
       m_ = []
       for i in c:
        if i.user_name == request.session['name']:
            m_.append(i)
       
       return render(request,"cart.html",{"conn":m_})

            
         


def face_book(request):

    return redirect("/www.facebook.com")
def twi_tter(request):

    return redirect("/www.twitter.com")

def insta_gram(request):

    return redirect("/www.instagram.com")

def beha_nce(request):
    return redirect("/www.behance.com" )

def thanks(request):
    return render(request,'thankyou.html')


   

def profile(request):
    a = Active.objects.get(pk=1)
    if a.active_token == 0:
        return redirect("/")
    return render(request,"profile.html")

def searchh(request):
    if request.method == 'POST':
        search_element = request.GET.get('search')
        dishes_ = Dishes.objects.all()
        dish_len = len(dishes_)
        
        menu_ = Menu.objects.all()
        menu_len = len(menu_)

        sp_dish = specialdish.objects.all()
        spd_len = len(sp_dish)
        for i in range(7,19):
                obj_ = Dishes.objects.get(pk=i)
                counter = 0
            #if len(obj_.name) <= len(str(search_element)):
                for i in obj_.name:
                    for j in str(search_element):
                        if i == j:
                            counter = counter + 1
                if counter >= 1:
                    se_ar_h = Searchhhh()
                    se_ar_h.sear = str(search_element)
                    se_ar_h.save()
        so = Searchhhh.objects.all()
        return render(request,"search.html",{"output":so})


    
  
    return render(request,"search.html")

def logout(request):
    request.session['loged in'] = False
    request.session['name'] = None
    return redirect("/login")
    

class navs:
    def navbar(self,request,nav):

        if nav == "dishes":
           return redirect("/dishes")
        elif nav == "menu":
            return redirect("/menu")
        elif nav == "review":
 
           return redirect("/review")
        
        elif nav == "about":

            return redirect("/about")
        elif nav == "order":

            return redirect("/order")

        elif nav == "search":

            return redirect("/search")
        elif nav == "home":
            return redirect("/index")
        elif nav == "signup":
            return redirect("/signup")
        elif nav == "login":
            return redirect("/login")
        elif nav == "www.facebook.com":
            return face_book(request)
        elif nav == "logout":
            return redirect("/logout")
        else:
            pass



