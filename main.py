<<<<<<< HEAD
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
=======
class Fan:
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    def __init__(self, speed=SLOW, radius=5, color="blue", on=False):
        self.__speed = speed
        self.__radius = radius
        self.__color = color
        self.__on = on

    def get_speed(self): return self.__speed
    def get_radius(self): return self.__radius
    def get_color(self): return self.__color
    def is_on(self): return self.__on

    def set_speed(self, speed): self.__speed = speed
    def set_radius(self, radius): self.__radius = radius
    def set_color(self, color): self.__color = color
    def set_on(self, on): self.__on = on


if __name__ == "__main__":
    fan1 = Fan(Fan.FAST, 10, "yellow", True)
    fan2 = Fan(Fan.MEDIUM, 5, "blue", False)

    print(f"🌀 Fan 1 → Speed: FAST | Radius: {fan1.get_radius()} | Color: {fan1.get_color().capitalize()} | Status: {'ON ✅' if fan1.is_on() else 'OFF ❌'}")
    print(f"🌀 Fan 2 → Speed: MEDIUM | Radius: {fan2.get_radius()} | Color: {fan2.get_color().capitalize()} | Status: {'ON ✅' if fan2.is_on() else 'OFF ❌'}")
>>>>>>> fc5a167149e94586531664f8b9bfb8f0fd8f0ef8
