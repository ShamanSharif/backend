from django.contrib import admin
from .models import HeroSection,Accessory, NavbarItem, Logo, DropdownItem, RepairService, RepairCategory, GoogleReview,RepairRequest, SellDevice, FranchiseApplication, JobOpening, JobApplication, Order
# Register your models here

class DropdownItemInline(admin.TabularInline):
    model = DropdownItem
    extra = 1

class NavbarItemAdmin(admin.ModelAdmin):
    inlines = [DropdownItemInline]


admin.site.register(HeroSection)
admin.site.register(Accessory) 
admin.site.register(RepairRequest)
admin.site.register(Logo)
admin.site.register(NavbarItem, NavbarItemAdmin)
admin.site.register(RepairService)
admin.site.register(RepairCategory)
admin.site.register(GoogleReview)
admin.site.register(SellDevice)
admin.site.register(FranchiseApplication)
admin.site.register(JobOpening)
admin.site.register(JobApplication)




from .models import Blog, FAQ

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)



from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer_first_name', 'customer_last_name', 'total_price', 'created_at')
    readonly_fields = ('items',)
