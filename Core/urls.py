from django.urls import path
from Core import views

urlpatterns = [
    path('',views.dashboard,name='dashboard'),
    path('banner/list/',views.manage_banners,name='manage-banners'),
    path('banner/add/',views.add_banner,name='add-banner'),
    path('banner/delete',views.delete_banner,name='delete-banner'),

    path('vlogs/manage/',views.manage_vlogs,name='manage-vlogs'),

    path('gallery/manage/',views.manage_gallery,name='manage-gallery'),
    path('gallery/images/add/',views.add_images,name='add-images'),
    path('gallery/image/delete/',views.delete_image,name='delete-image'),

    path('partner/manage/',views.manage_partners,name='manage-partners'),
    path('partner/add/',views.add_partners,name='add-partners'),
    path('partner/delete/',views.delete_partner,name='delete-partner'),

    path('school/manage/',views.manage_schools,name='manage-schools'),
    path('school/add/',views.add_schools,name='add-schools'),
    path('school/delete/',views.delete_school,name='delete-school'),

    path('events/manage/',views.manage_events,name='manage-events'),
    path('event/add/',views.add_event,name='add-event'),
    path('event/edit/<int:event_id>/',views.edit_event,name='edit-event'),
    path('event/delete/',views.delete_event,name='delete-event'),

    path('reviews/',views.manage_reviews,name='manage-reviews'),
    path('review/delete/',views.delete_review,name='delete-review'),
    path('enquiries/',views.enquiries,name='enquiries'),
    path('enquiry/delete/',views.delete_enquiry,name='delete-enquiry'),
    
    path('premium/list/',views.manage_premiums,name='manage-premiums'),
    path('premium/add/',views.add_premium,name='add-premium'),
    path('premium/delete/',views.delete_premium,name='delete-premium'),
    path('premium/edit/<int:premium_id>/',views.edit_premium,name='edit-premium'),
    path('premiumSize/delete/',views.delete_premiumSize,name='delete-premiumSize'),
    
    path('single/list/',views.manage_singles,name='manage-singles'),
    path('single/add/',views.add_single,name='add-single'),
    path('single/delete/',views.delete_single,name='delete-single'),
    path('single/edit/<int:single_id>/',views.edit_single,name='edit-single'),
    path('singleSize/delete/',views.delete_singleSize,name='delete-singleSize'),
    
    path('double/list/',views.manage_doubles,name='manage-doubles'),
    path('double/add/',views.add_double,name='add-double'),
    path('double/delete/',views.delete_double,name='delete-double'),
    path('double/edit/<int:double_id>/',views.edit_double,name='edit-double'),
    path('doubleSize/delete/',views.delete_doubleSize,name='delete-doubleSize'),
    
    path('dealer/list/',views.manage_dealers,name='manage-dealers'),
    path('dealer/add/',views.add_dealer,name='add-dealer'),
    path('dealer/delete/',views.delete_dealer,name='delete-dealer'),
    path('dealer/edit/<int:dealer_id>/',views.edit_dealer,name='edit-dealer'),
    
    path('warranty/list/',views.manage_warrantys,name='manage-warrantys'),
    path('warranty/add/',views.add_warranty,name='add-warranty'),
    path('warranty/delete/',views.delete_warranty,name='delete-warranty'),
    path('warranty/edit/<int:warranty_id>/',views.edit_warranty,name='edit-warranty'),
    
    path('complaint/list/',views.manage_complaints,name='manage-complaints'),
    path('complaint/add/',views.add_complaint,name='add-complaint'),
    path('complaint/delete/',views.delete_complaint,name='delete-complaint'),
    path('complaint/edit/<int:complaint_id>/',views.edit_complaint,name='edit-complaint'),
    
    path('testimonials/list/',views.manage_testimonials,name='manage-testimonials'),
    path('testimonials/add/',views.add_testimonials,name='add-testimonials'),
    path('testimonials/delete/',views.delete_testimonials,name='delete-testimonials'),
    
    path('blog/list/',views.manage_blogs,name='manage-blogs'),
    path('blog/add/',views.add_blog,name='add-blog'),
    path('blog/delete/',views.delete_blog,name='delete-blog'),
    path('blog/edit/<int:blog_id>/',views.edit_blog,name='edit-blog'),

]