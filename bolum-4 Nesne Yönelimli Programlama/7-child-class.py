class Person:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age
        print("Person sınıfı türetildi.")

    def intro(self):
        print(self.name, self.surname, self.age)


class Student(Person):
    def __init__(self, name, surname, age, number):
        super().__init__(name, surname, age)
        self.number = number
        print("Student sınıfı türetildi.")
        
    def study(self):
        print(f"{self.name} ders çalışıyor.")
        
    def intro(self):
        print(self.name, self.surname, self.age,self.number)


class Teacher(Person):
    def __init__(self, name, surname, age, branch):
        super().__init__(name, surname, age)
        self.branch = branch
        print("Teacher sınıfı türetildi.")
        
    def teach(self):
        print(f"{self.name} {self.branch} dersi anlatıyor.")


p1 = Person("Mehmet", "Çaka", 21)
p1.intro()

s1 = Student("Ahmet", "Yılmaz", 18,105)
s1.intro()
# s1.study()
# print(s1.number)


t1 = Teacher("Murat", "Yılmaz", 37,"fizik")
t1.intro()
# t1.teach()
# print(t1.branch)
