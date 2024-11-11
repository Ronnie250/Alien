import pgzrun
import random

a=Actor("alien")
a.x=400
a.y=250
msg="Catch the alien"
hits=0
misses=0
game_over=False
score=0

def draw():
    screen.fill("#010029")
    a.draw()
    screen.draw.text(msg,(330,330))
    screen.draw.text("Hits="+str(hits),(10,10))
    screen.draw.text("Misses="+str(misses),(715,10))
    if game_over:
        screen.fill("#010029")
        screen.draw.text("GAME OVER", (180, 100), fontsize=100)
        screen.draw.text("Your total score:", (300, 285), fontsize=40)
        screen.draw.text(str(score), (375, 330), fontsize=65)

def time_up():
    global score, hits, misses, game_over
    game_over=True
    score=hits-misses

def on_mouse_down(pos):
    global msg, misses, hits
    if a.collidepoint(pos):
        a.x=random.randint(0,800)
        a.y=random.randint(0,500)
        hits=hits+1
        msg="Good Shot!"
    else:
        msg="You Missed!"
        misses=misses+1

clock.schedule(time_up, 10.0)

pgzrun.go()