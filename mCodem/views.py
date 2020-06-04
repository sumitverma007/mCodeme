from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def index(request):
    # return HttpResponse("Home Shit Man")
    return render(request,"home.html")

def handleLogin(request):
    if request.method=="POST":
        luname=request.POST.get('luname')
        lupass=request.POST.get('lpass')
        user = authenticate(username=luname,password=lupass)
        if user is not None:
            login(request,user)
            messages.success(request,f"Welcome {user.first_name}")
            return redirect("/")
        else:
            messages.error(request,"Wrong Credentials")
            return redirect("/")
    return redirect("/")            
        


def handleSignup(request):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        email=request.POST.get('email')
        if len(uname)<4 or not uname.isalnum():
            messages.error(request,"username should be atleast 4 character and should only alphanumeric characters")
            return redirect("/")
        if pass1!=pass2:
            messages.error(request,"Password Didn't match")
            return redirect("/")
        # messages.success(request,"launde sahi hai")  
       
        try:
            myuser=User.objects.create_user(uname,email,pass1)
            myuser.first_name=fname
            myuser.last_name=lname
            myuser.save()
            messages.success(request,"Please Log in to continue")
            return redirect("/")
        except Exception as e:
            messages.error(request,f"Username {uname} Already Taken .Try Other")
            return redirect("/")    

        
         

    return redirect("/")




def handleLogout(request):
    if request.method=="POST":
        logout(request)
        return redirect("/")
    return redirect("/")        
