class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person sınıfı türetildi.")

    def intro(self):
        print(self.name,self.surname,self.age)

class Teacher(Person):
    pass


class Student(Person):
    pass


p1 = Person("Mehmet", "Çaka", 21)
p1.intro()

s1 = Student("Ahmet", "Yılmaz", 18)
s1.intro()

t1=Teacher("Murat","Yılmaz",37)
t1.intro()
