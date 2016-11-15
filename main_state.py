import game_framework
import main_character
import enemy
import random
from pico2d import *
from MAP import MAP

name = "MainState"

hero = None
m_enemy = None
e_num = 0
f_num = 0
motion_num = 0

bg = None

def enter():
    global hero, m_enemy, e_num, f_num, bg
    bg = load_image('resource/stage/stage2.png')
    hero = main_character.Main_Character()
    m_enemy = [enemy.Enemy_1()]

def exit():
    close_canvas()
    del(hero)
    del(m_enemy)
    del(bg)



def collide(a, b):
    # fill here
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False

    return True

def update():
    delay(0.06)
    hero.update()
    m_enemy[e_num].state = motion_num
    m_enemy[e_num].update()

def draw():
    clear_canvas()
    bg.draw(1230,300)
    m_enemy[e_num].draw()
    hero.draw()
    update_canvas()

def handle_events():
    global f_num, e_num, motion_num

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_z):
            f_num+=1
            if f_num>5:
                f_num=0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_x):
            e_num+=1
            if e_num>7:
                e_num=0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_c):
            motion_num+=1
            if motion_num>3:
                motion_num=0

        else:
            hero.handle_events(event)
    pass


def pause(): pass
def resume(): pass