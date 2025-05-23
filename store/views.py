from django.forms import ValidationError
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import *
from django.contrib.auth.models import User
import re
import random
import string
from django.conf import settings
from django.core.mail import send_mail
from django.core.paginator import Paginator
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.


def index(request):

    products = Product.objects.all()
    categories = Category.objects.all()
    prods_by_cats = {}
    for category in categories:
        prods_by_cats[category.name] = Product.objects.filter(category=category)

    # Get the current customers cart
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_total']

    context = {'cartItems':cartItems}
    return render(request,"page/index.html",  {"prods_by_cats": prods_by_cats,'cartItems':cartItems})















def shop(request):
    products = Product.objects.all().order_by('id')
    user = request.user
    paginator = Paginator(products,8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    categories = Category.objects.all()
    prods_by_cats = {}
    for category in categories:
        prods_by_cats[category.name] = Product.objects.filter(category=category)

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_total']

    context = {'cartItems':cartItems}    

    return render(request,"page/shop.html", {'page_obj': page_obj, "prods_by_cats": prods_by_cats, "cartItems": cartItems})




















def sproduct(request,pk):
    product = Product.objects.get(id=pk)
      # Get the current customers cart
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_total']

    return render(request,"page/sproduct.html", {'product': product, 'cartItems':cartItems})


















def blog(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_total']

    context = {'cartItems':cartItems}
    return render(request,"page/blog.html", context)











def about(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_total']

    context = {'cartItems':cartItems}
    return render(request,"page/about.html", context)




















def cart(request):

    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_total']

    context = {'items': items, 'order': order, 'cartItems': cartItems}    
    return render(request,"page/cart_summary.html", context)














def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}

    context = {'items': items, 'order': order}    
    return render(request,"page/checkout.html", context)



















def checkout_page(request):
    # Assuming the customer is logged in and associated with a session
    customer = request.user.customer  # Modify this if you're using another method of identifying the customer
    order = Order.objects.get(customer=customer, complete=False)  # Get the current incomplete order
    
    if request.method == 'POST':
        # Get data from the form
        name = request.POST['name']
        email = request.POST['email']
        address = request.POST['address']
        city = request.POST['city']
        state = request.POST['state']
        postal_code = request.POST['postal-code']

        # Create and save the ShippingAddress
        shipping_address = ShippingAddress.objects.create(
            customer=name,
            order=order,
            email=email,
            address=address,
            city=city,
            state=state,
            zipcode=postal_code
        )

        # Optionally, save any other details like the customer email to the order
        order.shipping_address = shipping_address
        order.save()

        print ("email: ", email)

        # Redirect to the payment page
        return redirect('payment')
    



















    

def contact(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items':0, 'get_cart_total':0}
        cartItems = order['get_cart_total']

    context = {'cartItems':cartItems}
    return render(request,"page/contact.html", context)

def logout_user(request):
    logout(request)
    messages.success(request, ( "You have been logged out....."))
    return redirect('index')






















def login_user(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass1')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, ( "You have been logged in!!"))
            # Redirect to a success page.
            return redirect('index')
        else:
            # Return an 'invalid login' error message.
            messages.error(request, ( "Invalid Username or Password"))
            return redirect('login')
        
   
    return render(request, "page/login.html")     

















def generate_otp():
    return ''.join(random.choices(string.digits, k=6))















def send_verification_email(email, otp):
    subject = 'Verify Your Account Information '
    message = f'You have been trying to register your self in The Cara website.Your OTP for Money Withdrawl is {otp}.'
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [email])

















def register_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        # Validate fields
        errors = []

        if len(password1) < 8:
            errors.append("Your password must contain at least 8 characters.")

        if re.match(r'^\d+$', password1):
            errors.append("Your password can't be entirely numeric.")

        if username and username in password1:
            errors.append("Your password can't be too similar to your username.")

        common_passwords = ['password', '123456', '123456789', '12345678', '12345', '1234567', '1234567890', 'qwerty', 'abcdef', 'letmein']
        if password1 in common_passwords:
            errors.append("Your password can't be a commonly used password.")

        if password1 != password2:
            errors.append("Passwords must match.")

        if errors:
            for error in errors:
                messages.error(request, error)
            return render(request, 'register.html')
        
        
        # Generate OTP and send verification email
        otp = generate_otp()
        send_verification_email(email, otp)

         # Create the user but don't log them in yet
        request.session['pending_user'] = {
            'username': username,
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': password1,
            'otp': otp
        }

        return redirect('verify_otp')  # Redirect to OTP verification page

    return render(request, 'page/register.html')























def verify_otp(request):
    if request.method == 'POST':
        entered_otp = request.POST.get('otp')
        pending_user_data = request.session.get('pending_user')

        if not pending_user_data:
            messages.error(request, "Session expired or invalid. Please start the registration process again.")
            return redirect('register')  #Redirect to registration page or a suitable page

        expected_otp = pending_user_data.get('otp')

        if entered_otp == expected_otp:

            # Extract the necessary fields from pending_user_data
            username = pending_user_data.get('username')
            password = pending_user_data.get('password')
            email = pending_user_data.get('email')
            first_name = pending_user_data.get('first_name')
            last_name = pending_user_data.get('last_name')
            del pending_user_data['otp']  # Clear the OTP from the session data
            # Create the user
            try:
                user = User.objects.create_user(username=username, password=password)
                user.first_name = first_name
                user.last_name = last_name
                user.email = email
                user.save()
            except ValidationError as e:
                messages.error(request, str(e))
                return render(request, 'page/verify_otp.html')
            # Create the customer
            customer = Customer(user=user, first_name=first_name, last_name=last_name, email=email, password=password)
            customer.save()
            del request.session['pending_user']  # Clear the session data
            login(request, user)
            messages.success(request, "Your account has been successfully registered...")
            return redirect('index')

        else:
            messages.error(request, "Invalid OTP. Please try again.")
            return render(request, 'page/verify_otp.html')

    return render(request, 'page/verify_otp.html')






























def updateItem(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            productId = data['productId']
            action = data['action']
            print('Action:', action)
            print('Product ID:', productId)

            customer = request.user.customer
            product = Product.objects.get(id=productId)
            order , created = Order.objects.get_or_create(customer=customer, complete=False)

            orderItem , created = OrderItem.objects.get_or_create(order=order, product=product)

            if action == 'add':
                orderItem.quantity = (orderItem.quantity + 1)
            elif action =='remove':
                orderItem.quantity = (orderItem.quantity - 1)
            
            orderItem.save()

            if orderItem.quantity <= 0:
                orderItem.delete()

            return JsonResponse('Item Was Added', safe=False)
        except json.JSONDecodeError:
            return JsonResponse('Invalid JSON data', safe=False)
    else:
        return JsonResponse('Invalid HTTP method', safe=False)  
    




























def payment(request):

    return render(request, 'page/payment.html')

# def COD(request):
    
#     return render(request, 'page/cod.html')













def payment_method(request):
    if request.method == 'POST':
        selected_payment = request.POST.get('payment')
        print (selected_payment)

        # Handle different payment methods
        if selected_payment == 'upi_payment':
            return redirect('upi_payment')
        elif selected_payment == 'other_upi_payment':
            return redirect('other_upi_payment')
        elif selected_payment == 'cera_pay_payment':
            return redirect('cera_pay_payment')
        elif selected_payment == 'card_payment':
            return redirect('card_payment')
        elif selected_payment == 'cod_payment':
            return redirect('cod_payment')
        elif selected_payment == 'net_banking_payment':
            return redirect('net_banking_payment')
        elif selected_payment == 'wallet_payment':
            return redirect('wallet_payment')
        elif selected_payment == 'gift_card_payment':
            return redirect('gift_card_payment')
        else:
            return HttpResponse("No valid payment method selected.")
        

















        # payment methods #
        



def upi_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("<h1><center>UPI Payment Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')

def other_upi_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("You selected Other UPI Apps Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')

def cera_pay_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("<h1><center>You selected Cera Pay UPI Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')

    

def card_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("<h1><center>You selected Credit and Debit Cards Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')


def cod_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("<h1><center>You selected Cash on Delivery Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')


def net_banking_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("<h1><center>You selected Net Banking Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')



def wallet_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("<h1><center>You selected Wallets Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')



def gift_card_payment(request):
    if request.method == 'POST':
        # For now, just redirect to a success page or a confirmation message
        return HttpResponse("<h1><center>You selected Gift Card or Promo Code Processed Successfully!</center><h1>")
    
    # Render the HTML form for UPI payment
    return render(request, 'page/upi_payment.html')

