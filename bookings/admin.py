from django.contrib import admin

from .models import Coupon, Booking, Event



admin.site.register(Coupon)

admin.site.register(Booking)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):

  list_display = ('name', 'price_per_ticket') # Columns to display in the admin list view

  search_fields = ('name',) # Enable search by event name

  list_filter = ('price_per_ticket',) # Add filter options by ticket price



