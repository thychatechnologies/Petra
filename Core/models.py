from django.db import models
from U_Auth.models import User
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.

BANNER_TYPES = [('Mobile','Mobile'),('System','System')]

class Banner(models.Model):
    Date = models.DateField(auto_now_add=True)
    Banner_Type = models.CharField(max_length=10,choices=BANNER_TYPES)
    Image = models.ImageField(null=True,upload_to='Banners')

class Gallery_Image(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Gallery')

class Partners(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Partners')

class Schools(models.Model):
    Date = models.DateField(auto_now_add=True)
    Image = models.ImageField(null=True,upload_to='Partners')

class Event(models.Model):
    Added_Date = models.DateField(auto_now_add=True)

    Name = models.CharField(max_length=100)
    Date = models.DateField()
    Start_Time = models.TimeField()
    End_Time = models.TimeField()
    Description = models.TextField()
    Image = models.ImageField(null=True,upload_to='Events')

    def __str__(self):
        return self.Name
    
class Review(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=100,null=True)
    Rating = models.IntegerField(default=0)
    Description = models.TextField()

class Enquiry(models.Model):
    Date = models.DateField(auto_now_add=True)
    Email = models.EmailField(max_length=100)
    Name = models.CharField(max_length=100)
    Place = models.CharField(max_length=100)
    Mobile = models.CharField(max_length=20,null=True)
    Message = models.TextField()

class Premium(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Premiums')
    Image2 = models.ImageField(null=True,upload_to='Premiums',blank=True)
    Image3 = models.ImageField(null=True,upload_to='Premiums',blank=True)
    Description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ['Name']
        verbose_name = 'premium'
        verbose_name_plural = 'premiums'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Name)
            slug = base_slug
            counter = 1
            while Premium.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=['premium', self.slug])
    
class PremiumSize(models.Model):
    premium = models.ForeignKey(Premium, on_delete=models.CASCADE, related_name='premium_sizes')
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size
    
class Single(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Singles')
    Image2 = models.ImageField(null=True,upload_to='Singles',blank=True)
    Image3 = models.ImageField(null=True,upload_to='Singles',blank=True)
    Description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ['Name']
        verbose_name = 'single'
        verbose_name_plural = 'singles'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Name)
            slug = base_slug
            counter = 1
            while Single.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=['single', self.slug])
    
class SingleSize(models.Model):
    single = models.ForeignKey(Single, on_delete=models.CASCADE, related_name='single_sizes')
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size
    
class Double(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Doubles')
    Image2 = models.ImageField(null=True,upload_to='Doubles',blank=True)
    Image3 = models.ImageField(null=True,upload_to='Singles',blank=True)
    Description = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ['Name']
        verbose_name = 'double'
        verbose_name_plural = 'doubles'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Name)
            slug = base_slug
            counter = 1
            while Double.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('product_detail', args=['double', self.slug])
    
class DoubleSize(models.Model):
    double = models.ForeignKey(Double, on_delete=models.CASCADE, related_name='double_sizes')
    size = models.CharField(max_length=50)

    def __str__(self):
        return self.size
    
class Dealer(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField()
    Contact_number = models.CharField(max_length=15)
    Business = models.CharField(max_length=100)
    Address = models.TextField(null=True,blank=True)
    State = models.CharField(max_length=50)
    District = models.CharField(max_length=50)
    
    def __str__(self):
        return self.Name
    
class RegisterWarranty(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Address = models.TextField(null=True,blank=True)
    Contact = models.CharField(max_length=15)
    Warranty = models.CharField(max_length=100,unique=True)
    Dealer = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.Name
    
class RegisterComplaint(models.Model):
    Date = models.DateField(auto_now_add=True)
    Name = models.CharField(max_length=100)
    Address = models.TextField(null=True,blank=True)
    Contact = models.CharField(max_length=15)
    Warranty = models.CharField(max_length=100,unique=True)
    Dealer = models.TextField(null=True,blank=True)
    Description = models.TextField(null=True,blank=True)
    
    def __str__(self):
        return self.Name
    
class Testimonials(models.Model):
    Date = models.DateField(auto_now_add=True)
    Link = models.CharField(max_length=300)
    
class Blogs(models.Model):
    Date = models.DateField(auto_now_add=True)
    Title = models.CharField(max_length=100)
    Image = models.ImageField(null=True,upload_to='Blogs')
    Description = models.TextField(null=True, blank=True)
    Content = models.TextField(null=True, blank=True)
    slug = models.SlugField(unique=True, blank=True)
    
    class Meta:
        ordering = ['Title']
        verbose_name = 'blog'
        verbose_name_plural = 'blogs'
    
    def save(self, *args, **kwargs):
        if not self.slug:
            base_slug = slugify(self.Title)
            slug = base_slug
            counter = 1
            while Blogs.objects.filter(slug=slug).exists():
                slug = f"{base_slug}-{counter}"
                counter += 1
            self.slug = slug
        super().save(*args, **kwargs)

    def get_url(self):
        return reverse('blog_detail', args=['blog', self.slug])