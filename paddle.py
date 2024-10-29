from turtle import Turtle

# Building the paddle class
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)  # Make paddle size
        self.goto(position)  # Use the passed position to place the paddle

    def go_up(self):
        new_y = self.ycor() + 40
        if new_y < 250:  # Prevent paddle from going out of bounds
            self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 40
        if new_y > -250:  # Prevent paddle from going out of bounds
            self.goto(self.xcor(), new_y)


