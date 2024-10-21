import pgzrun
import random

a=Actor("alien")
a.x=400
a.y=250
msg="Catch the alien"

def draw():
    screen.fill("#010029")
    a.draw()
    screen.draw.text(msg,(330,330))

def on_mouse_down(pos):
    global msg
    if a.collidepoint(pos):
        a.x=random.randint(0,800)
        a.y=random.randint(0,500)
        msg="Good Shot!"
    else:
        msg="You Missed!"


pgzrun.go()