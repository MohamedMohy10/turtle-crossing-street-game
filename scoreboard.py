from turtle import Turtle


FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-290, 250)
        self.update_level()

    def update_level(self):
        """ Increases the current level by 1 """
        self.clear()
        self.level += 1
        self.write(f"level: {self.level}", align="left", font=FONT)

    def game_over(self):  # Printing the game over message at the center of the screen
        self.home()
        self.color("red")
        self.write(f"Game over", align="center", font=FONT)
