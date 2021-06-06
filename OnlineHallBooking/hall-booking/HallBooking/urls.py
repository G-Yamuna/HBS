from django.urls import path
from HallBooking import views
from django.contrib.auth import views as v

urlpatterns = [
	path('',views.home,name="hm"),
	path('abt/',views.about,name="ab"),
	path('cnt/',views.contact,name="cn"),
	path('reg/',views.register,name="rg"),
	path('ch/',views.cgf,name="cg"),
	path('dashboard/',views.dashboard,name="dsh"),
	
	path('login/',v.LoginView.as_view(template_name="html/login.html"),name="lg"),
	path('logout/',v.LogoutView.as_view(template_name="html/logout.html"),name="lgo"),
	
	path('pfle/',views.prfle,name="pf"),
	path('updf/',views.updfple,name="upf"),
	
	path('vwhl/',views.hallsview,name="hlv"),
	path('adhl/',views.addhall,name="adh"),
	path('avhl/',views.availhalls,name="avh"),
	path('updhl/<int:pk>/',views.updathl,name="uphl"),
	path('dlt/<int:pj>/',views.deletehl,name="delt"),
    
    path('rolerq/',views.rolereq,name="rr"),
    path('permission/',views.permissions,name="per"),
    path('gvp/<int:k>/',views.giveper,name="gvpr"),

    path('bkhl/',views.bookhall,name="bkh"),
    path('det/',views.details,name="detail"),
] 