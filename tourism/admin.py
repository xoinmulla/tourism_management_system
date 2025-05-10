from django.contrib import admin
from .models import Destination, Package, Customer, Booking

admin.site.register(Destination)
admin.site.register(Package)
admin.site.register(Customer)
admin.site.register(Booking)
