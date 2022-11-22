from django.shortcuts import render,redirect
from .models import Tasks
from authapp.auth_decorators import check_authentication

# Create your views here.
def index(request):
    return render(request,'base.html')
    
@check_authentication
def dashboard(request):
    data={}
    tasks=Tasks.objects.filter(user_id=request.session['ssk_logged_user_id']).exclude(status=2).values('id','title','status').order_by('-date_created')
    if len(tasks)<=0:
        return render(request, 'dashboard.html',data) 
    data['tasks']=tasks
    pending_tasks=[]
    completed_tasks=[]
    for task in tasks:
        if str(task['status'])=='0':
            pending_tasks.append(task)
        elif str(task['status'])=='1':
            completed_tasks.append(task)
    if len(pending_tasks)>=1:
        data['pending_tasks']=pending_tasks
    if len(completed_tasks)>=1:
        data['completed_tasks']=completed_tasks
    return render(request, 'dashboard.html',data) 

@check_authentication
def addTask(request):
    if request.method=='POST':
        inp_data=request.POST.dict()
        task_obj=Tasks(
            user_id=request.session['ssk_logged_user_id'],
            title=inp_data['title']
        )
        task_obj.save()
    return redirect('/dashboard')

@check_authentication
def deleteTask(request,id):
    try:
        task_obj=Tasks.objects.filter(id=id).get()
        task_obj.status=2
        task_obj.save()
    except:
        data={'message':'Something went wrong!'}
        return render(request,'alert.html',data)
    return redirect('/dashboard')

@check_authentication
def completedTask(request,id):
    try:
        task_obj=Tasks.objects.filter(id=id).get()
        task_obj.status=1
        task_obj.save()
    except:
        data={'message':'Something went wrong!'}
        return render(request,'alert.html',data)
    return redirect('/dashboard')