from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from Core.models import Banner,Gallery_Image,Partners,Event,Review,Enquiry,Schools,Premium,Single,Double,PremiumSize,SingleSize,DoubleSize,Dealer,RegisterWarranty,RegisterComplaint,Testimonials,Blogs
from django.contrib import messages
from Core.reuse import resize
from Frontpage.models import Visitor

# Create your views here.

#----------------------------------- DASHBOARD -----------------------------------#

@login_required
def dashboard(request):
    page = 'dashboard'
    enquiries = Enquiry.objects.all().order_by('-id')[:10]
    images = Gallery_Image.objects.all().count()
    events = Event.objects.all().count()
    reviews = Review.objects.all().count()
    visitors = Visitor.objects.all().count()

    context = {
        'page' : page,
        'enquiries' : enquiries,
        'images' : images,
        'events' : events,
        'reviews' : reviews,
        'visitors' : visitors,
    }
    return render(request,'Dashboard/Core/dashboard.html',context)

#----------------------------------- Banners -----------------------------------#

@login_required
def manage_banners(request):
    banners = Banner.objects.all().order_by('-id')

    context = {
        "banners" : banners
    }
    return render(request,'Dashboard/Banners/banners.html',context)

#----------------------------------- Add Banner -----------------------------------#

@login_required
def add_banner(request):
    if request.method == 'POST':
        banner_type = request.POST.get('type')
        image = request.FILES.get('image')

        try:
            # resized = resize(image,800)
            Banner.objects.create(Banner_Type=banner_type, Image=image)

            messages.success(request, 'New banner added successfully ...!')
            return redirect('manage-banners')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-banner')

    return render(request, 'Dashboard/Banners/banner-add.html')

#----------------------------------- Delete Banner -----------------------------------#

@login_required
def delete_banner(request):
    banner_id = request.POST.get('banner_id')
    banner = Banner.objects.get(id=banner_id)
    banner.delete()
    return redirect('manage-banners')

#----------------------------------- Vlogs -----------------------------------#

@login_required
def manage_vlogs(request):
    return render(request,'Dashboard/Vlogs/vlogs.html')

#----------------------------------- Gallery -----------------------------------#

@login_required
def manage_gallery(request):
    images = Gallery_Image.objects.all().order_by('-id')

    context = {
        'images' : images
    }
    return render(request,'Dashboard/Gallery/images.html',context)

#----------------------------------- Add Images -----------------------------------#

@login_required
def add_images(request):
    if request.method == 'POST':
        images = request.FILES.getlist('images')

        for image in images:
            # resized = resize(image,800)
            try:
                Gallery_Image.objects.create(Image=image)
            except Exception as exception:
                messages.warning(request,exception)
                return redirect('image-gallery')
        messages.success(request,'New images added successfully ... !')
        return redirect('manage-gallery')
    
#----------------------------------- Delete Image -----------------------------------#

@login_required
def delete_image(request):
    image_id = request.POST.get('image_id')
    image = Gallery_Image.objects.get(id=image_id)
    image.delete()
    messages.warning(request,'Image Deleted ... !')
    return redirect('manage-gallery')

#----------------------------------- Partners -----------------------------------#

@login_required
def manage_partners(request):
    partners = Partners.objects.all().order_by('-id')

    context = {
        'partners' : partners
    }
    return render(request,'Dashboard/Gallery/partners.html',context)

#----------------------------------- Add Partners -----------------------------------#

@login_required
def add_partners(request):
    if request.method == 'POST':
        partners = request.FILES.getlist('partners')

        for partner in partners:
            # resized = resize(partner,300)
            Partners.objects.create(Image=partner)

        messages.success(request,'New partners added successfully ... !')
        return redirect('manage-partners')
    
#----------------------------------- Delete Partner -----------------------------------#

@login_required
def delete_partner(request):
    partner_id = request.POST.get('partner_id')
    partner = Partners.objects.get(id=partner_id)
    partner.delete()
    messages.warning(request,'Partner Deleted ... !')
    return redirect('manage-partners')

#----------------------------------- Manage Events -----------------------------------#

@login_required
def manage_events(request):
    events = Event.objects.all().order_by('-Date')

    context = {
        'events':events
    }
    return render(request,'Dashboard/Events/events.html',context)

#----------------------------------- Add Event -----------------------------------#

@login_required
def add_event(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        start = request.POST.get('start')
        end = request.POST.get('end')
        image = request.FILES.get('image')
        description = request.POST.get('description')

        try:
            Event.objects.create(Name=name,Date=date,Start_Time=start,End_Time=end,Image=image,Description=description)
            messages.success(request,'New event added successfully ... !')
            return redirect('manage-events')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('event-add')

    return render(request,'Dashboard/Events/event-add.html')

#----------------------------------- Edit Event -----------------------------------#

@login_required
def edit_event(request,event_id):
    event = Event.objects.get(id=event_id)

    if request.method == 'POST':
        try:
            if len(request.FILES) > 0:
                event.Image = request.FILES.get('image')

            event.Name = request.POST.get('name')
            event.Date = request.POST.get('date')
            event.Start_Time = request.POST.get('start')
            event.End_Time = request.POST.get('end')
            event.Description = request.POST.get('description') 
            event.save()
            messages.success(request,'Event details edited successfully ... !')
            return redirect('manage-events')
        except Exception as exception:
            messages.warning(request,exception)
            return redirect('edit-event',event_id=event.id)
        
    context = {
        'event' : event
    }
    return render(request,'Dashboard/Events/event-edit.html',context)

#----------------------------------- Delete Event -----------------------------------#

@login_required
def delete_event(request):
    event_id = request.POST.get('event_id')
    event = Event.objects.get(id=event_id)
    event.delete()
    return redirect('manage-events')

#----------------------------------- Reviews -----------------------------------#

@login_required
def manage_reviews(request):
    reviews = Review.objects.all().order_by('-id')

    context = {
        'reviews' : reviews
    }
    return render(request,'Dashboard/Core/reviews.html',context)

#----------------------------------- Delete Reviews -----------------------------------#

@login_required
def delete_review(request):
    if request.method == 'POST':
        review_id = request.POST.get('review_id')
        review = Review.objects.get(id=review_id)
        review.delete()
        return redirect('manage-reviews')

#----------------------------------- Enquiries -----------------------------------#

@login_required
def enquiries(request):
    enquiries = Enquiry.objects.all().order_by('-id')

    context = {
        'enquiries' : enquiries
    }
    return render(request,'Dashboard/Core/enquiries.html',context)

#----------------------------------- Delete Enquiry -----------------------------------#

@login_required
def delete_enquiry(request):
    if request.method == 'POST':
        enquiry_id = request.POST.get('enquiry_id')
        enquiry = Enquiry.objects.get(id=enquiry_id)
        enquiry.delete()
        return redirect('enquiries')
    
#----------------------------------- Happy Schools -----------------------------------#

@login_required
def manage_schools(request):
    schools = Schools.objects.all().order_by('-id')

    context = {
        'images' : schools
    }
    return render(request,'Dashboard/Gallery/schools.html',context)

#----------------------------------- Add Partners -----------------------------------#

@login_required
def add_schools(request):
    if request.method == 'POST':
        schools = request.FILES.getlist('images')

        for school in schools:
            # resized = resize(school,800)
            Schools.objects.create(Image=school)

        messages.success(request,'New schools added successfully ... !')
        return redirect('manage-schools')
    
#----------------------------------- Delete Partner -----------------------------------#

@login_required
def delete_school(request):
    school_id = request.POST.get('image_id')
    school = Schools.objects.get(id=school_id)
    school.delete()
    messages.warning(request,'school Deleted ... !')
    return redirect('manage-schools')

#----------------------------------- Manage Premiums -----------------------------------#

@login_required
def manage_premiums(request):
    premiums = Premium.objects.all().order_by('-Date')

    context = {
        'premiums': premiums
    }
    return render(request,'Dashboard/Premiums/premiums.html',context)

#----------------------------------- Add Premium -----------------------------------#

@login_required
def add_premium(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        desc = request.POST.get('desc')
        sizes = request.POST.getlist('sizes')

        try:
            # resized = resize(image,800)
            premium = Premium.objects.create(Name=name, Image=image, Image2=image2, Image3=image3, Description=desc)
            
            for size in sizes:
                PremiumSize.objects.create(premium=premium, size=size)

            messages.success(request, 'New Door added successfully ...!')
            return redirect('manage-premiums')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-premium')

    return render(request, 'Dashboard/Premiums/premium-add.html')

#----------------------------------- Delete Premium -----------------------------------#

@login_required
def delete_premium(request):
    premium_id = request.POST.get('premium_id')
    premium = Premium.objects.get(id=premium_id)
    premium.delete()
    return redirect('manage-premiums')

@login_required
def delete_premiumSize(request):
    premiumSize_id = request.POST.get('premiumSize_id')
    premiumSize = PremiumSize.objects.get(id=premiumSize_id)
    premiumSize.delete()
    return redirect('edit-premium', premium_id=premiumSize.premium.id)


#----------------------------------- Edit Premium -----------------------------------#

@login_required
def edit_premium(request, premium_id):
    premium = Premium.objects.get(id=premium_id)

    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                premium.Image = request.FILES.get('image')

            if 'image2' in request.FILES:
                premium.Image2 = request.FILES.get('image2')
                
            if 'image3' in request.FILES:
                premium.Image3 = request.FILES.get('image3')

            premium.Name = request.POST.get('name')
            premium.Description = request.POST.get('description')
            premium.save()
            
            sizes = request.POST.getlist('sizes')
            PremiumSize.objects.filter(premium=premium).delete()
            for size in sizes:
                PremiumSize.objects.create(premium=premium, size=size)
                
            messages.success(request, 'Premium details edited successfully!')
            return redirect('manage-premiums')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-premium', premium_id=premium.id)
        
    context = {
        'premium': premium,
        'sizes': PremiumSize.objects.filter(premium=premium)
    }
    return render(request, 'Dashboard/Premiums/premium-edit.html', context)

#----------------------------------- Manage Singles -----------------------------------#

@login_required
def manage_singles(request):
    singles = Single.objects.all().order_by('-Date')

    context = {
        'singles': singles
    }
    return render(request,'Dashboard/Singles/singles.html',context)

#----------------------------------- Add Single -----------------------------------#

@login_required
def add_single(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        desc = request.POST.get('desc')
        sizes = request.POST.getlist('sizes')

        try:
            # resized = resize(image,800)
            single = Single.objects.create(Name=name, Image=image, Image2=image2, Image3=image3, Description=desc)
            
            for size in sizes:
                SingleSize.objects.create(single=single, size=size)

            messages.success(request, 'New Door added successfully ...!')
            return redirect('manage-singles')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-single')

    return render(request, 'Dashboard/Singles/single-add.html')

#----------------------------------- Delete Single -----------------------------------#

@login_required
def delete_single(request):
    single_id = request.POST.get('single_id')
    single = Premium.objects.get(id=single_id)
    single.delete()
    return redirect('manage-singles')

@login_required
def delete_singleSize(request):
    singleSize_id = request.POST.get('singleSize_id')
    singleSize = SingleSize.objects.get(id=singleSize_id)
    singleSize.delete()
    return redirect('edit-single', single_id=singleSize.single.id)

#----------------------------------- Edit Single -----------------------------------#

@login_required
def edit_single(request, single_id):
    single = Single.objects.get(id=single_id)

    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                single.Image = request.FILES.get('image')

            if 'image2' in request.FILES:
                single.Image2 = request.FILES.get('image2')
                
            if 'image3' in request.FILES:
                single.Image3 = request.FILES.get('image3')

            single.Name = request.POST.get('name')
            single.Description = request.POST.get('description')
            single.save()
            
            sizes = request.POST.getlist('sizes')
            SingleSize.objects.filter(single=single).delete()
            for size in sizes:
                SingleSize.objects.create(single=single, size=size)
                
            messages.success(request, 'Single details edited successfully!')
            return redirect('manage-singles')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-single', single_id=single.id)
        
    context = {
        'single': single,
        'sizes': SingleSize.objects.filter(single=single)
    }
    return render(request, 'Dashboard/Singles/single-edit.html', context)

#----------------------------------- Manage Doubles -----------------------------------#

@login_required
def manage_doubles(request):
    doubles = Double.objects.all().order_by('-Date')

    context = {
        'doubles': doubles
    }
    return render(request,'Dashboard/Doubles/doubles.html',context)

#----------------------------------- Add Double -----------------------------------#

@login_required
def add_double(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        image = request.FILES.get('image')
        image2 = request.FILES.get('image2')
        image3 = request.FILES.get('image3')
        desc = request.POST.get('desc')
        sizes = request.POST.getlist('sizes')

        try:
            # resized = resize(image,800)
            double = Double.objects.create(Name=name, Image=image, Image2=image2, Image3=image3, Description=desc)
            
            for size in sizes:
                DoubleSize.objects.create(double=double, size=size)

            messages.success(request, 'New Door added successfully ...!')
            return redirect('manage-doubles')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-double')

    return render(request, 'Dashboard/Doubles/double-add.html')

#----------------------------------- Delete Double -----------------------------------#

@login_required
def delete_double(request):
    double_id = request.POST.get('double_id')
    double = Double.objects.get(id=double_id)
    double.delete()
    return redirect('manage-doubles')

@login_required
def delete_doubleSize(request):
    doubleSize_id = request.POST.get('doubleSize_id')
    doubleSize = DoubleSize.objects.get(id=doubleSize_id)
    doubleSize.delete()
    return redirect('edit-double', double_id=doubleSize.double.id)

#----------------------------------- Edit Double -----------------------------------#

@login_required
def edit_double(request, double_id):
    double = Double.objects.get(id=double_id)

    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                double.Image = request.FILES.get('image')

            if 'image2' in request.FILES:
                double.Image2 = request.FILES.get('image2')
                
            if 'image3' in request.FILES:
                double.Image3 = request.FILES.get('image3')

            double.Name = request.POST.get('name')
            double.Description = request.POST.get('description')
            double.save()
            
            sizes = request.POST.getlist('sizes')
            DoubleSize.objects.filter(double=double).delete()
            for size in sizes:
                DoubleSize.objects.create(double=double, size=size)
                
            messages.success(request, 'Double details edited successfully!')
            return redirect('manage-doubles')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-double', double_id=double.id)
        
    context = {
        'double': double,
        'sizes': DoubleSize.objects.filter(double=double)
    }
    return render(request, 'Dashboard/Doubles/double-edit.html', context)

#----------------------------------- Manage Dealers -----------------------------------#

@login_required
def manage_dealers(request):
    dealers = Dealer.objects.all().order_by('-Date')

    context = {
        'dealers': dealers
    }
    return render(request,'Dashboard/Dealers/dealers.html',context)

#----------------------------------- Add Dealers -----------------------------------#

@login_required
def add_dealer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        business = request.POST.get('business')
        address = request.POST.get('address')
        state = request.POST.get('state')
        district = request.POST.get('district') 

        try:
            # resized = resize(image,800)
            Dealer.objects.create(Name=name,Email=email,Contact_number=contact_number,Business=business,Address=address,State=state,District=district)

            messages.success(request, 'New Dealer Added Successfully ...!')
            return redirect('manage-dealers')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-dealer')

    return render(request, 'Dashboard/Dealers/dealer-add.html')

#----------------------------------- Delete Dealers -----------------------------------#

@login_required
def delete_dealer(request):
    dealer_id = request.POST.get('dealer_id')
    dealer = Dealer.objects.get(id=dealer_id)
    dealer.delete()
    return redirect('manage-dealers')

#----------------------------------- Edit Dealers -----------------------------------#

@login_required
def edit_dealer(request, dealer_id):
    dealer = Dealer.objects.get(id=dealer_id)

    if request.method == 'POST':
        try:
            dealer.Name = request.POST.get('name')
            dealer.Email = request.POST.get('email')
            dealer.Contact_number = request.POST.get('contact_number')
            dealer.Business = request.POST.get('business')
            dealer.State = request.POST.get('state')
            dealer.District = request.POST.get('district')
            dealer.save()
            
                
            messages.success(request, 'Dealer details edited successfully!')
            return redirect('manage-dealers')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-dealer', dealer_id=dealer.id)
        
    context = {
        'dealer': dealer,
    }
    return render(request, 'Dashboard/Dealers/dealer-edit.html', context)

#----------------------------------- Manage Warrantys -----------------------------------#

@login_required
def manage_warrantys(request):
    warrantys = RegisterWarranty.objects.all().order_by('-Date')

    context = {
        'warrantys': warrantys
    }
    return render(request,'Dashboard/Warrantys/warrantys.html',context)

#----------------------------------- Add Warranty -----------------------------------#

@login_required
def add_warranty(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        warranty = request.POST.get('warranty')
        dealer = request.POST.get('dealer')

        if RegisterWarranty.objects.filter(Warranty=warranty).exists():
            messages.error(request, 'Warranty with this value already exists.')
            print("Error: Warranty with this value already exists.")  # Debug statement
        else:
            try:
                RegisterWarranty.objects.create(
                    Name=name,
                    Address=address,
                    Contact=contact,
                    Warranty=warranty,
                    Dealer=dealer
                )
                messages.success(request, 'Warranty registered successfully.')
                return redirect('manage-warrantys')
            except Exception as exception:
                messages.warning(request, f'Error: {exception}')
                return redirect('add-warranty')

    return render(request, 'Dashboard/Warrantys/warranty-add.html')

#----------------------------------- Delete Warranty -----------------------------------#

@login_required
def delete_warranty(request):
    warranty_id = request.POST.get('warranty_id')
    warranty = RegisterWarranty.objects.get(id=warranty_id)
    warranty.delete()
    return redirect('manage-warrantys')

#----------------------------------- Edit Warranty -----------------------------------#

@login_required
def edit_warranty(request, warranty_id):
    warranty = RegisterWarranty.objects.get(id=warranty_id)

    if request.method == 'POST':
        try:
            warranty.Name = request.POST.get('name')
            warranty.Address = request.POST.get('address')
            warranty.Contact = request.POST.get('contact')
            warranty.Warranty = request.POST.get('warranty')
            warranty.Dealer = request.POST.get('dealer')
            warranty.save()
            
                
            messages.success(request, 'Warranty details edited successfully!')
            return redirect('manage-warrantys')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-warranty', warranty_id=warranty.id)
        
    context = {
        'warranty': warranty,
    }
    return render(request, 'Dashboard/Warrantys/warranty-edit.html', context)

#----------------------------------- Manage Complaints -----------------------------------#

@login_required
def manage_complaints(request):
    complaints = RegisterComplaint.objects.all().order_by('-Date')

    context = {
        'complaints': complaints
    }
    return render(request,'Dashboard/Complaints/complaints.html',context)

#----------------------------------- Add Complaint -----------------------------------#

@login_required
def add_complaint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        warranty = request.POST.get('warranty')
        dealer = request.POST.get('dealer')
        description = request.POST.get('description')

        if not RegisterWarranty.objects.filter(Warranty=warranty).exists():
            messages.error(request, 'Warranty with this value does not exist.')
            print("Error: Warranty with this value already exists.")  # Debug statement
        else:
            try:
                RegisterComplaint.objects.create(
                    Name=name,
                    Address=address,
                    Contact=contact,
                    Warranty=warranty,
                    Dealer=dealer,
                    Description=description
                )
                messages.success(request, 'Complaint registered successfully.')
                return redirect('manage-complaints')
            except Exception as exception:
                messages.warning(request, f'Error: {exception}')
                return redirect('add-complaint')

    return render(request, 'Dashboard/Complaints/complaint-add.html')

#----------------------------------- Delete Complaint -----------------------------------#

@login_required
def delete_complaint(request):
    complaint_id = request.POST.get('complaint_id')
    complaint = RegisterComplaint.objects.get(id=complaint_id)
    complaint.delete()
    return redirect('manage-complaints')

#----------------------------------- Edit Complaint -----------------------------------#

@login_required
def edit_complaint(request, complaint_id):
    complaint = RegisterComplaint.objects.get(id=complaint_id)

    if request.method == 'POST':
        try:
            complaint.Name = request.POST.get('name')
            complaint.Address = request.POST.get('address')
            complaint.Contact = request.POST.get('contact')
            complaint.Warranty = request.POST.get('warranty')
            complaint.Dealer = request.POST.get('dealer')
            complaint.Description = request.POST.get('description')

            complaint.save()
            
                
            messages.success(request, 'Complaint details edited successfully!')
            return redirect('manage-complaints')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-complaint', complaint_id=complaint.id)
        
    context = {
        'complaint': complaint,
    }
    return render(request, 'Dashboard/Complaints/complaint-edit.html', context)

#----------------------------------- testimonials -----------------------------------#

@login_required
def manage_testimonials(request):
    links = Testimonials.objects.all().order_by('-id')

    context = {
        'links' : links
    }
    return render(request,'Dashboard/Gallery/testimonials.html',context)

#----------------------------------- Add Testimonials -----------------------------------#

@login_required
def add_testimonials(request):
    if request.method == 'POST':
        link = request.POST.get('link') 
        try:
            # resized = resize(image,800)
            Testimonials.objects.create(Link=link)

            messages.success(request, 'New Testimonials Added Successfully ...!')
            return redirect('manage-testimonials')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-testimonials')

    return render(request, 'Dashboard/Gallery/testimonials-add.html')
    
#----------------------------------- Delete Testimonials -----------------------------------#

@login_required
def delete_testimonials(request):
    testimonial_id = request.POST.get('testimonial_id')
    link = Testimonials.objects.get(id=testimonial_id)
    link.delete()
    messages.warning(request,'Testimonial Deleted ... !')
    return redirect('manage-testimonials')

#----------------------------------- Manage Blogs -----------------------------------#

@login_required
def manage_blogs(request):
    blogs = Blogs.objects.all().order_by('-Date')

    context = {
        'blogs': blogs
    }
    return render(request,'Dashboard/Blogs/blogs.html',context)

#----------------------------------- Add Blogs -----------------------------------#

@login_required
def add_blog(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')
        desc = request.POST.get('desc')
        content = request.POST.get('content')
        

        try:
            # resized = resize(image,800)
            blog = Blogs.objects.create(Title=title, Image=image, Description=desc,Content=content)

            messages.success(request, 'New blog added successfully ...!')
            return redirect('manage-blogs')
        except Exception as exception:
            messages.warning(request, f'Error: {exception}')
            return redirect('add-blog')

    return render(request, 'Dashboard/Blogs/blog-add.html')

#----------------------------------- Delete Blog -----------------------------------#

@login_required
def delete_blog(request):
    blog_id = request.POST.get('blog_id')
    blog = Blogs.objects.get(id=blog_id)
    blog.delete()
    return redirect('manage-blogs')


#----------------------------------- Edit Blogs -----------------------------------#

@login_required
def edit_blog(request, blog_id):
    blog = Blogs.objects.get(id=blog_id)

    if request.method == 'POST':
        try:
            if 'image' in request.FILES:
                blog.Image = request.FILES.get('image')

            blog.Title = request.POST.get('title')
            blog.Description = request.POST.get('desc')
            blog.Content = request.POST.get('content')
            blog.save()
                
            messages.success(request, 'Blog details edited successfully!')
            return redirect('manage-blogs')
        except Exception as exception:
            messages.warning(request, exception)
            return redirect('edit-blog', blog_id=blog.id)
        
    context = {
        'blog': blog,
    }
    return render(request, 'Dashboard/Blogs/blog-edit.html', context)