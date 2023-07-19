

cars = ['mercedes', 'tesla', 'toyota']
trucks = ['Tanker', 'Fire engine']

for car in cars:
    if car == 'mercedes':
        print(car.upper());
    else:
        print(car.capitalize());


# add element to end of the list
cars.append("another car");
print(cars)
# delete element
del cars[3]
print(cars)

cars_trucks = cars + trucks;
print(cars_trucks);