from pico2d import *

class Enemy_1:
    image = None
    MOVE,ATTACK,DIE,HIT = 0, 1, 2, 3

    def __init__(self):
        if Enemy_1.image == None:
            Enemy_1.image = load_image('resource/enemy/enemy1.png')
            self.x, self.y = 500, 100
            self.frame = 0
            self.state = self.MOVE

    def update(self):
        if self.state == self.MOVE:
            self.state_frame = 8
            #self.x += 7
        elif self.state == self.ATTACK:
            self.state_frame = 11
        elif self.state == self.DIE:
            self.state_frame = 5
        elif self.state == self.HIT:
            self.state_frame = 1

        self.frame = (self.frame + 1) % self.state_frame

    def draw(self):
        if self.state == self.MOVE:
            self.image.clip_draw(self.frame * 121, 468, 121, 100, 300 + self.x , self.y)
        elif self.state == self.ATTACK:
            self.image.clip_draw(self.frame * 142, 333, 142, 135, 300 + self.x-5, self.y+16)
        elif self.state == self.DIE:
            self.image.clip_draw(self.frame * 140, 228, 140, 100, 300 + self.x+5, self.y-6)
        elif self.state == self.HIT:
            self.image.clip_draw(self.frame * 130, 128, 130, 100, 300 + self.x, self.y-4)


    def get_bb(self):
        return  self.x - 70, self.y - 70, self.x + 70, self.y + 70

    def draw_bb(self):
        draw_rectangle(*self.get_bb())
