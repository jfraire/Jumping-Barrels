import pgzrun
import random
import sys

WIDTH = 350
HEIGHT = 256

bg_pos = 0
BGSPEED = 1

FLOOR = HEIGHT-16

GRAVITY = 2
JUMP = 16

BARRELS_SPEED = 3

LIVES = 6

music.play('awesomeness')

def update_background():
    global bg_pos
    bg_pos = bg_pos - BGSPEED

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
hero.lives = LIVES

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

# Ajouter des tonneaux
barrels = set()
def add_a_barrel():
    barrel = Actor('barrel_empty', anchor=('left', 'bottom'),
        bottomleft=(WIDTH, FLOOR))
    barrels.add(barrel)

jumped_barrels = set()
killer_barrels = set()
def update_barrels():
    for barrel in barrels:
        barrel.left -= BARRELS_SPEED
        if barrel.colliderect(hero) and barrel not in killer_barrels:
            hero.lives -= 1
            killer_barrels.add(barrel)
        if (barrel.right < hero.left and barrel not in killer_barrels
            and barrel not in jumped_barrels):
            jumped_barrels.add(barrel)

# Montre les vies qui restent
def show_lives_and_points():
    screen.draw.text('Vies: '+str(hero.lives), (260, 16), color='orange')
    screen.draw.text('Points: ' + str(len(jumped_barrels)),
        (260, 32), color='orange')

# Arrêt le jeux
def stop_game():
    if hero.lives < 1 or bg_pos < -2048:
        print('Game over : '+str(len(jumped_barrels)))
        sys.exit()

# 'hooks' de pygame zero
def update():
    update_background()
    update_hero()
    if random.random() > 0.99:
        add_a_barrel()
    update_barrels()
    stop_game()

def draw():
    screen.blit('city_background_night_small', (bg_pos, 0))
    hero.draw()
    for barrel in barrels:
        barrel.draw()
    show_lives_and_points()

pgzrun.go()

