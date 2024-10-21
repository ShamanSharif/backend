
# home/models.py
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
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title





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
