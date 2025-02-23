from django.shortcuts import render,redirect,get_object_or_404
from .models import *
from .form import RegistrationForm,CustomerProfileForm
from django.views import View
from django.contrib import messages
from django.contrib.auth import authenticate ,login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.http import JsonResponse
from urllib import request
from django.db.models import Q
import razorpay
from django.conf import settings
from django.contrib.auth.decorators import login_required
from razorpay.errors import BadRequestError  # Import the necessary Razorpay error

#For Mobile Model View#

@login_required(login_url="login")
def myview1(request):
    # Fetch the data from each model
    product = Mobile.get_data() 
    monitorss = Monitor.monitors()  
    earphoness = Earphone.earphones() 
    gamingconsolss = GamingConsole.consoles() 
    games = Games.mygames()

    # Print the data to the console (useful for debugging)
    print(product)
    print(monitorss)
    print(earphoness)
    print(gamingconsolss)
    print(games)

    # Pass the data as a single dictionary to the template
    return render(request, 'index.html', {
        'product': product,
        'monitorss': monitorss,
        'earphoness': earphoness,
        'gamingconsolss':gamingconsolss,
        'games': games,
    })

def fun(request):
    return render(request,'home.html')

def myview2(request):
    return render(request,'about.html')

def myview3(request):
    return render(request,"index.html")

def contact(request):
    return render(request,"contact.html")

class RegistrationView(View):
    def get(self, request):
        form = RegistrationForm()  # Create an empty form
        return render(request, 'regist.html', {'form': form})

    def post(self, request):
        form = RegistrationForm(request.POST)  # Bind the form with POST data
        if form.is_valid():
            form.save()  # Save the form data to the database
            messages.success(request, "Congratulations! Registration successful.")
            return render(request, 'regist.html', {'form': form})
        else:
            messages.error(request, "Registration failed. Please check the form for errors.")
            return render(request, 'regist.html', {'form': form})
    
   



def you(request):
    return render(request,"youtube.html")

def services(request):
    return render(request, 'services.html')


class ProductDetails(View):
    def get(self, request, pk):
        product = Mobile.objects.get(pk=pk) 
        return render(request,"productdetail.html",locals())

class ProductDetails2(View):
    def get(self, request, pk):
        product = Monitor.objects.get(pk=pk) 
        return render(request,"productdetail2.html",locals())

class ProductDetails3(View):
    def get(self, request, pk):
        product = Earphone.objects.get(pk=pk) 
        return render(request,"productdetail3.html",locals())
    

class ProductDetails4(View):
    def get(self, request, pk):
        product = GamingConsole.objects.get(pk=pk) 
        return render(request,"productdetail4.html",locals())
    
class ProductDetails5(View):
    def get(self, request, pk):
        product = Games.objects.get(pk=pk) 
        return render(request,"productdetail5.html",locals())
 
class ProfileView(View):
    def get(self, request):
        # Check if the user already has a profile
        try:
            # If the user has a profile, pre-populate the form with existing data
            customer = Customer.objects.get(user=request.user)
            form = CustomerProfileForm(instance=customer)
        except Customer.DoesNotExist:
            # If no profile exists, create a new empty form
            form = CustomerProfileForm()
        
        return render(request, "profile.html", {'form': form})

    def post(self, request):
        form = CustomerProfileForm(request.POST)
        
        if form.is_valid():
            user = request.user
            name = form.cleaned_data['name']
            locality = form.cleaned_data['locality']
            city = form.cleaned_data['city']
            mobile = form.cleaned_data['mobile']
            state = form.cleaned_data['state']
            zipcode = form.cleaned_data['zipcode']
            
            # Check if the user already has a profile
            try:
                customer = Customer.objects.get(user=user)
                # Update the existing customer profile
                customer.name = name
                customer.locality = locality
                customer.city = city
                customer.mobile = mobile
                customer.state = state
                customer.zipcode = zipcode
                customer.save()
                messages.success(request, "Profile updated successfully.")
            except Customer.DoesNotExist:
                # If the user doesn't have a profile, create a new one
                customer = Customer(user=user, name=name, locality=locality, city=city, 
                                     mobile=mobile, state=state, zipcode=zipcode)
                customer.save()
                messages.success(request, "Profile created successfully.")

        else:
            messages.warning(request, "Invalid input data. Please check the form.")

        # After handling the form submission, re-render the profile page with the form
        return render(request, "profile.html", {'form': form})
    
#Address.html#
def get(request):
    add = Customer.objects.filter(user=request.user)
    return render(request,'address.html',locals())

#UPDATEADDRESS.HTML#
#Updateaddress.html
class UpdateAddress(View):
    def get(self, request, pk):
        # Get the address object or return 404 if not found
        address = get_object_or_404(Customer, pk=pk)
        
        # Initialize the form with the current address data
        form = CustomerProfileForm(instance=address)
        
        return render(request, "updateaddress.html", {'form': form, 'address': address})

    def post(self, request, pk):
        # Get the address object or return 404 if not found
        address = get_object_or_404(Customer, pk=pk)
        
        # Initialize the form with the POST data and the existing address
        form = CustomerProfileForm(request.POST, instance=address)
        
        if form.is_valid():
            form.save()  # This saves the updated address to the database
            messages.success(request, "Congratulations! Profile Update Successful")
            return redirect('address')  # Redirect to the address list page or wherever you want
        else:
            messages.warning(request, "Invalid Input Data")
        
        # If the form is invalid, re-render the form with error messages
        return render(request, "updateaddress.html", {'form': form, 'address': address})
    


def monitors(request):
    # Fetch the data from  model
    monitorss = Monitor.monitors()  
    # Print the data to the console (useful for debugging)
    print(monitorss)
   
    # Pass the data as a single dictionary to the template
    return render(request, 'monitorscat.html', {'monitorss': monitorss})



def category_view(request):
    category = request.GET.get('category', 'monitors')  # Default 'monitors'
    
    if category == 'monitors':
        products = Monitor.objects.all()
    elif category == 'mobiles':
        products = Mobile.objects.all()
    elif category == 'earphones':
        products = Earphone.objects.all()
    elif category == 'gamingconsole':
        products = GamingConsole.objects.all()
    elif category == 'game':
        products = Games.objects.all()
    else:
        products = Monitor.objects.all()  # Default if category is invalid
    
    return render(request, 'category.html', {'category': category, 'product': products})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home') 


def add_to_cart(request):
    user = request.user
    product_id = request.GET.get('prod_id')
    product = Mobile.objects.get(id=product_id)
    Cart(user=user,product=product).save()
    return redirect("/cart")

def show_cart(request):
    user = request.user
    cart = Cart.objects.filter(user=user)
    amount=0
    for p in cart:
        value = p.quantity * p.product.discounted_price
        amount = amount + value
    totalamount = amount + 40
    return render(request,'addtocart.html',locals())




def Checkout(request):
    if request.method == "GET":
        try:
            # Create Razorpay client
            client = razorpay.Client(auth=(settings.RAZOR_KEY_ID, settings.RAZOR_KEY_SECRET))
            
            # Sample order data
            data = {
                "amount": 50000,  # amount in paise (i.e., 50000 paise = ₹500)
                "currency": "INR",
                "receipt": "order_receipt_123"
            }

            # Create order
            payment_response = client.order.create(data=data)
            print(payment_response)
            
            context = {
                "payment_response": payment_response
            }
            return render(request, 'checkout.html', context)
        
        except BadRequestError as e:
            # Handle specific Razorpay bad request error
            print(f"Razorpay Error: {e}")
            return render(request, 'error.html', {'message': "An error occurred while processing your payment request."})
        except Exception as e:
            # Handle other general errors
            print(f"General Error: {e}")
            return render(request, 'error.html', {'message': "Something went wrong. Please try again later."})
def payment_done(request):
    order_id = request.GET.get('order_id')
    payment_id = request.GET.get('payment_id')
    cust_id = request.GET.get('cust_id')

    # You can add logic here to verify the payment details and save them to the database
    return render(request, 'payment_done.html', {
        'order_id': order_id,
        'payment_id': payment_id,
        'cust_id': cust_id
    })




def plus_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity+=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 50
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def minus_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.quantity-=1
        c.save()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 50
        data = {
            'quantity':c.quantity,
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)
    
def remove_cart(request):
    if request.method == "GET":
        prod_id=request.GET['prod_id']
        c = Cart.objects.get(Q(product=prod_id) & Q(user=request.user))
        c.delete()
        user=request.user
        cart=Cart.objects.filter(user=user)
        amount = 0
        for p in cart:
            value = p.quantity * p.product.discounted_price
            amount = amount + value
        totalamount = amount + 50
        data = {
            'amount':amount,
            'totalamount':totalamount
        }
        return JsonResponse(data)





def error_view(request, error_message):
    # This view will render the error page
    return render(request, 'error.html', {'error': error_message})







