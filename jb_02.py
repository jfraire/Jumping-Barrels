import pgzrun

WIDTH = 350
HEIGHT = 256

BGSPEED = 1

FLOOR = HEIGHT-16

# Voici le fond
bground = Actor('city_background_night_small', topleft=(0,0))

def update_background():
    bground.left -= BGSPEED

# Un héros
hero = Actor('running_hero01', anchor=('center','bottom'),
    bottomleft=(60, FLOOR))

# 'hooks' de pygame zero
def update():
    update_background()

def draw():
    bground.draw()
    hero.draw()

pgzrun.go()

