from django.shortcuts import render,redirect
from App.models import *
from App.forms import *
from django.contrib.auth import authenticate,login,logout
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.


def register(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("/")
	form = NewUserForm()
	return render (request,'register.html',{'form':form})

def loginpage(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			return redirect('/userhome')  
		else:
			return redirect('/login')
	
 
	return render(request, 'login.html')

@login_required
def custom_logout(request):
    logout(request)
    return redirect("/login")

def userhome(request):
    return render(request,'userhome.html')


class FoodCreate(CreateView):
    model = Food
    form_class = FoodForm
    template_name = 'addfood.html'
    success_url = reverse_lazy('addfood')
    
    
class ActivityCreate(CreateView):
    model = Activities
    form_class = ActivitiesForm
    template_name = 'addactivity.html'
    success_url = reverse_lazy('addactivity')
    
def foodlist(request):
    flist = Food.objects.all()
    return render(request,'flist.html',{'flist':flist})

def activitylist(request):
    alist = Activities.objects.all()
    return render(request,'alist.html',{'alist':alist})

def adduserfood(request,id):
    Uid = User.objects.get(id=id)
    flist = Food.objects.all()
    alist = Activities.objects.all()
    if request.method  == 'POST':
        user = User.objects.get(id=id)
        fooditem = request.POST.get('fooditem')
        fooditems = Food.objects.get(fid=fooditem)
        activity = request.POST.get('activity')
        activitys = Activities.objects.get(aid=activity)
        fintake = request.POST.get('fintake')
        ahours = request.POST.get('ahours')
        userFood = UserFood(fooditem=fooditems,fintake=fintake,activity=activitys,ahours=ahours,user=user)
        userFood.save()
	    
    return render(request,'userfood.html',{'flist':flist,'alist':alist})


    
    
    
    
            
   
     
