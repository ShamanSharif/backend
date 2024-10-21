


from django.shortcuts import render
from .models import HeroSection,Accessory, Logo, NavbarItem, RepairService, RepairCategory, GoogleReview, Blog, FAQ

def index(request):
    hero_sections = HeroSection.objects.filter(active=True)  # Get all active hero sections
    accessories = Accessory.objects.all()
    logo = Logo.objects.first()
    navbar_items = NavbarItem.objects.all()
    repair_services = RepairService.objects.all()
    repair_categories = RepairCategory.objects.all()  # Add the repair_categories variable to the context for use in the template.
    # Fetch only reviews that are marked to be displayed on the website
    reviews = GoogleReview.objects.all()[:6]
    latest_blogs = Blog.objects.order_by('-date')[:3]
    faqs = FAQ.objects.all()
    context = {
        'hero_sections': hero_sections,
        'accessories': accessories, 
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services, # Update the context variable
        'repair_categories': repair_categories,  # Add the repair_categories variable to the context for use in the template.
        'reviews': reviews,
        'latest_blogs': latest_blogs,
        'faqs': faqs,  # Add the latest_faq variable to the context for use in the template.
    }
    return render(request, 'index.html', context)

from django.shortcuts import render, redirect
from .models import RepairRequest, Logo, NavbarItem, RepairService
from django.contrib import messages

def repair_page(request):
    # Add the necessary context data similar to the index view
    logo = Logo.objects.first()
    navbar_items = NavbarItem.objects.all()
    repair_services = RepairService.objects.all()
    
    if request.method == 'POST':
        # Extract form data from POST request
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        problems = ','.join(request.POST.getlist('problem'))  # List to comma-separated string
        description = request.POST.get('problemDispriction')
        service_method = request.POST.get('serviceReciveMethod')
        store_location = request.POST.get('store')
        preferred_date = request.POST.get('date')
        preferred_time = request.POST.get('time')
        contact_first_name = request.POST.get('customerFirstName')
        contact_last_name = request.POST.get('customerLastName')
        contact_email = request.POST.get('customerEmail')
        contact_phone = request.POST.get('customerPhone')

        # Save to database
        repair_request = RepairRequest.objects.create(
            brand=brand,
            model=model,
            problems=problems,
            description=description,
            service_method=service_method,
            store_location=store_location,
            preferred_date=preferred_date,
            preferred_time=preferred_time,
            contact_first_name=contact_first_name,
            contact_last_name=contact_last_name,
            contact_email=contact_email,
            contact_phone=contact_phone,
        )
        messages.success(request, 'Your repair request has been submitted successfully!')
        return redirect('repair_page')  # Redirect after saving
    
    # Add the context for rendering the repair page
    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
    }
    return render(request, 'repair.html', context)
