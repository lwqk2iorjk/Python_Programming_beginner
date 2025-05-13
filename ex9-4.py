class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myfunc(self):
    print("Hello my name is " + self.name+ ", my age is "+ str(self.age))
    
p1 = Person("Henrry", 12)
print (p1)
p1.myfunc()
