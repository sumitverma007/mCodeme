from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import memobj

# Create your views here.
def memehome(request):
    allobj=memobj.objects.all()
    unique_tags={i.mem_tag for i in allobj}
    final_obj=set()
    for i in unique_tags:
        item=memobj.objects.filter(mem_tag=i)
        final_obj.add(item[0])
    # print(final_obj)
    # print(type(final_obj))

    return render(request,"meme/memehome.html",{'tagname':final_obj})

def memetag(request,slug):

    myobj=memobj.objects.filter(mem_tag=slug)
    if len(myobj)>0:
        
        return render(request,"meme/memdet.html",{'tagname':myobj,'slug':slug})
    else:
        return redirect('memehome')    
    return redirect('memehome')


def memdetail(request,slug,id):
    try:
        obj=memobj.objects.get(mem_id=id)
        return render(request,'meme/prodlanding.html',{'obj':obj})
    except Exception as e:
        return redirect("/")
    return redirect("/")
    # return HttpResponse(f"id is {id}")    