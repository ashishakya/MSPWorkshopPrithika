cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passenger_per_car = passengers / cars_driven
// this is the comment section
print("There are " +  str(cars) + "  cars available") #first method

print("There are" , cars , "cars available" ) #Secong method

print("There are", cars , "cars available", sep = "-")

f = "There are %d %s cars available" %(cars,"cars") # value assigned to f

print (f)
