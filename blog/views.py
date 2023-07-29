from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Product as pr
from .models import Contactdata as cd
from .models import Orders as od
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import math
from django.contrib.auth.models import User
    

def about(request):
    return render(request, '../templates/blog/about.html')

def productpage(request, myid):
    myproduct = pr.objects.filter(id= myid) 
    #we will get a list so our product =product[0]
    category=myproduct[0].cat
    categorywise= pr.objects.filter(cat = category)

    return render(request, '../templates/blog/product_page.html', {'myproduct': myproduct[0], 'categorywise': categorywise})
    

# Assuming 'pr' is the model representing the 'Product' class

def shop(request):
    # Step 1: Querying distinct categories from the 'pr' model and store them in 'query' list
    query = list(pr.objects.values_list('cat', flat=True).distinct())
    
    # Step 2: Create an empty dictionary 'categorywise' to store products categorized by category
    categorywise = {}
    
    # Step 3: Iterate over each category in the 'query' list
    for cate in query:
        # Step 4: Filter products with the current category and store them in 'products' list
        products = list(pr.objects.filter(cat=cate))
        
        # Step 5: Add the 'products' list to the 'categorywise' dictionary with 'cate' as the key
        categorywise[cate] = products

    # Step 6: Pass 'categorywise' dictionary to the template context
    context = {'categorywise': categorywise}
    return render(request, 'blog/index.html', context)



def contact(request):
    return render(request, '../templates/blog/contact.html')

def managecontact(request):
    if(request.method == 'POST'):
        #on server side we take the name of form into consideration as data sent from form is in key: values where
        #key= name , value=value
        c_name=request.POST['name']
        c_email=request.POST['email']
        c_subject=request.POST['subject']
        c_message=request.POST['message']
        
        cdata=cd(name=c_name, email=c_email, subject=c_subject, message= c_message )
        print(cdata)
        cdata.save()

        return redirect('blog')

def signup(request):
    return render(request, '../templates/blog/signup.html')
        

def handlesignin(request):
    if request.method=="POST":
        # Get the post parameters
        username=request.POST['username']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        pass1=request.POST['pass1']

        # check for errorneous input
        
        # Create the user
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname
        myuser.save()
        return redirect('blog')

    else:
        return HttpResponse("404 - Not found")

def mycart(request):
    return render(request, '../templates/blog/cart.html')

def checkout(request):
    if request.method == 'POST':
      
        uname=request.POST['uname']
        email=request.POST['email']
        fname=request.POST['fname']
        lname=request.POST['lname']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        zip_code=request.POST['zip_c']
        update1="Your Order was Placed Sucessfully."
        update2="Your Order has beed Couriered via POST. POST_ID: AASS_"+country+state+uname+zip_code
        update3="Your Order has your nearest Hub! It will be dispatched soon!!"
        order=od(username= uname, fname= fname, lname= lname, email= email,update1=update1 ,update2=update2,update3=update3 , address= address, country= country, state= state, zip_code= zip_code )
        order.save()
        return HttpResponse("checkingout")
    else:
        return HttpResponse('Only POST request entertained.')

def search(request):
  if request.method == 'POST':
    sub_cat=request.POST['sub_cat']
    filtered = list(pr.objects.filter(cat = sub_cat))
    filt={}
    filt[sub_cat]=filtered
    return render(request, '../templates/blog/searched.html',{'categorywise' : filt})

# def tracker(request):
#    if request.method == 'POST':
#      order_id=request.POST['id']
#      flag=1
#      order = od.objects.filter(id = order_id)
#      order=order[0]
#      if order is not null :
#        return render(request,"../templates/blog/tracker.html" ,{"order": order, "flag": 1})
#      else:
#         message.error(request,'Invalid ID')
#         return redirect('blog')
#    else:
#       return render(request,"../templates/blog/tracker.html" ,{"flag": 0})


def tracker(request):
    if request.method == 'POST':
        order_id = request.POST['id']
        print(order_id)
        try:
            order = od.objects.get(id=order_id)
            return render(request, 'blog/tracker.html', {"order": order, "flag": 1})
        except od.DoesNotExist:
            messages.error(request, 'Invalid ID')
            return redirect('blog')
    else:
        return render(request, 'blog/tracker.html', {"flag": 0})

def user_login(request):
     if request.method == 'POST':
        loguname = request.POST['username']
        logpassword=request.POST['password']

        user = authenticate(username=loguname, password=logpassword)
        if user is not None:
            login(request, user)
            messages.success(request, 'sucessfully logged in')
            return redirect('blog')
        else :
            messages.error(request, "Invalid Credentials")
           
def user_logout(request):
    logout(request)
    messages.success(request, 'sucessfully loged out!')
    return redirect('blog')