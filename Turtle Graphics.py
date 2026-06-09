import turtle

# Set up the turtle
t = turtle.Turtle()
t.shape("turtle") # Changes the cursor to look like a turtle

# Draw the 5-pointed star using a loop
for _ in range(5):
    t.forward(150)  # Move forward
    t.right(144)    # Turn exactly 144 degrees to make the star point

# Keep the window open until clicked
turtle.exitonclick()
