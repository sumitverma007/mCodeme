from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .models import probobj

# Create your views here.
def problemhome(request):
    allprob=probobj.objects.all()
    return render(request,'problem/problemhome.html',{'allprob':reversed(allprob)})

def pubpage(request):
    # print(request.user)
    
    if request.user.is_authenticated:
        allprob=probobj.objects.all()
        tags=set(i.p_tag for i in allprob)
        # print(tags)

        
        return render(request,'problem/pubproblem.html',{'tags':tags})
        




    else:
        return redirect('problemhome')   
    
    # if request.user.is_authenticated() is not None:
    #     return HttpResponse('Authentic')
    # else:
    #     return HttpResponse('No authentication')
    return redirect('problemhome')  
def showtags(request,tagname):
    targetobj=probobj.objects.filter(p_tag=tagname)
    if len(targetobj)>0:
        return render(request,"problem/targetland.html",{'allprob':targetobj,'tag':tagname})
    else:
        return redirect("/problem/")    
    return redirect("/problem/")  
def probdetails(request,id):
    targetobj=probobj.objects.get(p_id=id)
    return render(request,"problem/probdetail.html",{'obj':targetobj})
    # return HttpResponse(f"Gettin ready for product no {id}")    

def problemtags(request):
    allobj=probobj.objects.all()
    unique_tags={i.p_tag for i in allobj}
    final_obj=set()
    for i in unique_tags:
        item=probobj.objects.filter(p_tag=i)
        final_obj.add(item[0])
    return render(request,'problem/problemtags.html',{'tagname':final_obj})
def handlepubpage(request):
    if request.method=='POST':
        tagname=request.POST.get('tags',default="")
        newtag=request.POST.get('newtag',default="")
        cuser=request.user
        pname=request.POST.get('pname')
        pdesc=request.POST.get('pdesc')
        pin=request.POST.get('pin')
        pout=request.POST.get('pout')
        pout=request.POST.get('pout')
        pconst=request.POST.get('pconst')
        pexin=request.POST.get('pexin')
        pexout=request.POST.get('pexout')
        pcode=request.POST.get('pcode')
        if tagname=="" and newtag=="":
            messages.error(request,"You can't just leave tags empty")
            return redirect('/problem/publishpage/')
        if tagname!="" and newtag!="":
            messages.error(request,"Tags are conflicting choose any one")
            return redirect('/problem/publishpage/')
        if tagname!="":
            # print(tagname,cuser,pname,pdesc,pin,pout,pconst,pexin,pexout)
            newprob=probobj(p_user=cuser,p_tag=tagname,p_name=pname,p_desc=pdesc,p_in=pin,p_out=pout,p_const=pconst,p_exin=pexin,p_exout=pexout,p_code=pcode)
            newprob.save()
            messages.success(request,"Question added successfully")
            return redirect('/problem/')     
        if newtag!="":
            newprob=probobj(p_user=cuser,p_tag=newtag,p_name=pname,p_desc=pdesc,p_in=pin,p_out=pout,p_const=pconst,p_exin=pexin,p_exout=pexout,p_code=pcode)
            newprob.save()
            messages.success(request,"Question added successfully")
            return redirect('/problem/')  
        
    return redirect('/problem/')        