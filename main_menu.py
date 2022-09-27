#imports
import pygame as pg, time, random, sys
from pygame.locals import(
    K_w,
    K_s,
    K_UP,
    K_DOWN,
    K_ESCAPE,
    K_q,

)

#colours
white = (255, 255, 255)
black = (0, 0, 0)
grey = '#ecf0f1'
dgrey = '#A9A9A9'
ddgrey = '#2b2d2f'
blue = '#6699cc'
f1red = '#ff1801'

#screen setup
pg.init()
width = 1280
height = 720
disp = pg.display.set_mode((width, height ))
pg.display.set_caption('Formula 1 Strategy')
pg.mouse.set_visible(1)
clock = pg.time.Clock()

#images and fonts
font_csb = pg.freetype.Font(r"C:\Users\jackg\Documents\A Levels\Computer Science\VS Code\Formula Strategy Project\Fonts\Coco-Sharp-Bold-trial.ttf", 50)
bg_image = pg.image.load(r"C:\Users\jackg\Documents\A Levels\Computer Science\VS Code\Formula Strategy Project\Images\f1gamebgn.jpeg")
f1_logo = pg.image.load(r"C:\Users\jackg\Documents\A Levels\Computer Science\VS Code\Formula Strategy Project\Images\f1logo.png")
f1_logo = pg.transform.scale(f1_logo, (350, 87.5))
def f1log(x,y):
    disp.blit(f1_logo, (x, y))

#this subroutine draws a grid, making it easier to see the pixel positions of objects on the screen 
def draw_grid():
    block_size = 10
    for x in range(0, width, block_size):
        for y in range(0, height, block_size):
            rect = pg.Rect(x, y, block_size, block_size)
            pg.draw.rect(disp, black, rect, 1)

#setting up the class for the buttons on the main menu
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

game_font = pg.font.Font(None, 50)

#button setup
play_btn = Button((500,255),280,50,5,'Play')
quit_btn = Button((500,355),280,50,5,'Quit')
set_btn = Button((500, 455),280,50,5,'Settings')

buttons = [play_btn, quit_btn, set_btn]

#buttons loop
def button_draw():
    for b in buttons:
        b.draw()

#game loop
running = True
while running:
    control_key = pg.key.get_pressed()
    mouse = pg.mouse.get_pos()
    disp.blit(bg_image, (0,0))
    #draw_grid()

    button_draw()

    if control_key[K_ESCAPE]:
        break
        quit()

    #if control_key[K_UP]:



    if play_btn.pressed == True:
        print('Play')
        time.sleep(0.1)
        exec(open('r_setup.py').read())

    if quit_btn.pressed == True:
        print('Quit')
        time.sleep(0.1)
        break
        quit()

    pg.display.flip()
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.display.quit()
            running = False

    pg.display.update()
    clock.tick(60)