"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Ruien Ni
"""
########################################################################
# DONE
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow()
mike = rg.SimpleTurtle('turtle')
mike.pen = rg.Pen('green', 10)
mike.speed = 5
size = 150
for k in range(10):
    mike.draw_circle(size)
    mike.pen_up()
    mike.right(45)
    mike.right(30)
    mike.pen_down()
    size = size-10

rebecca = rg.SimpleTurtle('turtle')
rebecca.pen = rg.Pen('pink',10)
rebecca.speed = 5
length = 200
for j in range (15):
    rebecca.draw_square(length)
    rebecca.pen_up()
    rebecca.left(45)
    rebecca.forward(10)
    rebecca.left(45)
    rebecca.pen_down()
    length = length-10











