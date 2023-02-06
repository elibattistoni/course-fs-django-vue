from django.db import models


class Manufacturer(models.Model):
    name = models.CharField(max_length=120)
    location = models.CharField(max_length=120)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    #! NB this field will allow us to also get all the products related to a manufacturer, starting from the manufacturer (cfrr views.py --> manufacturer_details)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )
    name = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    #! NB blank=True and null=True to make it optional
    photo = models.ImageField(blank=True, null=True)
    price = models.FloatField()
    shipping_cost = models.FloatField()
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return self.name
