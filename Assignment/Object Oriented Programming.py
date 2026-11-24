
# Question 1: Multilevel inheritance


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def show_vehicle(self):
        print("Vehicle brand:", self.brand)


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

    def show_car(self):
        print("Car seats:", self.seats)


class ElectricCar(Car):
    def __init__(self, brand, seats, battery):
        super().__init__(brand, seats)
        self.battery = battery

    def show_electric_car(self):
        print("Battery capacity:", self.battery, "kWh")


my_car = ElectricCar("Tata", 5, 40)
my_car.show_vehicle()
my_car.show_car()
my_car.show_electric_car()



# Question 2: Multiple inheritance


class Teacher:
    def teach(self):
        print("\nTeaching students")


class Researcher:
    def research(self):
        print("Doing research work")


class Professor(Teacher, Researcher):
    def show(self):
        print("I am a Professor")


prof = Professor()
prof.teach()
prof.research()
prof.show()



# Question 3: Hierarchical inheritance


class Shape:
    def area(self):
        print("Area of the shape")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print()
print("Circle area   :", Circle(5).area())
print("Rectangle area:", Rectangle(4, 6).area())
print("Triangle area :", Triangle(10, 5).area())



# Question 4: Method overriding


class Animal:
    def sound(self):
        print("Animal makes a sound")


class Dog(Animal):
    def sound(self):
        print("Dog says: Bow Bow")


class Cat(Animal):
    def sound(self):
        print("Cat says: Meow Meow")


print()
Animal().sound()
Dog().sound()
Cat().sound()



# Question 5: Operator overloading


class ComplexNumber:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

   
    def __add__(self, other):
        return ComplexNumber(self.real + other.real,
                             self.imaginary + other.imaginary)

    def show(self):
        print(self.real, "+", str(self.imaginary) + "i")


c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)
c3 = c1 + c2

print("\nSum of two complex numbers:")
c3.show()



# Question 6: Create a class with a private variable (__salary)


class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.__salary = salary         

    def get_salary(self):
        return self.__salary

    def set_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary


emp = Employee("Rahul", 40000)
print("\nEmployee:", emp.name)
print("Salary:", emp.get_salary())

emp.set_salary(50000)
print("Updated salary:", emp.get_salary())

try:
    print(emp.__salary)
except AttributeError:
    print("Cannot access __salary directly, it is private")



# Question 7: ATM system using encapsulation


class ATM:
    def __init__(self, pin, balance):
        self.__pin = pin               
        self.__balance = balance        

    def check_pin(self, entered_pin):
        return entered_pin == self.__pin

    def check_balance(self):
        print("Balance:", self.__balance)

    def deposit(self, amount):
        self.__balance = self.__balance + amount
        print("Deposited:", amount)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance = self.__balance - amount
            print("Withdrawn:", amount)


atm = ATM(1234, 10000)

entered_pin = int(input("\nEnter your ATM PIN: "))

if atm.check_pin(entered_pin):
    print("PIN correct")
    atm.check_balance()

    deposit_amount = int(input("Enter amount to deposit: "))
    atm.deposit(deposit_amount)

    withdraw_amount = int(input("Enter amount to withdraw: "))
    atm.withdraw(withdraw_amount)

    atm.check_balance()
else:
    print("Wrong PIN")



# Question 8: Game Character Design


class Character:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self):
        print(self.name, "attacks with power", self.attack_power)

    def special_move(self):
        print(self.name, "has no special move")

    def show_status(self):
        print(self.name, "- Health:", self.health)


class Warrior(Character):
    def special_move(self):
        print(self.name, "uses Sword Slash! Damage:", self.attack_power * 2)


class Mage(Character):
    def special_move(self):
        print(self.name, "casts Fireball! Damage:", self.attack_power * 3)


class Archer(Character):
    def special_move(self):
        print(self.name, "shoots Triple Arrow! Damage:", self.attack_power * 2.5)


print()
characters = [
    Warrior("Thor", 150, 20),
    Mage("Merlin", 80, 30),
    Archer("Legolas", 100, 25)
]

for player in characters:
    player.show_status()
    player.attack()
    player.special_move()
    print()