
# home/models.py
from django.utils.text import slugify

from django.db import models

class HeroSection(models.Model):
    LINK_TYPE_CHOICES = [
        ('url', 'External URL'),
        ('tel', 'Phone Link'),
        ('scroll', 'Scroll to Section'),
    ]

    title = models.CharField(max_length=200)
    subtitle = models.TextField()
    button_text = models.CharField(max_length=100)
    button_link = models.CharField(max_length=200)  # Use CharField for flexibility
    link_type = models.CharField(max_length=10, choices=LINK_TYPE_CHOICES, default='url')  # New field for link type
    background_image = models.ImageField(upload_to='hero_images/')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.title




class Accessory(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    original_price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='accessories/')
    category = models.CharField(max_length=50)  # e.g., 'Case And Protection', 'Battery', etc.

    def __str__(self):
        return self.name



from django.db import models

# Model for the logo
class Logo(models.Model):
    image = models.ImageField(upload_to='logo/')
    link = models.URLField(default='/')  # Link to the homepage
    
    def __str__(self):
        return "Website Logo"

# Model for top-level navbar items
class NavbarItem(models.Model):
    title = models.CharField(max_length=50)
    link = models.URLField(null=True, blank=True)
    is_dropdown = models.BooleanField(default=False)
    
    def __str__(self):
        return self.title

# Model for dropdown items (for dropdown menus like 'Company' and 'Repair Service')
class DropdownItem(models.Model):
    parent = models.ForeignKey(NavbarItem, related_name='dropdown_items', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    link = models.URLField()

    def __str__(self):
        return f"{self.title} (dropdown under {self.parent.title})"

# Model for repair services with image
class RepairService(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='repair_services/')
    link = models.URLField(default="#")
    
    def __str__(self):
        return self.title




class RepairCategory(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories-images/')
    link = models.URLField()
    
    def __str__(self):
        return self.name


from django.db import models

class GoogleReview(models.Model):
    reviewer_name = models.CharField(max_length=100)
    reviewer_image = models.ImageField(upload_to='reviewers/')
    rating = models.DecimalField(max_digits=2, decimal_places=1, default=5.0)
    review_text = models.TextField()
    review_link = models.URLField()
    
    def __str__(self):
        return self.reviewer_name
    



from django.db import models

class Blog(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, default="Admin")
    date = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to='blogs/')
    
    url = models.URLField(max_length=200, blank=True, null=True)  # If needed, keep external URL
    slug = models.SlugField(null=True, blank=True)
    
    def __str__(self):
        return self.title
    def save(self, *args, **kwargs):
        if not self.slug:  # Only set slug if it's not already set
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
  




class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField()

    def __str__(self):
        return self.question

from django.db import models

class RepairRequest(models.Model):
    BRAND_CHOICES = [
        ('iphone', 'iPhone'),
        ('samsung', 'Samsung'),
        ('lg', 'LG'),
        ('google', 'Google'),
        ('motorola', 'Motorola'),
        ('other', 'Other'),
    ]

    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    model = models.CharField(max_length=50)
    problems = models.TextField()  # Storing problems as a comma-separated string
    description = models.TextField(null=True, blank=True)
    service_method = models.CharField(max_length=20)
    store_location = models.CharField(max_length=100, null=True, blank=True)
    preferred_date = models.CharField(max_length=100, null=True, blank=True)
    preferred_time = models.CharField(max_length=20, null=True, blank=True)
    contact_first_name = models.CharField(max_length=50)
    contact_last_name = models.CharField(max_length=50)
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.model} Repair - {self.contact_first_name} {self.contact_last_name}"




from django.db import models

class SellDevice(models.Model):
    DEVICE_TYPE_CHOICES = [
        ('phone', 'Phone'),
        ('tab', 'Tab'),
        ('computer', 'Computer'),
        ('console', 'Console'),
        ('headset', 'Headset'),
        ('something else', 'Something Else'),
    ]
    
    type = models.CharField(max_length=50, choices=DEVICE_TYPE_CHOICES)
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    description = models.TextField()
    device_images = models.ImageField(upload_to='device_images/', null=True, blank=True)
    customer_first_name = models.CharField(max_length=50)
    customer_last_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer_first_name} {self.customer_last_name} - {self.type} {self.brand} {self.model}"





from django.db import models

class FranchiseApplication(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    street_address = models.TextField()
    about_applicant = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.email}"



from django.db import models

class JobOpening(models.Model):
    title = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    employment_type = models.CharField(max_length=50)  # Full Time, Part Time
    location = models.CharField(max_length=100)  # Onsite, Remote
    salary_range = models.CharField(max_length=50)  # E.g., "$2000 - $4500 USD/month"
    description = models.TextField()
    responsibilities = models.TextField()
    requirements = models.TextField()

    def __str__(self):
        return self.title

class JobApplication(models.Model):
    job = models.ForeignKey(JobOpening, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = models.CharField(max_length=15)
    message = models.TextField(blank=True, null=True)
    resume = models.FileField(upload_to='resumes/')
    applied_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.job.title}"




from django.db import models
from django.db.models import JSONField

from decimal import Decimal

class Order(models.Model):
    customer_first_name = models.CharField(max_length=50)
    customer_last_name = models.CharField(max_length=50)
    customer_email = models.EmailField()
    customer_phone = models.CharField(max_length=15)
    customer_address = models.TextField()
    items = JSONField()  # Store items in JSON format: [{"name": ..., "quantity": ..., "price": ...}, ...]
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} by {self.customer_first_name} {self.customer_last_name}"
