from turtle import Screen
from paddle import Paddle
from pongball import PongBall

# Set up the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)  # Turn off automatic updates for smoother animation

# Create paddles and the ball
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
pong_ball = PongBall()

# Listen for key presses
screen.listen()
screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")  # Use 'w' to move the left paddle up
screen.onkey(left_paddle.go_down, "s")  # Use 's' to move the left paddle down

# Main game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen continuously
    pong_ball.move()  # Move the ball

    # Detect collision with the top or bottom wall
    if pong_ball.ycor() > 290 or pong_ball.ycor() < -290:
        pong_ball.bounce_y()

    # Detect collision with paddles
    if (pong_ball.distance(right_paddle) < 50 and pong_ball.xcor() > 320) or \
       (pong_ball.distance(left_paddle) < 50 and pong_ball.xcor() < -320):
        pong_ball.bounce_x()

    # Detect when the ball goes out of bounds on the right or left
    if pong_ball.xcor() > 380:
        pong_ball.reset_position()  # Ball goes out on the right, reset
        # You could also implement scoring here

    if pong_ball.xcor() < -380:
        pong_ball.reset_position()  # Ball goes out on the left, reset
        # You could also implement scoring here

screen.exitonclick()
