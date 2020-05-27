# task1
class TrafficLight:
    import time as time

    def __init__(self, color):
        self._color = color

    def running(self):
        if self._color != "red":
            print("the sequence is broken, please input red color")
            return False
        while True:
            self._color = "red"
            print(self._color)
            self.time.sleep(7)
            self._color = "yellow"
            print(self._color)
            self.time.sleep(2)
            self._color = "green"
            print(self._color)
            self.time.sleep(5)


color = "red"
light1 = TrafficLight(color)
light1.running()


# task 2
class Road():

    def __init__(self, length, width, height):
        """
        :param length: length in meters
        :param width: width in meters
        :param height: height in sm
        """
        self._length = length
        self.width = width
        self._height = height

    def mass_eval(self):
        """

        :return: mass in tons
        """
        return self._length * self.width * self._height * 25/1000


road1 = Road(20, 5000, 5)
print(road1.mass_eval())

# task3
class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.income = income


class Position(Worker):
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income ["bonus"]


worker1 = Position("Ivan", "Ivanov", "Manager", {"wage": 100, "bonus": 200})
print(worker1.get_full_name(), worker1.get_total_income())

# task 4
class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def my_car_go(self, speed):
        print(f"{self.name} is moving with {speed} kmh")
        self.speed = speed

    def stop(self):
        print("the car stopped")
        self.speed = 0

    def turn(self, direction):
        if self.speed != 0:
            print(f" {self.name} has turned to the ", direction)
        else:
            print(f"{self.name} is now moving and turning to the {direction} and the speed is set to 40")
            self.speed = 40

    def show_speed(self):
        print("the speed is ", self.speed)


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print(f"your speed is {self.speed}. the speed limit is violated")
        else:
            print(f"your speed is {self.speed}")


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print(f"your speed is {self.speed}. the speed limit is violated")
        else:
            print(f"your speed is {self.speed}")


general_car = Car(50, "blue", "Lada")
general_car.my_car_go(20)
general_car.stop()
town_car = TownCar(70, "red", "Ford")
town_car.show_speed()

# task 5
class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print(f"{self.title} is drawing")


class Pen(Stationary):
    def draw(self):
        print(f"{self.title} is a pen and it is drawing")


general_stationary = Stationary("St1")
general_stationary.draw()
pen1 = Pen("pen1")
pen1.draw()
