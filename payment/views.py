import paypalrestsdk
from django.conf import settings
from django.shortcuts import render, redirect
from django.urls import reverse
from main.models import Category , ShoppingCart

paypalrestsdk.configure({
    "mode": "sandbox",  # Change to "live" for production
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_SECRET,
})

def create_payment(request , price):
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal",
        },
        "redirect_urls": {
            "return_url": request.build_absolute_uri(reverse('execute_payment')),
            "cancel_url": request.build_absolute_uri(reverse('payment_failed')),
        },
        "transactions": [
            {
                "amount": {
                    "total": f"{price}",  # Total amount in USD
                    "currency": "USD",
                },
                "description": "Payment for Product/Service",
            }
        ],
    })



    if payment.create():
        return redirect(payment.links[1].href)  # Redirect to PayPal for payment
    else:
        return render(request, 'payment_failed.html')

def execute_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)

    if payment.execute({"payer_id": payer_id}):
        return render(request, 'payment_success.html')
    else:
        return render(request, 'payment_failed.html')

def payment_checkout(request):

    categories = Category.objects.all()
    try:
        cart_items = ShoppingCart.objects.filter(user=request.user)
    except:
        cart_items = []

    if cart_items:
        total_price = sum([item.product.price * item.quantity for item in cart_items])
    else:
        total_price = 0
    context = {
        'nav': 'checkout',
        'categories':categories,
        'cart_items':cart_items,
        'total_price':total_price,

    }
    return render(request, 'payement_checkout.html' , context=context)

def payment_failed(request):
    return render(request, 'payment_failed.html')