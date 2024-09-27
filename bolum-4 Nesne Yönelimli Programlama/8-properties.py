class Product:
    def __init__(self, name, price,description):
        self.name = name
        
        if price>=0:
            self._price = price
        else:
            raise ValueError("Ürün fiyatı negatif olamaz")
        
        if len(description)<=20:
            self._description=description
        else:
            raise ValueError("Açıklama kısmı 20 karakterden uzun olamaz")
        
    @property    
    def price(self):
        return self._price
    
    @price.setter
    def price(self,value):
        if value>=0:
            self._price = value
        else:
            raise ValueError("Ürün fiyatı negatif olamaz")
    
    @property   
    def description(self):
        return self._description
    
    @description.setter
    def description(self,value):
        if len(value)<=20:
            self._description=value
        else:
            raise ValueError("Açıklama kısmı 20 karakterden uzun olamaz")
        
        
        
    # def set_price(self,value):
    #     if value>=0:
    #         self._price = value
    #     else:
    #         raise ValueError("Ürün fiyatı negatif olamaz")
        
        
    # def get_price(self):
    #     return self._price


p=Product("Iphone 16",80000,"Ios işletim sistemi")

print(p.price)
p.price=90000
print(p.price)


print(p.description)
p.description="Android değildir"
print(p.description)

# p.set_price(70000)
# print(p.get_price())

# print(p.name,p.price)