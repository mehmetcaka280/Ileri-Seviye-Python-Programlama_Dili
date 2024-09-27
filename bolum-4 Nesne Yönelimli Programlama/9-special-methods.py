liste=[1,2,3]
print(len(liste))


# sayi=10
# print(len(sayi))

s="Merhaba"
print(len(s))


class Movie:
    def __init__(self, name, director,year,duration):
        self.name = name
        self.director = director
        self.year = year
        self.duration = duration
        
        
    def __repr__(self) :
        return f"{self.name}, {self.director} tarafından {self.year} yılında yayınlandı"
    
    def __len__(self):
        return self.duration
    
    def __del__(self):
        print("Film silindi")
    
    
    
    
m=Movie("Film Adı","Yönetmen","Yapım Yılı",120)
print(m.__repr__())
print(len(m))

del m