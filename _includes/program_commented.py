# Import the `turtle` module.
#
# Modules are bits of code someone else wrote for us.  They rock!
import turtle

# What's going on here?
#
# The `edward =` part is me defining a *name*.  This tells Python
# to go look at what's after the equals sign when I use the name.
#
# The name I've picked is 'edward'.  Names should be descriptive.
#
# After the equals sign is where it gets interesting.  We use the
# `turtle` name to reference the module we've imported.  The dot
# then tells python to look inside the module for something called
# `Turtle`.  The `()` just mean we aren't giving that `Turtle` thing
# any extra information. 
edward = turtle.Turtle()

# Now comes a `for` statement.
# 
# Python will take each of the things after the `in`, assign them
# to the `color_name` name, and then execute only the statements
# in the susequent block (the onews with two spaces in front of them)
for color_name in ['red', 'blue', 'green', 'yellow']:
  
  # Now what? `edward` seems to have things *inside* him.  These
  # are called "Methods" and they're something you have to read
  # the documentation (or see an example) to know about.
  # Each method lets us control the `edward` turtle in a different way.
  edward.color(color_name)
  edward.forward(75)
  edward.left(90)

# This line of code makes the window wait at the end.  Otherwise it
# closes.  Comment it out by adding a "#" in front of it to see.
turtle.done()
