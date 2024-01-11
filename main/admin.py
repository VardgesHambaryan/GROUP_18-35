from django.contrib import admin
from django.apps import apps
from .models import (
    GeneralSlider , Image , Product , Review
)

@admin.register(GeneralSlider)
class GeneralSliderModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'sale_text' , 'img_preview']
    list_display_links = ['id', 'img_preview']
    list_editable = ['title' , 'sale_text']  


@admin.register(Image)
class ImageModelAdmin(admin.ModelAdmin):
    list_display = ['id' , 'img_preview']
    list_display_links = ['id', 'img_preview']

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['user' , 'product' , 'review' , 'rating']
    list_display_links = ['user' , 'product' ]
    list_editable = ['review' , 'rating']  
    list_filter = ['user' , 'product', 'rating']

@admin.register(Product)
class ProductModelAdmin(admin.ModelAdmin):
    list_display = ['name' , 'price' , 'discount' , 'about'] 
    list_display_links = ['name' , 'price' , 'discount' , 'about'] 
    list_filter = ['is_trendy']



#---------------------------------------Auto-Register-----------------------------------------
models = apps.get_models()

for model in models:
    try:
        admin.site.register(model_or_iterable=model)
    except admin.sites.AlreadyRegistered:
        pass
#----------------------------------------------------------------------------------------------