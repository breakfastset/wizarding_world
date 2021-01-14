from car import Car


def main():
    car1 = Car("SFF1033J", 1600)
    car2 = Car("ABC999P", 2000)
    car3 = Car("SHA1234X", 1800)
    cars = [car1, car2, car3]
    car4 = Car("XYZ0000B", 1300)
    add_car(cars, car4)
    print_cars(cars)


def print_cars(cars):
    for car in cars:
        print(car)


def add_car(cars, car):
    cars.append(car)


if __name__ == '__main__':
    main()
