from typing import Any
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render , redirect
from django.views.generic import ListView , DetailView
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import (
    GeneralSlider , HeaderTop , Category , Product,
    CooperativeCompanies
)

from .forms import (
    ContactUsForm, StayUpdatedForm
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


    def post(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:
        form = StayUpdatedForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            form = StayUpdatedForm()
        

        return redirect('home')


class ShopListView(ListView):
    template_name = 'shop.html'
    paginate_by = 1  # Number of products per page


    @staticmethod
    def __extract_all_data(request):
        products = Product.objects.all()
        paginator = Paginator(products, ShopListView.paginate_by)
        page = request.GET.get('page')

        try:
            products = paginator.page(page)
        except PageNotAnInteger:
            # If page is not an integer, deliver first page.
            products = paginator.page(1)
        except EmptyPage:
            # If page is out of range, deliver last page of results.
            products = paginator.page(paginator.num_pages)

        context = {
            'nav': 'shop',
            'products': products,
        }

        return context


    @staticmethod
    def product_filter_by_price(queryset , price_ranges):
        new_queryset = []
        for price in price_ranges:
            try:
                upper_bound , lower_bound = map(int , price.replace('$' , '').split(' - '))
            except Exception as ex:
                price(ex)
                return queryset
            else:
                queryset = queryset.filter(price__range=(lower_bound , upper_bound))
                new_queryset.append(queryset)

    @staticmethod
    def product_filter_by_color(queryset, color_ids):
        try:
            queryset = queryset.filter(colors__in = color_ids)
        except Exception as ex:
            return queryset

    @staticmethod
    def product_filter_by_size(queryset, size_ids):
        queryset = queryset.filter(sizes__in = size_ids)



    def get(self, request: HttpRequest, *args: Any, **kwargs: Any) -> HttpResponse:

        return render(request , self.template_name , context=self.__extract_all_data(request))



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

        return redirect("contact")


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








