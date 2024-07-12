from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from Core.models import Banner,Gallery_Image,Review,Enquiry,Partners,Event,Schools,Premium,Single,Double,Dealer,RegisterWarranty,RegisterComplaint,Testimonials,Blogs
from Frontpage.models import Visitor
import uuid
from django.contrib import messages

# Create your views here.

def update_visitors():
    key = str(uuid.uuid4().hex)[:8]
    Visitor.objects.create(Key=key)


def home(request):
    mobile_banners = Banner.objects.filter(Banner_Type='Mobile').order_by('-id')
    system_banners = Banner.objects.filter(Banner_Type='System').order_by('-id')
    images = Gallery_Image.objects.all().order_by('-id')[:6]
    reviews = Review.objects.all().order_by('-id')[:6]
    partners = Partners.objects.all().order_by('-id')
    events = Event.objects.all().order_by('-Date')[:3]
    schools = Schools.objects.all().order_by('-id')[:2]

    update_visitors()

    context = {
        'mobile_banners' : mobile_banners,
        'system_banners' : system_banners,
        'images' : images,
        'reviews' : reviews,
        'partners' : partners,
        'events' : events,
        'schools' : schools,
    }
    return render(request,'Frontpage/index.html',context)

def index(request):
    return render(request, 'Frontpage/indexpetra.html')

def about(request):
    reviews = Review.objects.all().order_by('-id')
    partners = Partners.objects.all().order_by('-id')

    context = {
        'reviews' : reviews,
        'partners' : partners
    }
    return render(request,'Frontpage/about.html',context)

def products(request):
    premiums = Premium.objects.all()
    singles = Single.objects.all().order_by('-id')
    doubles = Double.objects.all().order_by('-id')
    
    print(premiums)
    print(singles)
    print(doubles)
    
    context = {
        'premium' : premiums,
        'single' : singles,
        'double' : doubles
    }
    return render(request, 'Frontpage/products.html',context)


def product_detail(request, category, slug):
    if category == 'premium':
        product = get_object_or_404(Premium, slug=slug)
        suggest = Premium.objects.exclude(slug=slug)
    elif category == 'single':
        product = get_object_or_404(Single, slug=slug)
        suggest = Single.objects.exclude(slug=slug)
    elif category == 'double':
        product = get_object_or_404(Double, slug=slug)
        suggest = Double.objects.exclude(slug=slug)
    else:
        product = None
        suggest = None

    print("Product:", product)
    print("Suggestions:", suggest)

    return render(request, 'Frontpage/product_detail.html', {'product': product, 'suggest': suggest, 'category': category})

def findDealers(request):
    return render(request, 'Frontpage/findNearDealers.html')

def becomeDealer(request):
    return render(request, 'Frontpage/becomeAdealers.html')

def registerComplaint(request):
    return render(request, 'Frontpage/registerComplaint.html')

def registerwarranty(request):
    return render(request, 'Frontpage/registerwarranty.html')

def testimonials(request):
    return render(request, 'Frontpage/testimonials.html')

def blogs(request):
    return render(request, 'Frontpage/blogs.html')

@csrf_exempt
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        place = request.POST.get('place')
        mobile = request.POST.get('mobile')
        message = request.POST.get('message')

        try:
            Enquiry.objects.create(Name=name,Email=email,Place=place,Mobile=mobile,Message=message)
            messages.success(request, 'Your enquiry submitted successfully.')
            return redirect('contact')
        except:
            return JsonResponse({'status':'failed'})
    return render(request,'Frontpage/contact.html')

def events(request):
    events = Event.objects.all().order_by('-Date')

    context = {
        'events' : events
    }
    return render(request,'Frontpage/events.html',context)

def gallery(request):
    images = Gallery_Image.objects.all().order_by('-id')

    context = {
        'images' : images
    }
    return render(request,'Frontpage/gallery.html',context)

def packages(request):
    schools = Schools.objects.all().order_by('-id')

    context = {
        'schools' : schools
    }
    return render(request,'Frontpage/packages.html',context)

def rides(request):
    return render(request,'Frontpage/rides.html')

@csrf_exempt
def review(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        place = request.POST.get('place')
        description = request.POST.get('description')
        rating = request.POST.get('rating')

        try:
            Review.objects.create(Name=name,Place=place,Description=description,Rating=rating)
            # return JsonResponse({'status':'success'})
            messages.success(request,'Review Added Successfully ... !')
            return redirect('review')
        except:
            return JsonResponse({'status':'failed'})
        
    return render(request,'Frontpage/review.html')

@csrf_exempt
def becomeDealer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        contact_number = request.POST.get('contact_number')
        business = request.POST.get('business')
        address = request.POST.get('address')
        state = request.POST.get('state')
        district = request.POST.get('district')

        try:
            Dealer.objects.create(Name=name,Email=email,Contact_number=contact_number,Business=business,Address=address,State=state,District=district)
            messages.success(request,'Dealer Added Successfully ... !')
            return redirect('becomeDealer')
        except:
            return JsonResponse({'status':'failed'})
    return render(request,'Frontpage/becomeAdealers.html')

def findNearDealers(request):
    state = request.GET.get('state')
    district = request.GET.get('district')
    if state and district:
        dealers = Dealer.objects.filter(State=state, District=district)
    else:
        dealers = Dealer.objects.none()

    context = {
        'state': state,
        'district': district,
        'dealers': dealers
    }
    return render(request, 'Frontpage/findNearDealersResult.html', context)

@csrf_exempt
def registerWarranty(request):
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
                print("Success: Warranty registered successfully.")  # Debug statement
                return redirect('registerWarranty')
            except Exception as e:
                print(f"Exception: {e}")  # Debug statement
                return JsonResponse({'status': 'failed'}, f'An error occurred: {e}')

    print("Rendering registerWarranty.html")  # Debug statement
    return render(request, 'Frontpage/registerWarranty.html')

@csrf_exempt
def registerComplaint(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        address = request.POST.get('address')
        contact = request.POST.get('contact')
        warranty = request.POST.get('warranty')
        dealer = request.POST.get('dealer')
        description = request.POST.get('description')

        # Check if the warranty does not exist
        print(f"Checking for warranty: {warranty}")
        if not RegisterWarranty.objects.filter(Warranty=warranty).exists():
            messages.error(request, 'Warranty with this value does not exist.')
            print("Error: Warranty with this value does not exist.")
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
                print("Success: Complaint registered successfully.")
                return redirect('registerComplaint')
            except Exception as e:
                print(f"Exception: {e}")
                return JsonResponse({'status': 'failed', 'error': str(e)})

    print("Rendering registerComplaint.html")
    return render(request, 'Frontpage/registerComplaint.html')

def testimonials(request):
    videos = Testimonials.objects.all()
    
    context = {
        'videos' : videos,
    }
    return render(request, 'Frontpage/testimonials.html',context)

def gallery(request):
    images = Gallery_Image.objects.all()
    
    context = {
        'images' : images,
    }
    return render(request, 'Frontpage/gallery.html',context)

def blogs(request):
    blogs = Blogs.objects.all().order_by('-id')
    
    context = {
        'blogs' : blogs,
    }
    return render(request, 'Frontpage/blogs.html',context)

def blog_detail(request, category, slug):
    if category == 'blog':
        blog = get_object_or_404(Blogs, slug=slug)
    else:
        blog = None


    return render(request, 'Frontpage/blog_detail.html', {'blog': blog})