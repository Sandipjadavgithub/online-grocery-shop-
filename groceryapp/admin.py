from django.contrib import admin
from .models import*

# Register your models here.


@admin.register(Carousel)
class Admin(admin.ModelAdmin):
    list_display =('title','description','image')

@admin.register(Category)
class Admin(admin.ModelAdmin):
    list_display =('name','created')
@admin.register(Product)
class Admin(admin.ModelAdmin):
    list_display =('category','name','image','description','price','discount','updated','created')
@admin.register(UserProfile)
class Admin(admin.ModelAdmin):
     list_display = ('user','mobile','address','image')
@admin.register(Cart)
class Admin(admin.ModelAdmin):
    list_display =('user','product','created','updated')
@admin.register(Booking)
class Admin(admin.ModelAdmin):
    list_display =('user','product','total','status','created','updated')
@admin.register(Feedback)
class Admin(admin.ModelAdmin):
    list_display = ('user','message','status','created','updated')
@admin.register(Contact)
class Admin(admin.ModelAdmin):
    list_display=('name','email','subject')









