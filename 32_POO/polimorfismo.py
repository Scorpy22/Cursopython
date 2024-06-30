class Animal: #como nuestra clase padre
  def speak(self):
    pass

class Dog(Animal): #hereda la clase animal
  def speak(self):
    print("Gua Gua")

class Cat(Animal): #hereda de la clase animal
  def speak(self):
    print("Miu Miu")

#creamso las intancias o los objetos
dog = Dog()
dog.speak()
cat = Cat()
cat.speak()