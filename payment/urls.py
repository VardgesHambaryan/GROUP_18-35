from django.urls import path
from . import views

urlpatterns = [
    path('', views.payment_checkout, name='checkout_payment'),
    path('create_payment/<int:price>', views.create_payment, name='create_payment'),
    path('execute_payment/', views.execute_payment, name='execute_payment'),
    path('payment_failed/', views.payment_failed, name='payment_failed'),  
]