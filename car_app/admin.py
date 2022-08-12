from tkinter import Widget
from django.contrib import admin
from .models import Car , Brand , Booking
# Register your models here.



@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display  = ('model','year','condition','price' ,'is_latest',)
    list_editable = ('is_latest',)
    list_filter   = ('model','year','condition','price')
    search_fields = ('model','year','condition','price')
    list_display_links = ('model','year')



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display  = ('user','car','city','booking_date','To_agree',)
    search_fields = ('booking_date',)
    list_editable = ('To_agree',)

