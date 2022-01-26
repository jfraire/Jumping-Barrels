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
running_costumes = [
    'running_hero01',
    'running_hero02',
    'running_hero03',
    'running_hero04',
    'running_hero05',
    'running_hero06',
]

hero = Actor('running_hero01', anchor=('center','bottom'),
    bottomleft=(60, FLOOR))
hero.costume = 0

def update_hero():
    """Change le costume du héros pour l'animer"""
    hero.costume += 1
    if hero.costume > 5:
        hero.costume = 0
    hero.image = running_costumes[hero.costume]

# 'hooks' de pygame zero
def update():
    update_background()
    update_hero()

def draw():
    screen.blit(background['night'], (background['position'], 0))
    hero.draw()

pgzrun.go()

