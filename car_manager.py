from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []

    def create_car(self):
        """ Creates a car object """
        car_chance = randint(1, 6)
        if car_chance == 1:
            car = Turtle("square")
            car.penup()
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.setheading(180)
            car.color(choice(COLORS))
            car.goto(300, randint(-250, 250))
            self.cars.append(car)

    def move_cars(self):
        """ Moves all cars on the screen by the value of the current speed"""
        for car in self.cars:
            car.forward(self.speed)

    def increase_speed(self):
        """ Increase the speed of the car by the value of MOVE_INCREMENT """
        self.speed += MOVE_INCREMENT

    def get_collision(self, object):
        """ Checking the distance between the passed [object] and car objects on screen;
        returns True if the distance is less than 20 """
        for car in self.cars:
            if car.distance(object) < 20:
                return True
