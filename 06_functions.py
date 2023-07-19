

def print_car(cars):
    # cars = ['mercedes', 'tesla', 'toyota']

    for car in cars:
        if car == 'mercedes':
            print(car.upper());
        else:
            print(car.capitalize());

print_car(['mercedes', 'tesla', 'toyota']);