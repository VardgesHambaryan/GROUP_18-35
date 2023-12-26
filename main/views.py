from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views.generic import ListView , DetailView
from .models import (
    GeneralSlider , HeaderTop , Category , Product,
    CooperativeCompanies
)

from .forms import (
    ContactUsForm
)


class HomeListView(ListView):
    template_name = 'index.html'

    @staticmethod
    def __extract_all_data():
        general_sliders = GeneralSlider.objects.all()
        header = HeaderTop.objects.get()
        categories = Category.objects.all()
        just_arrived = Product.objects.order_by('-created_at')[:8]
        trandy_products = Product.objects.order_by('-id')[:8]
        cooperative_companies = CooperativeCompanies.objects.all()


        context = {
            'nav': 'home',
            'general_sliders':general_sliders,
            'header':header,
            'categories':categories,
            "just_arrived":just_arrived,
            "trandy_products":trandy_products,
            "cooperative_companies":cooperative_companies
        }

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        return render(request , self.template_name , context=self.__extract_all_data())


class ShopListView(ListView):
    template_name = 'shop.html'

    @staticmethod
    def __extract_all_data():
        products = Product.objects.all()

        context = {
            'nav': 'shop',
            'products':products,
        }

        return context
    
    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        return render(request , self.template_name , context=self.__extract_all_data())


class ShopDetailView(DetailView):
    template_name = 'index.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = {

        }
        return render(request , self.template_name , context=context)


class ContactListView(ListView):
    template_name = 'contact.html'

    @staticmethod
    def __extract_all_data():

        context = {
            'nav': 'contact',

        }
        return context

    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        return render(request , self.template_name , context=self.__extract_all_data())


    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = ContactUsForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = ContactUsForm()
        
        return render(request, self.template_name , context={
            'form':form
        })


class CartListView(ListView):
    template_name = 'cart.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = {
            'nav': 'cart',

        }
        return render(request , self.template_name , context=context)


class CheckoutListView(ListView):
    template_name = 'checkout.html'


    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        context = {
            'nav': 'checkout',

        }
        return render(request , self.template_name , context=context)











