from django.contrib import admin
from Core.models import Banner,Gallery_Image,Partners,Event,Review,Enquiry,Schools,Premium,PremiumSize,Dealer,RegisterWarranty,RegisterComplaint,Blogs

# Register your models here.

@admin.register(Banner)
class BannerModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date','Banner_Type']

@admin.register(Gallery_Image)
class GalleryModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date']

@admin.register(Partners)
class PartnersModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date']

@admin.register(Schools)
class SchoolsModelAdmin(admin.ModelAdmin):
    list_display = ['Image','Date']

@admin.register(Event)
class EventModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Start_Time','End_Time']

@admin.register(Review)
class ReviewModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Place','Description']

@admin.register(Enquiry)
class EnquiryModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Mobile','Email','Message','Place']
    
class PremiumSizeInline(admin.TabularInline):
    model = PremiumSize
    extra = 1
    
@admin.register(Premium)
class PremiumModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Image']
    inlines = [PremiumSizeInline]
    
@admin.register(Dealer)
class DealerModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Email','Contact_number','Business','District','State']
    
@admin.register(RegisterWarranty)
class RegisterWarrantyModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Contact','Address','Warranty','Dealer']
    
@admin.register(RegisterComplaint)
class RegisterComplaintModelAdmin(admin.ModelAdmin):
    list_display = ['Name','Date','Contact','Address','Warranty','Dealer','Description']
    
@admin.register(Blogs)
class BlogModelAdmin(admin.ModelAdmin):
    list_display = ['Title','Date','Image','Description']