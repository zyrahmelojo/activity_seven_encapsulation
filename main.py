class Car:
    def __init__(self, year_model, make):
        self.__year_model = year_model
        self.__make = make
        self.__speed = 0

    def accelerate(self):
        self.__speed += 5

    def brake(self):
        self.__speed -= 5 if self.__speed >= 5 else 0

    def get_speed(self):
        return self.__speed


if __name__ == "__main__":
    my_car = Car(2024, "Ford")
    print("Accelerating...")
    for i in range(5):
        my_car.accelerate()
        print(f"Speed after accelerate {i+1}: {my_car.get_speed()}")

    print("\nBraking...")
    for i in range(5):
        my_car.brake()
        print(f"Speed after brake {i+1}: {my_car.get_speed()}")
