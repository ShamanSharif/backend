from django.contrib import admin
from .models import HeroSection,Accessory, NavbarItem, Logo, DropdownItem, RepairService, RepairCategory, GoogleReview
# Register your models here

class DropdownItemInline(admin.TabularInline):
    model = DropdownItem
    extra = 1

class NavbarItemAdmin(admin.ModelAdmin):
    inlines = [DropdownItemInline]


admin.site.register(HeroSection)
admin.site.register(Accessory) 

admin.site.register(Logo)
admin.site.register(NavbarItem, NavbarItemAdmin)
admin.site.register(RepairService)
admin.site.register(RepairCategory)
admin.site.register(GoogleReview)



from .models import Blog, FAQ

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'date')

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question',)
