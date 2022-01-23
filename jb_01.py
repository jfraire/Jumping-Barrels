import pgzrun

WIDTH = 350
HEIGHT = 256

BGSPEED = 1

bground = Actor('city_background_night_small', topleft=(0,0))

def update_background():
    bground.left -= BGSPEED

# 'hooks' de pygame zero
def update():
    update_background()

def draw():
    bground.draw()

pgzrun.go()

