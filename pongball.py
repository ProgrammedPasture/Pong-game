from turtle import Turtle

class PongBall(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)  # Ball size
        self.goto(0, 0)  # Start at the center of the screen
        self.x_move = 10  # Initial movement in x-direction
        self.y_move = 10  # Initial movement in y-direction
        self.move_speed = .01  # Speed of the ball

    def move(self):
        """Move the ball in the current direction."""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Bounce the ball when it hits a horizontal boundary (top/bottom)."""
        self.y_move *= -1  # Reverse y direction

    def bounce_x(self):
        """Bounce the ball when it hits a vertical boundary (left/right)."""
        self.x_move *= -1  # Reverse x direction

    def reset_position(self):
        """Reset the ball to the center and change direction."""
        self.goto(0, 0)
        self.bounce_x()  # Start moving in the opposite x-direction
