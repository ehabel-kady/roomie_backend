from django.db import models

# Create your models here.
class Offer(models.Model):
    owner = models.CharField(max_length=150, default="", null=True)
    latitude = models.DecimalField(max_digits=18, decimal_places=9)
    longtude = models.DecimalField(max_digits=18, decimal_places=9)
    photo_1 = models.ImageField(upload_to="uploads/", null=True)
    photo_2 = models.ImageField(upload_to="uploads/", null=True)
    photo_3 = models.ImageField(upload_to="uploads/", null=True)
    photo_4 = models.ImageField(upload_to="uploads/", null=True)
    photo_5 = models.ImageField(upload_to="uploads/", null=True)
    phone_number = models.CharField(max_length=100, default="", null=True)
    price = models.IntegerField()
    ameneties_1 = models.CharField(max_length=100, default="", null=True)
    ameneties_2 = models.CharField(max_length=100, default="", null=True)
    ameneties_3 = models.CharField(max_length=100, default="", null=True)
    ameneties_4 = models.CharField(max_length=100, default="", null=True)
    ameneties_5 = models.CharField(max_length=100, default="", null=True)
    ameneties_6 = models.CharField(max_length=100, default="", null=True)

    class Meta:
        verbose_name = 'Offer'
        verbose_name_plural = 'Offers'
    
    def __str__(self):
        return str(self.id)