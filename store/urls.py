from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    # navigation pages #
    path('', views.index, name='index'),
    path('shop', views.shop, name='shop'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('checkout_page', views.checkout_page, name='checkout_page'),
    path('blog', views.blog, name='blog'),
    path('about', views.about, name='about'),
    path('contact', views.contact, name='contact'),







    # login logout register #






    path('login/', views.login_user, name='login'),
    path('logout', views.logout_user, name='logout'),
    path('register', views.register_user, name='register'),
    path('verify_otp', views.verify_otp, name='verify_otp'),









    # products and cart #










    path('sproduct/<int:pk>', views.sproduct, name='sproduct'),
    path('update_item', views.updateItem, name='update_item'),








    #  payment #












    path('payment', views.payment, name='payment'),
    # path('COD', views.COD, name='COD'),
    path('payment_method', views.payment_method, name='payment_method'),
    path('payment/upi', views.upi_payment, name='upi_payment'),
    path('payment/other-upi', views.other_upi_payment, name='other_upi_payment'),
    path('payment/cera-pay', views.cera_pay_payment, name='cera_pay_payment'),
    path('payment/card', views.card_payment, name='card_payment'),
    path('payment/cod', views.cod_payment, name='cod_payment'),
    path('payment/net-banking', views.net_banking_payment, name='net_banking_payment'),
    path('payment/wallet', views.wallet_payment, name='wallet_payment'),
    path('payment/gift-card', views.gift_card_payment, name='gift_card_payment')

] 