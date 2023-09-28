from django.db import models

# Create your models here.
class Product(models.Model):
    name       = models.CharField(max_length=50)
    desc       = models.TextField()
    price      = models.DecimalField(max_digits=10,decimal_places= 2)
    stock      = models.IntegerField(blank=True, default=0)
    istrending = models.BooleanField(default=False)
    img        = models.ImageField(upload_to="products", blank=True)
    
    


