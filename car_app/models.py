from django.db import models
from datetime import datetime
from django.core.validators import FileExtensionValidator
from multiselectfield import MultiSelectField 
from datetime import timezone
from account.models import User
# Create your models here.

class Brand(models.Model):
    brand_name = models.CharField(max_length=250, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand_name} was created , {self.date_created }"
    

class Car(models.Model):

    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r, r))

    car_category = models.CharField(verbose_name='car_title',max_length=200)
    brand_name = models.ForeignKey(Brand, on_delete=models.SET_NULL , null=True)
    color = models.CharField(max_length=200)
    model = models.CharField(max_length=200)
    year = models.IntegerField(('Year'), choices=year_choice)
    condition = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    description = models.TextField()
    car_photo = models.ImageField(validators=[FileExtensionValidator(
        [ 'jpg', 'jpeg'])], upload_to='cars_images')
    car_photo_1 = models.ImageField(validators=[FileExtensionValidator(
        [ 'jpg', 'jpeg'])], upload_to='cars_images', blank=True)
    car_photo_2 = models.ImageField(validators=[FileExtensionValidator(
        [ 'jpg', 'jpeg'])], upload_to='cars_images', blank=True)
    car_photo_3 = models.ImageField(validators=[FileExtensionValidator(
        [ 'jpg', 'jpeg'])], upload_to='cars_images', blank=True)
    car_photo_4 = models.ImageField(validators=[FileExtensionValidator(
        [ 'jpg', 'jpeg'])], upload_to='cars_images', blank=True)
    features = MultiSelectField(choices=features_choices)
    body_style = models.CharField(max_length=200)
    miles = models.PositiveIntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.PositiveIntegerField()
    milage = models.PositiveIntegerField()
    fuel_type = models.CharField(max_length=50)
    is_latest = models.BooleanField(default=False)
    created_date = models.DateField(default=datetime.now, blank=True)




    def _str_(self):
        return self.car_category 
    
    
class Booking(models.Model):
    state_choice = (
        ('NI', 'Niger'),
        ('BO', 'Borno '),
        ('TA', 'Taraba'),
        ('KD', 'Kaduna'),
        ('BA', 'Bauchi'),
        ('YO', 'Yobe'),
        ('ZA', 'Zamfara'),
        ('AD', 'Adamawa'),
        ('KW', 'Kwara'),
        ('KE', 'Kebbi'),
        ('BE', 'Benue'),
        ('PL', 'Plateau'),
        ('KO', 'Kogi'),
        ('OY', 'Oyo'),
        ('NA', 'Nasarawa'),
        ('SO', 'Sokoto'),
        ('KT', 'Katsina'),
        ('JI', 'Jigawa'),
        ('CR', 'Cross River'),
        ('KN', 'Kano'),
        ('GO', 'Gombe'),
        ('ED', 'Edo'),
        ('DE', 'Delta'),
        ('OG', 'Ogun'),
        ('ON', 'Ondo'),
        ('RI', 'Rivers'),
        ('BY', 'Bayelsa'),
        ('OS', 'Osun'),
        ('FC', 'Fct'),
        ('EN', 'Enugun'),
        ('AK', 'Akwa Ibom'),
        ('EK', 'Ekit'),
        ('AB', 'Abia'),
        ('EB', 'Ebonyi'),
        ('IM', 'Imo'),
        ('AN', 'Anambra'),
        ('LA', 'Lagos'),
    )
    city = models.CharField(max_length=200)
    to_state = models.CharField(max_length=10, choices=state_choice)
    user = models.ForeignKey(User , on_delete=models.CASCADE)
    car = models.OneToOneField(Car , on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    To_agree = models.BooleanField(default=False, verbose_name='Car is Booked')
    
    def __str__(self):
        return f"{self.user.first_name} booked {self.car.car_category} with the price {self.car.price} to {self.to_state}"