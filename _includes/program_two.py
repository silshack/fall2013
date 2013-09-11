import turtle

edward = turtle.Turtle()


# Old Code:
# for color in ['red', 'blue', 'green', 'yellow']:
#  edward.color(color)
#  edward.forward(75)
#  edward.left(90)

def draw_side(turtle_name, color, length, angle):
  turtle_name.color(color)
  turtle_name.forward(length)
  turtle_name.left(angle)

draw_side(edward, 'red', 75, 90)
draw_side(edward, 'blue', 75, 90)
draw_side(edward, 'green', 75, 90)
draw_side(edward, 'yellow', 75, 90)


turtle.done()
