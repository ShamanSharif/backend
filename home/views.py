


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








