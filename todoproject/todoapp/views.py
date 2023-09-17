from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import task
from .forms import todoform
# Create your views here.
def test(request):
    detail = task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        details=task(taskname=name,priority=priority,date=date)
        details.save()
    return render(request,'demo.html',{'data':detail})

# def details(request):
#
#     return render(request,'details.html',)

def delete(request,taskid):
    Task=task.objects.get(id=taskid)
    if request.method=='POST':
        Task.delete()
        return redirect('/')
    return render(request,'delete.html')

def update(request,id):
    Task=task.objects.get(id=id)
    f=todoform(request.POST or None,instance=Task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':Task})