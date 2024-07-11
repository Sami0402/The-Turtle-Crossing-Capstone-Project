from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        create = random.randint(0,6)
        if (create==6):
            car = Turtle("square")
            car.shapesize(stretch_len=2,stretch_wid=1)
            car.color(random.choice(COLORS))
            car.penup()
            car_position = random.randint(a=-260,b=260)
            car.goto(320,car_position)
            self.all_cars.append(car)

    def move_backward(self):
        for cars in self.all_cars:
            cars.backward(self.speed)

    def level_up(self):
        self.speed += MOVE_INCREMENT

