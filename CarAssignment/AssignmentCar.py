# Create a class called  Car. In the __init__(), allow the user to specify the following attributes: price, speed, fuel, mileage. 
# If the price is greater than 10,000, set the tax to be 15%. Otherwise, set the tax to be 12%.

# Create six different instances of the class Car. 
# In the class have a method called display_all() that returns all the information about the car as a string. 
# In your __init__(), call this display_all() method to display information about the car once the attributes have been defined.


class Car:
    def __init__(self, price,speed,fuel,milage):
        self.price= price
        self.speed= speed
        self.fuel = fuel
        self.milage = milage

    def displayInfo(self):
        print ("Price: "+str(self.price))
        print ("Speed: "+str(self.speed))
        print ("Fuel: "+str(self.fuel))
        print ("Mileage: "+str(self.milage)+ 'mph')
        return self

    def taxtotal(self):
        if self.price < 10000:
            print("Tax: 0.12")
        else:
            print("Tax: 0.15")
        return self

car1 = Car(2000,35,"Full",15)
car1.displayInfo().taxtotal()

car2 = Car(2000,5,"Not Full",105)
car2.displayInfo().taxtotal()

car3 = Car(2000,15,"Kinda Full",95)
car3.displayInfo().taxtotal()

car4 = Car(2000,25,"Full",25)
car4.displayInfo().taxtotal()

car5 = Car(2000,45,"Empty",25)
car5.displayInfo().taxtotal()

car6 = Car(20000000,35,"Empty",15)
car6.displayInfo().taxtotal()