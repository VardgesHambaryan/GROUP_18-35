from django.db import models
from django.utils.html import mark_safe
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

    name = models.CharField('Color Name',max_length=5)

    def __str__(self) -> str:
        return self.name


class Image(models.Model):

    img = models.ImageField('Product Image',upload_to='media')

    def __str__(self) -> str:
        return "Image"

    def img_preview(self):
        return mark_safe(f'<img src = "{self.img.url}" width = "60"/>')


class Product(models.Model):

    name = models.CharField('Product Name', max_length=255)
    price = models.PositiveSmallIntegerField('Product Price')
    discount = models.DecimalField('Discount Size',max_digits=3 ,decimal_places = 1)
    about = models.TextField('About Product')
    is_trandy = models.BooleanField(default=False)


    images = models.ManyToManyField(Image)
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products",null=True)


    facebook = models.URLField('Facebook URL', blank=True)
    twitter = models.URLField('Twitter URL', blank=True)
    linedin = models.URLField('LinkedIn URL', blank=True)
    pinterest = models.URLField('Pinterest URL', blank=True)


    description = models.TextField('Description')
    information = models.TextField('Information')

    created_at = models.DateTimeField('Created At', auto_now_add=True,null=True)
    updated_at = models.DateTimeField('Updated At',auto_now=True,null=True)


    def __str__(self) -> str:
        return self.name
    


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


