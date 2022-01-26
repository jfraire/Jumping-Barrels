import pgzrun

WIDTH = 350
HEIGHT = 256

BGSPEED = 1

FLOOR = HEIGHT-16

# Voici le fond
background = dict()
background['position'] = 0
background['night'] = 'city_background_night_small'

def update_background():
    background['position'] -= BGSPEED

# Un héros
hero = Actor('running_hero01', anchor=('center','bottom'),
    bottomleft=(60, FLOOR))

# 'hooks' de pygame zero
def update():
    update_background()

def draw():
    screen.blit(background['night'], (background['position'], 0))
    hero.draw()

pgzrun.go()

