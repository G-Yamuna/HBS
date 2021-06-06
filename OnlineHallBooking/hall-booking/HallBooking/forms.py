from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,PasswordChangeForm
from django import forms
from HallBooking.models import User,AdHl,RoleRqst
from django.forms import ModelForm

class Usrg(UserCreationForm):
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Password"}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control","placeholder":"Enter Confirm Password"}))
	class Meta:
		model = User
		fields = ["username","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Username",
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Enter Email id",
			}),
		}

class RoleR(forms.ModelForm):
	class Meta:
		model = RoleRqst
		fields= ["uname","roletype","proof"]
		widgets={
		"uname":forms.TextInput(attrs={"class":"form-control my-2","readonly":True}),
		"roletype":forms.Select(attrs = {"class": "form-control my-2",}),
		"proof":forms.ClearableFileInput(attrs={"class":"form-control"}),

		}

class RoleUp(forms.ModelForm):
	class Meta:
		model = User
		fields = ["username","role"]
		widgets={
		"username": forms.TextInput(attrs={"class":"form-control","readonly":True,}),
		"role":forms.Select(attrs={"class":"form-control"}),
		}

class UpdaPfl(ModelForm):
	class Meta:
		model = User
		fields = ["username","first_name","last_name","email"]
		widgets = {
		"username":forms.TextInput(attrs={
			"class":"form-control",
			}),
		"first_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update First Name"
			}),
		"last_name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Update Last Name"
			}),
		"email":forms.EmailInput(attrs={
			"class":"form-control",
			"placeholder":"Update Emailid"
			}),
		}

class ChpwdForm(PasswordChangeForm):
	old_password=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter Old password"}))
	new_password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Enter New password"}))
	new_password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':"Confirm your New password"}))
	class Meta:
		model=User
		fields=['oldpassword','newpassword','confirmpassword']


class AddHalls(forms.ModelForm):
	class Meta:
		model = AdHl
		fields = ["name","address","halltype","occupancy"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Enter name",
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"Enter address",
			"rows":3,
			"cols":10
			}),
		"halltype":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Marriage/Seminar/Event",
			}),
		"occupancy":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Occupancy(capacity)",
			})

		}


class UpHls(ModelForm):
	class Meta:
		model = AdHl
		fields = ["name","address","halltype","occupancy"]
		widgets = {
		"name":forms.TextInput(attrs={
			"class":"form-control",
			"readonly":True
			}),
		"address":forms.Textarea(attrs={
			"class":"form-control",
			"placeholder":"Update Address",
			"rows":3,
			"cols":10
			}),
		"halltype":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Marriage/Seminar/Event",
			}),
		"occupancy":forms.TextInput(attrs={
			"class":"form-control",
			"placeholder":"Occupancy(capacity)",
			})
		}