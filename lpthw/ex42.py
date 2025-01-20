# Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

# dog is-a animal
class Dog(Animal):
    
    def __init__(self, name):
       # self.name has-a name
       self.name = name

# cat is-a animal
class Cat(Animal):
        
    def __init__ (self, name):
        # self.name has-a name
        self.name = name

# is-a
class Person(object):
     
    def __init__(self, name):
        # has-a
        self.name = name

        # Person has-a pet of some kind
        self.pet = None

# is-a
class Employee(Person):

    def __init__ (self, name, salary):
        # has-a
        super(Employee, self).__init__(name)
        # has-a
        self.salary = salary

# is-a
class Fish(object):
    pass

# is-a
class Salmon(Fish):
    pass

# ia-a
class Halibut(Fish):
    pass


# rover is-a dog
rover = Dog("Rover")

# is-a
satan = Cat("Satan")

# is-a
mary = Person("Mary")

# has-a
mary.pet = satan

# is-a
frank = Employee("Frank", 120000)

# has-a
frank.pet = rover

# is-a
flipper = Fish()

# is-a
crouse = Salmon()

# is-a
harry = Halibut()
