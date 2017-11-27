"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Catianne Troncin.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
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

tim = rg.SimpleTurtle('turtle')
tim.pen = rg.Pen('blue', 5)
tim.speed = 10

nancy = rg.SimpleTurtle('turtle')
nancy.pen = rg.Pen('red', 5)
nancy.speed = 10


size = 100

nancy.left(10)

for k in range(18):
    tim.draw_circle(size)
    nancy.draw_circle(size)
    tim.pen_up()
    nancy.pen_up()
    tim.right(20)
    nancy.left(20)
    tim.pen_down()
    nancy.pen_down()

window.close_on_mouse_click()