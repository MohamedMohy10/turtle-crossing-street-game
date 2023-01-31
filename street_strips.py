from turtle import Turtle


def draw_signs():  # The main function
    # Drawing black strips of street
    white_lines_positions = [-140, 0, 140]
    draw_lines(white_lines_positions, "white", "dashed")
    # Drawing start and finish lines
    y_positions_sf = [-260, 250]
    draw_lines(y_positions_sf, "black")


def draw_lines(y_positions, color, type=''):  # Secondary function
    all_turtles = []

    # Creating turtle objects to draw lines
    for _ in range(len(y_positions)):
        new_turtle = Turtle(shape="turtle")
        new_turtle.hideturtle()
        new_turtle.color(color)
        new_turtle.pensize(5)
        new_turtle.penup()
        new_turtle.setpos(x=-300, y=y_positions[_])
        all_turtles.append(new_turtle)

    # Drawing lines
    if type == "dashed":  # Draw dashed line
        for turtl in all_turtles:
            while turtl.xcor() < 300:
                turtl.pendown()
                turtl.forward(80)
                turtl.penup()
                turtl.forward(40)
    else:
        for turtl in all_turtles:  # Draw a straight line
            while turtl.xcor() < 300:
                turtl.pendown()
                turtl.forward(600)
