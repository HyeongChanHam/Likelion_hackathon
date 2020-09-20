from django.shortcuts import render,redirect,get_object_or_404
from .models import Content,DateTime,UserTemp
from .forms import ContentForm,UserTempForm
from datetime import datetime,timedelta,time,date

# Create your views here.
def index(request):
    all_contents=Content.objects.all()
    return render(request,'index.html',{'all_contents':all_contents})

def create(request):
    if request.method=='POST':
        form=ContentForm(request.POST)
        if form.is_valid():
            obj_content=Content(creator=form.data['creator'],contact=form.data['contact'],title=form.data['title'],department=form.data['department'],location=form.data['location'],reward=form.data['reward'],condition=form.data['condition'],detail=form.data['detail'],password=form.data['password'])
            obj_content.save()
            num_people=int(form.data['num_people'])
            runningdate=int(form.data['runningdate'])
            runningtime=int(form.data['runningtime'])
            date_time=form.data['date']
            for i in range(runningdate):
                date=(datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')+timedelta(days=i)).date()
                for j in range(num_people):
                    starttime=(datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')+timedelta(minutes=runningtime*j)).time()
                    endtime=(datetime.strptime(date_time,'%Y-%m-%d %H:%M:%S')+timedelta(minutes=runningtime*(j+1))).time()
                    obj_timeslot=DateTime(content=obj_content,date=date,starttime=starttime,endtime=endtime,isUsed=False)
                    obj_timeslot.save()
            return redirect('index')
    content_form=ContentForm()
    return render(request,'create.html',{'content_form':content_form})

def detail(request,content_id):
    content=get_object_or_404(Content,pk=content_id)
    time_slots=DateTime.objects.all()
    time_slot=time_slots.filter(content=content_id)
    return render(request,'detail.html',{'time_slot':time_slot})

def enrollment(request,timeslot_id):
    if request.method=='POST':
        filled_form=UserTempForm(request.POST)
        if filled_form.is_valid():
            temp_form=filled_form.save(commit=False)
            temp_form.time_temp=DateTime.objects.get(pk=timeslot_id)
            temp_form.save()

            timeslot=DateTime.objects.get(pk=timeslot_id)
            timeslot.isUsed=True
            timeslot.save()

            return redirect('index')

    timeslot=DateTime.objects.get(pk=timeslot_id)
    usertemp=UserTempForm()
    if timeslot.isUsed==False:
        return render(request,'usertemp.html',{'usertemp':usertemp,'timeslot':timeslot.id})
    if timeslot.isUsed==True:
        return redirect('advise',timeslot.id)

def advise(request,timeslot_id):
    timeslot=DateTime.objects.get(pk=timeslot_id)
    user=UserTemp.objects.get(time_temp=timeslot)
    usertemp_form=UserTempForm(instance=user)
    if request.method=="POST":
        updated_form=UserTempForm(request.POST,instance=user) 
        if updated_form.is_valid():
            updated_form.save()
            return redirect('index')
    return render(request,'usertemp_advise.html',{'usertemp':usertemp_form,'timeslot':timeslot.id})

def delete(request,timeslot_id):
    timeslot=DateTime.objects.get(pk=timeslot_id)
    timeslot.isUsed=False
    timeslot.save()
    user=UserTemp.objects.get(time_temp=timeslot)
    user.delete()

    return redirect('index')



