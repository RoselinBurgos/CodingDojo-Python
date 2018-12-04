# The owner of a store wants a program to track products. 
# Create a product class to fill the following requirements.

# Product Class:
# Attributes:

# Price
# Item Name
# Weight
# Brand
# Status: default "for sale"
# Methods:

# Sell: changes status to "sold"
# Add tax: takes tax as a decimal amount as a parameter and returns the price of the item including sales tax
# Return Item: takes reason_for_return as a parameter and changes status accordingly. 
# If the item is being returned because it is defective, change status to "defective" and change price to 0. 
# If it is being returned in the box, like new, mark it "for sale". 
# If the box has been opened, set the status to "used" and apply a 20% discount.  (use "defective", "like_new", or "opened" as three possible value for reason_for_return).
# Display Info: show all product details.
# Every method that doesn't have to return something should return self so methods can be chained.

class Product:
    def __init__(self, price,name,weight,brand,reason):
        self.price= price
        self.name= name
        self.weight = weight
        self.brand = brand
        self.status = "For Sale"
        self.reason = reason

    def displayInfo(self):
        print ("Status: "+str(self.status))
        print ("Price: $"+str(self.price))
        print ("Item Name: "+str(self.name))
        print ("Brand: "+str(self.brand))
        print ("Weight: "+str(self.weight)+ ' lbs')
        return self
        
    def taxtotal(self):
        tax = self.price* 0.095
        self.price += tax
        print("Price after tax: "+ str(round(self.price,2)))
        return self
        
    def sell(self):
        self.status="Sold"
        print("Sale Status: "+self.status)
        return self

    def return_item(self):
        if self.reason == "Defective":
            self.status = "Defective"
            self.price = 0
            print("Sale Status: "+self.status)
            print("Price of returned item: "+ str(round(self.price,2)))

        if self.reason == "Open Box":
            self.status = "For Sale"
            print("Sale Status: "+self.status)
            print("Opened Box Item price: "+ str(round(self.price,2)))

        if self.reason == "Used":
            discount= self.price * 0.20
            self.price -= discount
            self.status = "Used"
            print("Sale Status: "+self.status)
            print("Price of used item: "+str(round(self.price,2)))

        if self.reason == "None":
            self.status = "none"
        return self


item1 = Product(40.99,"Electric toothbrush",.69,"Quip","Defective")
item1.displayInfo().taxtotal().sell().return_item()


item2 = Product(10.95,"Phone Case",.05,"Hex","Used")
item2.displayInfo().taxtotal().sell().return_item()


item3 = Product(10.95,"Phone Case",.05,"Hex","Open Box")
item3.displayInfo().taxtotal().sell().return_item()

        
