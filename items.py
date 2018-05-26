
class Vehicle:
    def __init__(self, name):
       self.Name = name

    def get_no_of_wheels(self, no_of_wheels):
       self.wheels = no_of_wheels

    def print_information(self):
       print("Vehicle Name:", self.Name, "no of wheels:", self.wheels)

    def update_wheels(self, no_of_wheels):
        self.wheels = no_of_wheels

class HUMAN:
   def  __init__(self,name):
        self.n1 = name
   def get_age(self,age):
        self.a1 = age
   def show_age(self):
      print("name is:", self.n1 , "age is :" , self.a1)

o1=HUMAN('RNS')
o1.get_age(60)
o1.show_age()




obj1 = Vehicle('Honda')
obj1.get_no_of_wheels(4)
obj1.update_wheels(5)
obj1.print_information()

obj2 = Vehicle('Innova')
obj2.get_no_of_wheels(6)
obj2.print_information()






 
