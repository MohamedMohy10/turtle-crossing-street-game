from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def move(self):  # Move the car
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        """ Returns the turtle to the starting point at the bottom of the screen"""
        self.goto(STARTING_POSITION)

    def reached_finish_line(self):  # checking reaching the finish line
        """ Returns True if the player reached the finish line """
        if self.ycor() >= FINISH_LINE_Y:
            return True
