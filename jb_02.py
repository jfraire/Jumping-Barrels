import pgzrun

WIDTH = 350
HEIGHT = 256

bg_pos = 0
BGSPEED = 1

FLOOR = HEIGHT-16

def update_background():
    global bg_pos
    bg_pos = bg_pos - BGSPEED

# Un héros
hero = Actor('running_hero01', anchor=('center','bottom'),
    bottomleft=(60, FLOOR))

# 'hooks' de pygame zero
def update():
    update_background()

def draw():
    screen.blit('city_background_night_small', (bg_pos, 0))
    hero.draw()

pgzrun.go()

