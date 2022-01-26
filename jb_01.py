import pgzrun

WIDTH = 350
HEIGHT = 256

BGSPEED = 1

# Voici le fond
background = dict()
background['position'] = 0
background['night'] = 'city_background_night_small'

def update_background():
    background['position'] -= BGSPEED

# 'hooks' de pygame zero
def update():
    update_background()

def draw():
    screen.blit(background['night'], (background['position'], 0))

pgzrun.go()

