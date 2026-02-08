from django.contrib import admin
from .models import User,AdminLog,ParkingLot,ParkingSlot,Booking,Payment,Notification
# Register your models here.

admin.site.register(User)
admin.site.register(AdminLog)
admin.site.register(ParkingLot)
admin.site.register(ParkingSlot)
admin.site.register(Booking)
admin.site.register(Payment)
admin.site.register(Notification)
