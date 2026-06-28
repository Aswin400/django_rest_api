from django.db import models

class Product(models.Model) : 
    title = models.CharField(default="default",null=True)
    content = models.TextField(default="default",null=True)
    price = models.IntegerField(default=1000)

    @property

    def gst_price(self) : 
        return self.price*10