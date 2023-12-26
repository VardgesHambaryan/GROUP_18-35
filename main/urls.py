from django.urls import path
from .views import (
    HomeListView, ShopDetailView, ShopListView,
    CartListView, CheckoutListView, ContactListView
)


urlpatterns = [
    path('' , HomeListView.as_view() , name='home'),
    path('shop/' , ShopListView.as_view() , name='shop'),
    # path('shop/<....>' , HomeListView.as_view() , name='home'), # TODO: add unique indicator
    path('shopping-cart/' , CartListView.as_view() , name='cart'),
    path('shopping-cart/checkout/' , CheckoutListView.as_view() , name='checkout'),
    path('contact/' , ContactListView.as_view() , name='contact'),

]
