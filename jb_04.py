import pgzrun

WIDTH = 350
HEIGHT = 256

BGSPEED = 1

FLOOR = HEIGHT-16

GRAVITY = 2
JUMP = 16

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
hero.is_running = True
hero.vy = 0

def update_hero():
    """
    Change le costume du héros pour l'animer
    et sa position pour sauter
    """
    if hero.is_running:
        hero.costume += 1
        if hero.costume > 5:
            hero.costume = 0
        hero.image = running_costumes[hero.costume]
    else:
        hero.image = 'jumping_hero'

    # Changement de position pour sauter
    if not hero.is_running:
        hero.y += hero.vy
        hero.vy += GRAVITY
        if hero.y >= FLOOR:
            hero.y = FLOOR
            hero.vy = 0
            hero.is_running = True

# Le héros peut sauter !
def on_key_down(key):
    if hero.is_running:
        hero.is_running = False
        hero.vy -= JUMP

# 'hooks' de pygame zero
def update():
    update_background()
    update_hero()

def draw():
    screen.blit(background['night'], (background['position'], 0))
    hero.draw()

pgzrun.go()

