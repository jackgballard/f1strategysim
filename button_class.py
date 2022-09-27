import pygame as pg
white = (255, 255, 255)
black = (0, 0, 0)
grey = '#ecf0f1'
dgrey = '#A9A9A9'
ddgrey = '#2b2d2f'
blue = '#6699cc'
f1red = '#ff1801'

game_font = pg.font.Font(None, 50)

buttons = []
class Button():
    def __init__(self, pos, w, h, elev, txt):
        #attributes 
        self.pressed = False
        self.elev = elev
        self.dynamic_elev = elev
        self.og_y_pos = pos[1]

        #top rectangle
        self.top_col = ddgrey
        self.top_rect = pg.Rect(pos,(w,h))

        #bottom rectangle
        self.btm_col = dgrey
        self.btm_rect = pg.Rect(pos,(w,h))

        #adding text to the buttons
        self.txt = txt
        self.txt_render = game_font.render(txt, True, '#FFFFFF')
        self.txt_bbox = self.txt_render.get_rect(center = self.top_rect.center)
        buttons.append(self)

    def draw(self):
        self.top_rect.y = self.og_y_pos - self.dynamic_elev
        self.txt_bbox.center = self.top_rect.center

        self.btm_rect.midtop = self.top_rect.midtop
        self.btm_rect.height = self.top_rect.height + self.dynamic_elev

        pg.draw.rect(disp,self.btm_col,self.btm_rect,border_radius=10)
        pg.draw.rect(disp,self.top_col,self.top_rect,border_radius=10)
        disp.blit(self.txt_render, self.txt_bbox)
        self.check_click()

    def check_click(self):
        mouse_pos = pg.mouse.get_pos()
        if self.top_rect.collidepoint(mouse_pos):
            self.top_col = f1red
            if pg.mouse.get_pressed()[0]:
                self.dynamic_elev = 0
                self.pressed = True
            else:
                self.dynamic_elev = self.elev
                if self.pressed == True:
                    self.pressed = False
        else:
            self.dynamic_elev = self.elev
            self.top_col = ddgrey