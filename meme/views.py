from django.shortcuts import render,HttpResponse,redirect
from django.contrib import messages
from .models import memobj,memeComment
from meme.templatetags import extras
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
        
        return render(request,"meme/memdet.html",{'tagname':reversed(myobj),'slug':slug})
    else:
        return redirect('memehome')    
    return redirect('memehome')


def memdetail(request,slug,id):
    try:
        obj=memobj.objects.get(mem_id=id)
        cmnt=memeComment.objects.filter(memepost=obj,parent=None)
        replies=memeComment.objects.filter(memepost=obj).exclude(parent=None)
        repDict={}
        for reply in replies:
            if not reply.parent.sno in repDict.keys():
                repDict[reply.parent.sno]=[]
                repDict[reply.parent.sno]=[reply]
            else:
                repDict[reply.parent.sno].append(reply)    
        
        return render(request,'meme/prodlanding.html',{'obj':obj,'comments':cmnt,'repDict':repDict})
    except Exception as e:
        return redirect("/")
    return redirect("/")
    # return HttpResponse(f"id is {id}")    

def postComment(request):
    if request.method=="POST":
        comment=request.POST.get('comment')
        user=request.user
        memid=request.POST.get('postId')
        memno=memobj.objects.get(mem_id=memid)
        parentno=request.POST.get('Parentsno')
        if parentno=="":
            #parent comment
            cmnt=memeComment(comment=comment,user=user,memepost=memno)
            cmnt.save()
            return redirect(f'/meme/{memno.mem_tag}/{memid}')
        else:
            parent=memeComment.objects.get(sno=parentno)
            cmnt=memeComment(comment=comment,user=user,memepost=memno,parent=parent)
            cmnt.save()
            return redirect(f'/meme/{memno.mem_tag}/{memid}')
        
    return HttpResponse("Post Comment Page")    