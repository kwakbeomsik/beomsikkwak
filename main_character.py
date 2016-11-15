from pico2d import *

running = None

class Main_Character:
    image = None

    STAND_RIGHT, STAND_LEFT, MOVE_RIGHT, MOVE_LEFT, MOTION1, MOTION2, MOTION3, MOTION4, \
    MOTION5, DIE_RIGHT, DIE_LEFT, HIT_RIGHT, HIT_LEFT = 0,1,2,3,4,5,6,7,8,9,10,11,12
    def __init__(self):
        if Main_Character.image == None:
            Main_Character.image = load_image('resource/character/character_main_zoro1.png')


        self.x, self.y = 0, 110
        self.frame = 0
        self.state = self.STAND_RIGHT

    def update(self):
        if self.state == self.MOVE_RIGHT:
            self.x += 10
        if self.state == self.MOVE_LEFT:
            self.x -= 10


        if self.state == self.STAND_RIGHT or self.state == self.MOVE_RIGHT\
            or self.state == self.STAND_LEFT or self.state == self.MOVE_LEFT or self.state == self.STAND_LEFT \
                or self.state == self.HIT_LEFT or self.state == self.STAND_RIGHT or self.state == self.HIT_RIGHT:
            self.state_frame = 6
        elif self.state == self.DIE_RIGHT or self.state == self.DIE_LEFT:
            self.state_frame = 8
        elif self.state == self.MOTION1:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

        if self.state != self.HIT_RIGHT and self.state != self.HIT_LEFT and \
            self.state != self.MOVE_RIGHT and self.state != self.MOVE_LEFT and self.state != self.STAND_LEFT:
            if self.frame == 0:
                self.state = self.STAND_RIGHT

    def draw(self):
        if self.state == self.STAND_RIGHT or self.state == self.MOVE_RIGHT:
            self.image.clip_draw(self.frame * 162, 1320, 162, 133, 300 + self.x, self.y)
        elif self.state == self.STAND_LEFT or self.state == self.MOVE_LEFT:
            self.image.clip_draw(self.frame * 160, 1170, 158, 140, 300 + self.x, self.y)
        elif self.state == self.STAND_RIGHT or self.state == self.HIT_RIGHT:
            self.image.clip_draw(self.frame * 232, 550, 210, 185, 300 + self.x, self.y)
        elif self.state == self.STAND_LEFT or self.state == self.HIT_LEFT:
            self.image.clip_draw(self.frame * 230, 300, 170, 190, 300 + self.x, self.y)
        elif self.state == self.STAND_RIGHT or self.state == self.DIE_RIGHT:
            self.image.clip_draw(self.frame * 170, 960, 150, 205, 300 + self.x, self.y + 60)
        elif self.state == self.STAND_LEFT or self.state == self.DIE_LEFT:
            self.image.clip_draw(self.frame * 170, 755, 180, 205, 300 + self.x, self.y + 60)
        elif self.state == self.MOTION1 and self.state == self.STAND_RIGHT:
            self.image.clip_draw(self.frame * 170, 260, 150, 205, 300 + self.x, self.y)
        elif self.state == self.MOTION1 and self.state == self.STAND_LEFT:
            self.image.clip_draw(self.frame * 170, 130, 150, 205, 300 + self.x, self.y)


    def handle_events(self,event):
        global running

        # events = get_events()
        # for event in events:
        #     if event.type == SDL_QUIT:
        #         running = False
        #     elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
        #         running = False
        if (event.type, event.key) == (SDL_KEYUP, SDLK_RIGHT):
            self.state = self.STAND_RIGHT
        elif (event.type, event.key) == (SDL_KEYUP, SDLK_LEFT):
            self.state = self.STAND_LEFT
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_RIGHT):
            self.state = self.MOVE_RIGHT
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_LEFT):
            self.state = self.MOVE_LEFT
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_d):
            self.state = self.HIT_RIGHT
            self.frame = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_a):
            self.state = self.HIT_LEFT
            self.frame = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_s):
            self.state = self.DIE_RIGHT
            self.frame = 0
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_w):
            self.state = self.DIE_LEFT
            self.frame = 0



    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 100, self.y + 100
    def draw_bb(self):
        draw_rectangle(*self.get_bb())




def main():

    open_canvas(1200,600)
    mc = Main_Character()

    #boss = load_image('resource/enemy/Boss/Boss_Stand.png')#
    #boss_l_h = load_image('resource/enemy/Boss/Boss_Left_Hand_Stand.png')#
    #boss_r_h = load_image('resource/enemy/Boss/Boss_Right_Hand_Stand.png')#

    global frame_bg

    global running
    running = True
    while running:

        mc.handle_events()

        mc.update()
        clear_canvas()

        #boss.clip_draw(0,0,850,590,700,320)#
        #boss_l_h.clip_draw(0,0,285,215, 370, 130)#
        #boss_r_h.clip_draw(0,0,250,215, 950, 130)#

        mc.draw()

        update_canvas()

        delay(0.07)

    close_canvas()

if __name__ == '__main__':
    main()