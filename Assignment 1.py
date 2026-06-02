from abc import ABC, abstractmethod
#-------------------Creating Ride Types--------------------
class RideType(ABC): #OOP Principle Abstraction for types of rides.
  def __init__(self, distance):
    self.distance = distance
  @abstractmethod #abstract method for all the classes to implement individually
  def price(self):
    pass

class Economy(RideType):
  def __init__(self, distance):
    super().__init__(distance) #Inheritance: inheriting the __init__ from base class
  def price(self):
    return self.distance * 5
class Luxury(RideType):
  def __init__(self, distance):
    super().__init__(distance)
  def price(self):
    return self.distance * 10
class Pool(RideType):
  def __init__(self, distance):
    super().__init__(distance)
  def price(self):
    return self.distance * 3 #implied polymorphic actions for each type of Ride
#-------------------Creating Drivers and implementing--------------------
class Driver:
  def __init__(self, name):
    self.name = name
    self.available = True

class DriverList:
  def __init__(self):
    self.__driver_list = [] #protected driver's list for Encapsulation practice. 
  def add_driver(self, driver): #setter for driver's list
    self.__driver_list.append(driver)
  def get_driver_list(self): #getter for driver's list
    return self.__driver_list

  def assign_driver(self):
    if self.__driver_list:
      for driver in self.__driver_list:
        if driver.available == True:
          driver.available = False
          return driver
    return None # Return None if no driver is available

#-------------------Creating Customer--------------------
class Customer:
  def __init__(self,name):
    self.name = name
#-------------------Creating Receipt--------------------
class Receipt: #S in Solid, only has one purpose: print receipt.
  def __init__(self,customer,pickup,dropoff,rideinfo,driver): #when implementing, we will fill parameters with instances of classes; association
    self.customer = customer
    self.pickup = pickup
    self.dropoff = dropoff
    self.rideinfo = rideinfo
    self.driver = driver

  def __str__(self): #method to print without showing memory address
    if self.driver:
      return f"Ride Fare ${self.rideinfo.price()}, Driver = {self.driver.name}"
    else:
      return "No drivers available." 
#all methods include what they need, (I in SOLID), 
driver1 = Driver("Alice")
driver2 = Driver("Bob")
driverList = DriverList()
driverList.add_driver(driver1)
driverList.add_driver(driver2)

customer1 = Customer("John")
assigned_driver = driverList.assign_driver()
receipt1 = Receipt(customer1,"Airport","Downtown",Economy(15),assigned_driver)
print(receipt1)

customer1 = Customer("Rebecca")
assigned_driver = driverList.assign_driver()
receipt2 = Receipt(customer1,"College","Downtown",Luxury(10),assigned_driver)
print(receipt2)

customer1 = Customer("Mike")
assigned_driver = driverList.assign_driver()
receipt3 = Receipt(customer1,"Downtown","Shopping Mall",Pool(5),assigned_driver)
print(receipt3)
