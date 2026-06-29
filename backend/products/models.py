from django.db import models

class Product(models.Model) : 
    title = models.CharField()
    content = models.TextField(default=None,null = True)
    price = models.IntegerField(default=1000)

    @property

    def gst_price(self) : 
        return self.price*10
    
    def brand(self) : 
        if hasattr(self,'audi') : 
            return self.audi
        return None