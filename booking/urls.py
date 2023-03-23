from django.urls import path, include
from . import views

app_name = "booking"
urlpatterns = [
 
    path('index',views.index,name='index'),
    path('elements',views.elements,name='elements'),
    path('hotels', views.hotels,name='hotels'),
    path('insurance',views.insurance,name='insurance'),
    path('packages',views.packages,name='packages'),
    path('about',views.about,name='about'),
    path('bloghome',views.bloghome,name='bloghome'),  
    path('login',views.login,name='login'),   
    path('register',views.login,name='register'),   
    path('search',views.search,name='search'),
    path('book',views.book,name='book'),
    path('booking',views.booking,name='booking'),
    path('layout',views.layout,name='layout'),
    path('layout2',views.layout2,name='layout2'),

]

