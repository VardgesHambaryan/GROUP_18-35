from collections.abc import Iterable
from django.db import models
from django.utils.html import mark_safe
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User


class HeaderTop(models.Model):
    FAQs = models.TextField('FAQs')
    Help = models.TextField("Help")
    Support = models.TextField("Support")

    facebook = models.URLField("Facebook URL")
    twitter = models.URLField("Twitter URL")
    linkedin = models.URLField('LinkedIn URL')
    instagram = models.URLField('Instagram URL')
    youtube = models.URLField('Youtube URL')

    def __str__(self) -> str:
        return "Header Data"
    
    class Meta:
        verbose_name = 'Header Top'
        verbose_name_plural = 'Header Top'


class GeneralSlider(models.Model):
    sale_text = models.CharField('About Sale' , max_length = 150)
    title = models.CharField('Title' , max_length = 150)
    img = models.ImageField('Image' , upload_to='media')

    def img_preview(self):
        return mark_safe(f'<img src = "{self.img.url}" width = "60"/>')

    def __str__(self) -> str:
        return self.title
    
    class Meta:
        verbose_name = 'General Slider'
        verbose_name_plural = 'General Sliders'


class Category(models.Model):

    name = models.CharField('Category', max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product Category'
        verbose_name_plural = 'Product Categories'


class SubCategory(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE , related_name = 'subcat')
    name = models.CharField('Category', max_length=50)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'Product Sub Category'
        verbose_name_plural = 'Product Sub Categories'


class Color(models.Model):

    name = models.CharField('Color Name',max_length=20)

    def __str__(self) -> str:
        return self.name


class Size(models.Model):

    name = models.CharField('Size Name',max_length=5)

    def __str__(self) -> str:
        return self.name


class Image(models.Model):

    img = models.ImageField('Product Image',upload_to='media')

    def __str__(self) -> str:
        return "Image"

    def img_preview(self):
        return mark_safe(f'<img src = "{self.img.url}" width = "60"/>')


from django.db import models

class Product(models.Model):
    # Basic Information
    name = models.CharField('Product Name', max_length=255)
    about = models.TextField('About Product')
    description = models.TextField('Description')
    information = models.TextField('Information')

    # Pricing and Discounts
    price = models.PositiveSmallIntegerField('Product Price')
    discount = models.DecimalField('Discount Size', max_digits=3, decimal_places=1)
    discounted_price = models.DecimalField('Discounted Price', max_digits=10, decimal_places=2, blank=True, null=True)


    # Product Attributes
    is_trendy = models.BooleanField(default=False)
    images = models.ManyToManyField('Image')
    colors = models.ManyToManyField('Color')
    sizes = models.ManyToManyField('Size')
    category = models.ForeignKey('Category', on_delete=models.CASCADE, related_name='products', null=True)

    # Social Media Links
    facebook = models.URLField('Facebook URL', blank=True)
    twitter = models.URLField('Twitter URL', blank=True)
    linkedin = models.URLField('LinkedIn URL', blank=True)
    pinterest = models.URLField('Pinterest URL', blank=True)

    # Timestamps
    created_at = models.DateTimeField('Created At', auto_now_add=True, null=True)
    updated_at = models.DateTimeField('Updated At', auto_now=True, null=True)

    def __str__(self) -> str:
        return self.name

    def save(self, *args, **kwargs) -> None:
        """Override the save method to set the discounted price."""
        self.discounted_price = self.price * (1 - float(self.discount) / 100)
        super(Product, self).save(*args, **kwargs)


class Review(models.Model):

    RATING_CHOICES = [
        (1,'1 - Poor'),
        (2,'2 - Fair'),
        (3,'3 - Good'),
        (4,'4 - Very good'),
        (5,'5 - Excellent'),
    ]

    user = models.ForeignKey(User , on_delete=models.PROTECT , related_name = 'rev_user')
    product = models.ForeignKey(Product, on_delete=models.CASCADE ,related_name='prod_rev')
    rating = models.CharField(max_length=1 , choices = RATING_CHOICES)
    review = models.TextField('Review Text')

    def __str__(self) -> str:
        return self.rating


class StayUpdated(models.Model):

    email = models.EmailField('Customer Email')

    def __str__(self) -> str:
        return self.email
    
    class Meta:
        verbose_name = "Stay Updated"
        verbose_name_plural = "Stay Updated"


class CooperativeCompanies(models.Model):
    image = models.ImageField('Image')

    class Meta:
        verbose_name = "CooperativeCompanie"
        verbose_name_plural = "CooperativeCompanies"



class ShoppingCart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'cart_user')
    product = models.ForeignKey(Product,on_delete=models.CASCADE, related_name = 'cart_product')
    quantity = models.PositiveSmallIntegerField(default=1)
    total_price = models.FloatField(null=True, blank=True)
    def __str__(self):
        return self.product.name
    

    def save(self, *args, **kwargs) -> None:
        """Override the save method to set the discounted price."""
        self.total_price = self.product.price * self.quantity

        super(ShoppingCart, self).save(*args, **kwargs)

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCarts"




# ---------------------------------------Contact-Page----------------------------------------


class ContactUs(models.Model):
    name = models.CharField('Customer Name', max_length = 50)
    email = models.EmailField('Customer Email')
    subject = models.CharField('Customer Message Subject', max_length = 50)
    message = models.TextField('Message text')

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        verbose_name = 'ContactUs'    
        verbose_name_plural = 'ContactUs'        


class GetInTouch(models.Model):
    text = models.TextField('Contact Information')

    def __str__(self):
        return 'Contact Information'

    class Meta:
        verbose_name = 'GetInTouch'
        verbose_name_plural = 'GetInTouch'

    
class Store(models.Model):
    address = models.CharField('Store Address', max_length=255)
    email = models.EmailField("Email", max_length=254)
    phone = PhoneNumberField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Store'
        verbose_name_plural = 'Stores'


# ----------------------------------------------------------------------------------------------
