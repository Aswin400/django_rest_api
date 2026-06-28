class SuperMarket : 

    def __init__(self,Product,price) : 
        self.Product = Product
        self.price = price
    
    @property
    def Sale_Price(self) : 
        return self.price * 10
    
    def gst(self) : 
        return self.price * 2

value = SuperMarket('maggi',15)
print(value.Product)
print(value.price)
print(value.Sale_Price)
print(value.gst())

class School : 

    class Meta  :  
        name = 'bhuvan'
        school = 'smhs'

print(School.Meta.name)