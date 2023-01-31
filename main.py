import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from street_strips import draw_signs

# Screen setup
screen = Screen()
screen.title("Cross the street game")
screen.bgcolor("light grey")
screen.setup(width=600, height=600)
screen.tracer(0)
draw_signs()

# Creating score, player, car objects
score = Scoreboard()
player = Player()
car_control = CarManager()

# listening to user key press
screen.listen()
screen.onkeypress(player.move, "space")  # move when SPACE key is pressed

# game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    #  creating cars on screen and moving them
    car_control.create_car()
    car_control.move_cars()

    # Detecting if the player collided with a car
    if car_control.get_collision(player):
        score.game_over()
        game_is_on = False

    # Detecting if the player reached the finish line successfully
    if player.reached_finish_line():
        player.go_to_start()
        car_control.increase_speed()
        score.update_level()

screen.exitonclick()
