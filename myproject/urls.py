"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from myapp.views import *
from django.conf import settings
from django.contrib.auth import views as auth_view
from myapp.form import *
from myapp import views
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',myview1,name='home'),
    path('home',fun),
    path('about',myview2,name='about'),
    path('index',myview3),
    path("login/",login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path("contact",contact,name='contact'),
    path('regist/',views.RegistrationView.as_view(),name='registration'),
    path("youtube/",you),
    path("services",services,name='services'),
    path('productdetail/<int:pk>',views.ProductDetails.as_view(), name="product"), 
    path('productdetail2/<int:pk>',views.ProductDetails2.as_view(), name="product2"), 
    path('productdetail3/<int:pk>',views.ProductDetails3.as_view(), name="product3"), 
    path('productdetail4/<int:pk>',views.ProductDetails4.as_view(), name="product4"), 
    path('productdetail5/<int:pk>',views.ProductDetails5.as_view(), name="product5"), 
    #Products Categories URL 
    path('monitor',monitors,name='mymonitors'),
    path('category/', category_view, name='category_view'),
    
    path('profile/',views.ProfileView.as_view(),name='profile'),
    path('address/',views.get,name='address'),
    path('updateaddress/<int:pk>',views.UpdateAddress.as_view(),name='updateaddress'),
    path('add-to-cart/',views.add_to_cart,name='add_to_cart'),
    path('cart/',views.show_cart,name='showcart'),
    path('pluscart/',views.plus_cart,name='plus_cart'),  
    path('minuscart/',views.minus_cart,name='minus_cart'),   
    path('removecart/',views.plus_cart,name='remove_cart'),
    #Remove 
    path('checkout/',views.Checkout,name='checkout'),
    path('paymentdone/', views.payment_done, name='payment_done'),
   

#Password :-->
    path('passwordchange/',auth_view.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=MyPasswordChangeForm,success_url='/passwordchangedone'),name='passwordchange'),
    path('passwordchangedone/',auth_view.PasswordChangeDoneView.as_view(template_name='passwordchangedone.html'),name='passwordchangedone'),
    path('password-reset/',auth_view.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm),name='password_reset'),
    path('password-reset/done/',auth_view.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>',auth_view.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html",form_class=MySetPasswordForm),name='password_reset_confirm'),
    path('password-reset-complete/',auth_view.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),name='password_reset_complete'),
    
    path('error/', views.error_view, name='error'),
    

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

