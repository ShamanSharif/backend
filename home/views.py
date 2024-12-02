


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




from django.shortcuts import render, redirect
from .models import SellDevice, Logo, NavbarItem, RepairService
from django.contrib import messages

def sell_device(request):
    logo = Logo.objects.first()  # Get the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Get all navbar items
    repair_services = RepairService.objects.all()  # Get the repair services for the dropdown
    
    if request.method == 'POST':
        # Get form data from POST request
        device_type = request.POST.get('type')
        brand = request.POST.get('brand')
        model = request.POST.get('model')
        description = request.POST.get('deviceDispriction')
        customer_first_name = request.POST.get('customerFirstName')
        customer_last_name = request.POST.get('customerLastName')
        customer_email = request.POST.get('customerEmail')
        customer_phone = request.POST.get('customerPhone')
        device_images = request.FILES.get('deviceImages')  # Handle file upload

        # Save the data to the SellDevice model
        sell_device = SellDevice.objects.create(
            type=device_type,
            brand=brand,
            model=model,
            description=description,
            customer_first_name=customer_first_name,
            customer_last_name=customer_last_name,
            customer_email=customer_email,
            customer_phone=customer_phone,
            device_images=device_images,  # Save the uploaded image
        )
        messages.success(request, 'Your device has been submitted for sale!')
        return redirect('sell_device')  # Redirect after saving
    
    # Add the context for rendering the navbar and sell page
    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
    }
    return render(request, 'sell.html', context)





from django.shortcuts import render
from .models import Logo, NavbarItem, RepairService

def terms_conditions(request):
    logo = Logo.objects.first()  # Get the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Get all navbar items
    repair_services = RepairService.objects.all()  # Get the repair services for the dropdown

    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
    }
    
    return render(request, 'termsConditions.html', context)



from django.shortcuts import render
from .models import Logo, NavbarItem, RepairService

def privacy_policy(request):
    logo = Logo.objects.first()  # Get the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Get all navbar items
    repair_services = RepairService.objects.all()  # Get the repair services for the dropdown

    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
    }
    
    return render(request, 'privacyPolicy.html', context)







from django.shortcuts import render, redirect
from django.contrib import messages
# Import FranchiseApplication model
from .models import FranchiseApplication, Logo, NavbarItem, RepairService

def franchise_view(request):
    logo = Logo.objects.first()  # Fetch the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Fetch all navbar items
    repair_services = RepairService.objects.all()  # Fetch the repair services for the dropdown

    if request.method == 'POST':
        # Get form data
        first_name = request.POST.get('franchiseApplicantFirstName')
        last_name = request.POST.get('franchiseApplicantLastName')
        email = request.POST.get('franchiseApplicantEmail')
        phone_number = request.POST.get('franchiseApplicantPhone')
        street_address = request.POST.get('franchiseApplicantStreetAddress')
        about_applicant = request.POST.get('aboutFranchiseApplicant')

        # Save the data to the database
        franchise_application = FranchiseApplication.objects.create(
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            street_address=street_address,
            about_applicant=about_applicant,
        )
        
        # Success message and redirect after saving
        messages.success(request, 'Your franchise application has been submitted successfully!')
        return redirect('franchise')  # Redirect to avoid resubmission on page refresh

    # Pass the context to the template
    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
    }

    return render(request, 'franchise.html', context)



from django.shortcuts import render, get_object_or_404, redirect
from .models import JobOpening, JobApplication
from django.contrib import messages

def career_view(request):
    job_openings = JobOpening.objects.all()  # Fetch all job openings
    logo = Logo.objects.first()  # Fetch the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Fetch all navbar items
    repair_services = RepairService.objects.all()  # Fetch the repair services for the dropdown
    context = {
        'job_openings': job_openings,
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
    }
    return render(request, 'career.html', context)

def apply_for_job(request, job_id):
    job = get_object_or_404(JobOpening, id=job_id)
    
    if request.method == 'POST':
        first_name = request.POST.get('applicantFirstName')
        last_name = request.POST.get('applicantLastName')
        email = request.POST.get('applicantEmail')
        phone_number = request.POST.get('applicantNumber')
        message = request.POST.get('applicantMassage')
        resume = request.FILES.get('applicantCV')
        
        # Save application to the database
        JobApplication.objects.create(
            job=job,
            first_name=first_name,
            last_name=last_name,
            email=email,
            phone_number=phone_number,
            message=message,
            resume=resume
        )

        messages.success(request, 'Your application has been submitted successfully!')
        return redirect('career')  # Redirect to the career page after submission

    context = {'job': job}
    return render(request, 'career.html', context)




from django.shortcuts import render
from .models import Logo, NavbarItem, RepairService  # Import your models as needed

def contact_page(request):
    logo = Logo.objects.first()  # Get the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Get all navbar items
    repair_services = RepairService.objects.all()  # Get the repair services for the dropdown (if needed)

    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,  # Optional: Include if needed for dropdowns
    }

    return render(request, 'contact.html', context)





from django.shortcuts import render
from .models import Logo, NavbarItem, RepairService, Blog

def blogs_page(request):
    logo = Logo.objects.first()  # Fetch the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Fetch all navbar items
    repair_services = RepairService.objects.all()  # Fetch repair services (if needed for the navbar dropdown)
    blogs = Blog.objects.all()  # Fetch all blogs

    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,  # Optional for dropdown
        'blogs': blogs,  # Fetch blogs dynamically
    }

    return render(request, 'blogs.html', context)


from django.shortcuts import render, get_object_or_404
from .models import Blog, Logo, NavbarItem, RepairService

def blog_detail(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    
    # Fetch the logo, navbar items, and repair services for the navbar
    logo = Logo.objects.first()
    navbar_items = NavbarItem.objects.all()
    repair_services = RepairService.objects.all()

    context = {
        'blog': blog,
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,  # Include repair services for the dropdown
    }

    return render(request, 'blog_detail.html', context)


from django.shortcuts import render, get_object_or_404, redirect
from .models import Accessory, Logo, NavbarItem, RepairService, Order
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from decimal import Decimal



# View to display all products with filters
def products_view(request):
    logo = Logo.objects.first()  # Get the logo for the navbar
    navbar_items = NavbarItem.objects.all()  # Get all navbar items
    repair_services = RepairService.objects.all()  # Get the repair services for the dropdown
    accessories = Accessory.objects.all()  # Get all accessories by default

    # Handle search query
    query = request.GET.get('query')
    if query:
        accessories = accessories.filter(name__icontains=query)

    # Handle price range filter
    max_price = request.GET.get('maxPrice')
    if max_price:
        accessories = accessories.filter(price__lte=max_price)

    # Handle category filter
    category = request.GET.get('productsCategory')
    if category and category != 'all':
        accessories = accessories.filter(category=category)

    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
        'accessories': accessories,
        'selected_category': category or 'all',  # Store selected category
        'selected_max_price': max_price or 194,  # Default max price
        'search_query': query or '',
    }
    
    return render(request, 'products.html', context)

def product_details(request, product_id):
    logo = Logo.objects.first()
    navbar_items = NavbarItem.objects.all()
    repair_services = RepairService.objects.all()
    accessory = get_object_or_404(Accessory, id=product_id)

    # Add the product to the session's cart
    cart = request.session.get('cart', [])
    if product_id not in cart:
        cart.append(product_id)
        request.session['cart'] = cart

    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
        'accessory': accessory,
    }

    return render(request, 'productDetails.html', context)






# from django.shortcuts import render, redirect
# from .models import Accessory, Logo, NavbarItem, RepairService

# def cart_view(request):
#     logo = Logo.objects.first()
#     navbar_items = NavbarItem.objects.all()
#     repair_services = RepairService.objects.all()

#     # Retrieve cart item IDs from the session
#     cart = request.session.get('cart', [])
#     accessories_in_cart = Accessory.objects.filter(id__in=cart)

#     # Calculate subtotal
#     subtotal = sum(item.price for item in accessories_in_cart)

#     context = {
#         'logo': logo,
#         'navbar_items': navbar_items,
#         'repair_services': repair_services,
#         'accessories_in_cart': accessories_in_cart,
#         'subtotal': subtotal,
#         'delivery_charge': 45,  # Example fixed delivery charge
#     }
#     return render(request, 'cart.html', context)



from django.shortcuts import render
from .models import Logo, NavbarItem, RepairService, Accessory

def cart_view(request):
    logo = Logo.objects.first()
    navbar_items = NavbarItem.objects.all()
    repair_services = RepairService.objects.all()
    
    cart = request.session.get('cart', {})
    accessories_in_cart = Accessory.objects.filter(id__in=cart.keys())

    items = []
    subtotal = 0
    for accessory in accessories_in_cart:
        quantity = cart[str(accessory.id)]
        total_price = accessory.price * quantity
        items.append({
            'accessory': accessory,
            'quantity': quantity,
            'total_price': total_price,
        })
        subtotal += total_price

    delivery_charge = 45
    total = subtotal + delivery_charge

    context = {
        'logo': logo,
        'navbar_items': navbar_items,
        'repair_services': repair_services,
        'accessories_in_cart': items,
        'subtotal': subtotal,
        'delivery_charge': delivery_charge,
        'total': total,
    }
    return render(request, 'cart.html', context)





# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', [])
#     if product_id not in cart:
#         cart.append(product_id)
#         request.session['cart'] = cart
#     return redirect('view_cart')


# def add_to_cart(request, accessory_id):
#     # Get the cart from the session, or initialize it as an empty dictionary if it doesn't exist
#     cart = request.session.get('cart', {})

#     # Check if the accessory ID is already in the cart
#     if str(accessory_id) in cart:
#         # If it's already in the cart, increase the quantity
#         cart[str(accessory_id)] += 1
#     else:
#         # If it's not in the cart, add it with a quantity of 1
#         cart[str(accessory_id)] = 1

#     # Save the cart back to the session
#     request.session['cart'] = cart
#     request.session.modified = True

#     return redirect('view_cart')

def add_to_cart(request, product_id):
    quantity = int(request.POST.get('quantity', 1))  # Get quantity from form input
    cart = request.session.get('cart', {})
    if str(product_id) in cart:
        cart[str(product_id)] += quantity  # Add the specified quantity
    else:
        cart[str(product_id)] = quantity  # Set initial quantity
    request.session['cart'] = cart
    return redirect('view_cart')




from django.http import JsonResponse

def remove_from_cart(request, product_id):
    # Get the cart from the session
    cart = request.session.get('cart', [])
    
    # Remove the product if it's in the cart
    if product_id in cart:
        cart.remove(product_id)
        request.session['cart'] = cart  # Save the updated cart back to the session
    
    return JsonResponse({'success': True})

from django.views.decorators.http import require_POST
from django.shortcuts import redirect
from django.contrib import messages
from .models import Accessory, Order
from decimal import Decimal

@require_POST
def confirm_order(request):
    # Retrieve form data
    customer_data = {
        'first_name': request.POST.get('customerFirstName'),
        'last_name': request.POST.get('customerLastName'),
        'email': request.POST.get('customerEmail'),
        'phone': request.POST.get('customerPhone'),
        'address': request.POST.get('customerAddress'),
    }

    # Retrieve cart items from session
    cart = request.session.get('cart', [])
    accessories_in_cart = Accessory.objects.filter(id__in=cart)
    
    # Format items for JSON storage
    items = [{'name': item.name, 'quantity': 1, 'price': float(item.price)} for item in accessories_in_cart]
    total_price = sum(Decimal(item['price']) for item in items)

    # Create the Order
    order = Order.objects.create(
        customer_first_name=customer_data['first_name'],
        customer_last_name=customer_data['last_name'],
        customer_email=customer_data['email'],
        customer_phone=customer_data['phone'],
        customer_address=customer_data['address'],
        items=items,
        total_price=total_price
    )

    # Clear cart after order is confirmed
    request.session['cart'] = []
    messages.success(request, "Thank you for shopping with us!")
    
    return redirect('view_cart')



from django.http import JsonResponse
from .models import Accessory

def update_cart_view(request):
    if request.method == "POST" and request.is_ajax():
        accessory_id = request.POST.get("accessory_id")
        action = request.POST.get("action")
        cart = request.session.get("cart", {})

        try:
            # Ensure the item exists in the database
            accessory = Accessory.objects.get(id=accessory_id)

            if action == "add":
                cart[accessory_id] = cart.get(accessory_id, 0) + 1  # Increase quantity
            elif action == "remove":
                if accessory_id in cart:
                    cart[accessory_id] -= 1
                    if cart[accessory_id] <= 0:
                        del cart[accessory_id]  # Remove item if quantity is zero or less
            elif action == "delete":
                cart.pop(accessory_id, None)  # Remove item entirely from cart

            # Save updated cart back to session
            request.session["cart"] = cart
            request.session.modified = True  # Ensure session is saved

            # Recalculate subtotal and total
            subtotal = sum(Accessory.objects.get(id=item_id).price * quantity for item_id, quantity in cart.items())
            delivery_charge = 45
            total = subtotal + delivery_charge

            return JsonResponse({
                "status": "success",
                "subtotal": subtotal,
                "delivery_charge": delivery_charge,
                "total": total,
                "cart_quantity": cart.get(accessory_id, 0),
                "accessory_id": accessory_id
            })
        except Accessory.DoesNotExist:
            return JsonResponse({"status": "error", "message": "Accessory does not exist."})

    return JsonResponse({"status": "error", "message": "Invalid request"})






from django.http import JsonResponse

def increment_quantity(request, accessory_id):
    cart = request.session.get('cart', {})
    cart[str(accessory_id)] = cart.get(str(accessory_id), 1) + 1  # Increase quantity by 1
    request.session['cart'] = cart
    return JsonResponse({'status': 'success', 'quantity': cart[str(accessory_id)]})

def decrement_quantity(request, accessory_id):
    cart = request.session.get('cart', {})
    if cart.get(str(accessory_id), 1) > 1:
        cart[str(accessory_id)] -= 1  # Decrease quantity by 1 if above 1
    else:
        del cart[str(accessory_id)]  # Remove item if quantity is 1
    request.session['cart'] = cart
    return JsonResponse({'status': 'success', 'quantity': cart.get(str(accessory_id), 0)})
