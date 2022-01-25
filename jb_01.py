import pgzrun

WIDTH = 350
HEIGHT = 256

bg_pos = 0
BGSPEED = 1

def update_background():
    global bg_pos
    bg_pos = bg_pos - BGSPEED

# 'hooks' de pygame zero
def update():
    update_background()

def draw():
    screen.blit('city_background_night_small', (bg_pos, 0))

pgzrun.go()

