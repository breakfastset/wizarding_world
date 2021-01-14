from car import Car


def main():
    car1 = Car("SFF1033J", 1600)
    car2 = Car("ABC999P", 2000)
    car3 = Car("SHA1234X", 1800)
    car_array = [car1, car2, car3]
    print_cars(car_array)


def print_cars(cars):
    for car in cars:
        print(car)


if __name__ == '__main__':
    main()
