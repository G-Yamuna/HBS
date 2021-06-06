from django.shortcuts import render,redirect
from HallBooking.forms import Usrg,UpdaPfl,ChpwdForm,AddHalls,RoleR,RoleUp
from django.contrib.auth.decorators import login_required
from HallBooking.models import User,AdHl,RoleRqst
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,'html/home.html')

def about(request):
	return render(request,'html/about.html')

def contact(request):
	return render(request,'html/contact.html')


def register(request):
	if request.method == "POST":
		p = Usrg(request.POST)
		if p.is_valid():
			p.save()
			# messages.success(request,"You have successfully registered")
			return redirect('/login')
	p = Usrg()
	return render(request,'html/register.html',{'k':p})

@login_required
def dashboard(request):
	return render(request,'html/dashboard.html')

@login_required
def prfle(request):
	return render(request,'html/profile.html')

def cgf(request):
	if request.method=="POST":
		print("yes")
		c=ChpwdForm(user=request.user,data=request.POST)
		if c.is_valid():
			c.save()
			return redirect('/login')
	c=ChpwdForm(user=request)
	return render(request,'html/changepwd.html',{'t':c})


def updfple(request):
	if request.method == "POST":
		m = UpdaPfl(request.POST,instance=request.user)
		if m.is_valid() and n.is_valid():
			m.save()			
			# messages.success(request,"Profile updated Successfully")
			return redirect('/pfle')
	m = UpdaPfl(instance=request.user)
	# n = Im(instance=request.user.updf)
	return render(request,'html/updateprofile.html',{'p':m,'r':n})


@login_required
def hallsview(request):
	l = AdHl.objects.filter(add_id=request.user.id)
	# r = AdHl.objects.all()
	# z = []
	# for i in r:
	# 	if i.created_by == request.user.username:
	# 		continue
	# 	else:
	# 		z.append(i)
	return render(request,'html/hallsview.html',{'mn':l})

@login_required
def addhall(request):
	if request.method == "POST":
		k = AddHalls(request.POST,request.FILES)
		if k.is_valid():
			m = k.save(commit=False)
			m.add_id = request.user.id
			m.save()
			messages.success(request,"{} Hall Added Successfully".format(m.name))
			return redirect('/vwhl') 
	k = AddHalls()
	return render(request,'html/adhal.html',{'p':k})

@login_required
def updathl(request,pk):
	# c = AdHl.objects.get(id=pk)
	if request.method == "POST":
		g = UpHls(request.POST,request.FILES,instance=c)
		if g.is_valid():
			g.save()
			# messages.success(request,"{} Hall Details Updated Successfully".format(c.name))
			# return redirect("/vwhl")
	g = UpHls(instance=request.user)
	return render(request,'html/updatehall.html',{'y':g})

@login_required
def deletehl(request,pj):
	s = AdHl.objects.get(id=pj)
	if request.method == "POST":
			s.delete()
			messages.warning(request,"{} Hall Deleted Successfully".format(s.name))
			return redirect('/vwhl')
	return render(request,'html/deltehall.html',{'t':s})

@login_required
def rolereq(request):
	if request.method== "POST":
		k =RoleR(request.POST,request.FILES)
		if k.is_valid():
			s=k.save(commit=False)
			s.uname= request.user.username
			s.uid_id= request.user.id
			s.save()
			return redirect('/dashboard')
	k=RoleR() 
	return render(request,'html/rolereq.html',{'a':k})


@login_required
def permissions(request):
	ty=User.objects.all()
	a=RoleRqst.objects.all()
	c,rr=[],{}
	for b in a:
		c.append(b.uid_id)
	for j in ty:
		if j.is_superuser==1 or j.id not in c:
			continue
		else: 
			d=RoleRqst.objects.get(uid_id=j.id)
			rr[j.id]=j.username,d.roletype,j.role,j.id
	e=rr.values()

	# rr={}
	# for a in ty:
	# 	if a.is_superuser==1:
	# 		continue
	# 	else:
	# 		b=RoleRqst.objects.get(uid_id=a.id)
	# 		rr[a.id]=a.username,b.roletype,a.role,a.id
	# c=rr.values()
	# print(rr.items)
	return render(request,'html/givepermissions.html',{'q':e})



@login_required
def giveper(request,k):
	r=User.objects.get(id=k)
	m=RoleRqst.objects.get(uid_id=k)
	if request.method == "POST":
		k=RoleUp(request.POST,instance=r)
		if k.is_valid():
			k.save()
			m.is_checked=1
			m.save()
			return redirect('/permission')
	k= RoleUp(instance=r)
	return render(request,'html/acceptpermissions.html',{'y':k})


def availhalls(request):
	l = AdHl.objects.filter(add_id=request.user.id)
	return render(request,'html/availablehalls.html',{'mn':l})

def details(request):
	return render(request,'html/details.html')

def bookhall(request):
	return render(request,'html/booking.html')