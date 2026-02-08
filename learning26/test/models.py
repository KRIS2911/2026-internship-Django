from django.db import models

# Create your models here.

from django.db import models

class User(models.Model):
    ROLE_CHOICES = (
        ('Admin', 'Admin'),
        ('User', 'User'),
    )

    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    password = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.username

class AdminLog(models.Model):
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Admin'}
    )
    action = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)
    ip_address = models.CharField(max_length=50)

    class Meta:
        db_table = "admin_log"

    def __str__(self):
        return f"{self.admin.username} - {self.action}"

class ParkingLot(models.Model):
    admin = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        limit_choices_to={'role': 'Admin'}
    )
    lot_name = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "parking_lot"

    def __str__(self):
        return self.lot_name


class ParkingSlot(models.Model):
    SLOT_TYPE_CHOICES = (
        ('Regular', 'Regular'),
        ('EV', 'EV'),
        ('Handicap', 'Handicap'),
    )

    STATUS_CHOICES = (
        ('Available', 'Available'),
        ('Reserved', 'Reserved'),
        ('Occupied', 'Occupied'),
    )

    parking_lot = models.ForeignKey(ParkingLot, on_delete=models.CASCADE)
    slot_number = models.CharField(max_length=10)
    slot_type = models.CharField(max_length=20, choices=SLOT_TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    price_per_hour = models.FloatField()
    is_active = models.BooleanField(default=True)

    class Meta:
        db_table = "parking_slot"

    def __str__(self):
        return f"{self.parking_lot.lot_name} - Slot {self.slot_number}"

class Booking(models.Model):
    BOOKING_STATUS_CHOICES = (
        ('Reserved', 'Reserved'),
        ('Cancelled', 'Cancelled'),
        ('Completed', 'Completed'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    parking_slot = models.ForeignKey(ParkingSlot, on_delete=models.CASCADE)
    booking_date = models.DateField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField()
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUS_CHOICES)
    booking_code = models.CharField(max_length=50, unique=True)

    class Meta:
        db_table = "booking"

    def __str__(self):
        return self.booking_code


class Payment(models.Model):
    PAYMENT_METHOD_CHOICES = (
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('Wallet', 'Wallet'),
        ('Cash', 'Cash'),
    )

    PAYMENT_STATUS_CHOICES = (
        ('Success', 'Success'),
        ('Pending', 'Pending'),
        ('Failed', 'Failed'),
    )

    booking = models.OneToOneField(Booking, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    amount = models.FloatField()
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES)
    transaction_id = models.CharField(max_length=100)
    payment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "payment"

    def __str__(self):
        return self.transaction_id


class Notification(models.Model):
    STATUS_CHOICES = (
        ('Read', 'Read'),
        ('Unread', 'Unread'),
    )

    TYPE_CHOICES = (
        ('Alert', 'Alert'),
        ('Info', 'Info'),
        ('Reminder', 'Reminder'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = "notification"

    def __str__(self):
        return f"{self.type} - {self.user.username}"
