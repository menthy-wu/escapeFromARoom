import imp
import pygame,sys,random
from basket import *
from button import *
from mechanism import *
from pack import *
from password import *
from photoship import *
from pic import *
from sway import *
from text import *
from tool import *
SCREEN_W,SCREEN_H = 1000,600 

pship = CLS_photoship()
G01 = CLS_guide('1.jpg')
pship.add_guide(G01)
G11 = CLS_guide('1.1.jpg')
pship.add_guide(G11)
G12 = CLS_guide('1.2.jpg')
pship.add_guide(G12)
G10 = CLS_guide('1.0.jpg')
pship.add_guide(G10)
G02 = CLS_guide('2.jpg')
pship.add_guide(G02)
G03 = CLS_guide('3.jpg')
pship.add_guide(G03)
G31 = CLS_guide('3.1.jpg')
pship.add_guide(G31)
G32 = CLS_guide('3.2.jpg')
pship.add_guide(G32)
G33 = CLS_guide('3.3.jpg')
pship.add_guide(G33)
G34 = CLS_guide('3.4.jpg')
pship.add_guide(G34)
G35 = CLS_guide('3.5.jpg')
pship.add_guide(G35)
G36 = CLS_guide('3.6.jpg')
pship.add_guide(G36)
G37 = CLS_guide('3.7.jpg')
pship.add_guide(G37)
G38 = CLS_guide('3.8.jpg')
pship.add_guide(G38)
G04 = CLS_guide('4.jpg')
pship.add_guide(G04)
G20 = CLS_guide('2.0.jpg')
pship.add_guide(G20)
G41 = CLS_guide('4.1.jpg')
pship.add_guide(G41)
G05 = CLS_guide('5ws.jpg')
pship.add_guide(G05)
G51 = CLS_guide('5ws1.jpg')
pship.add_guide(G51)
G06 = CLS_guide('6cs.jpg')
pship.add_guide(G06)
G07 = CLS_guide('7fin.jpg')
pship.add_guide(G07)

G01.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G04.id)
G01.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G02.id)
G11.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G04.id)
G11.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G02.id)
G12.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G04.id)
G12.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G02.id)
G02.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G01.id)
G02.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G03.id)
G03.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G03.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)
G31.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G31.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)
G33.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G33.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)
G34.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G34.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)
G35.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G35.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)
G36.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G36.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)
G37.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G37.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)
G38.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G02.id)
G38.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G04.id)


G04.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G03 .id)
G04.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G01.id)
G41.add_button('L','bLeft.bmp',20,SCREEN_H//2 - 35,G03 .id)
G41.add_button('R','bRight.bmp',\
               SCREEN_W-100,SCREEN_H//2-35,G01.id)
G10.add_button('D','bDown.bmp',\
               SCREEN_W//2-35,SCREEN_H-100,G01.id)
G20.add_button('D','bDown.bmp',\
               SCREEN_W//2-35,SCREEN_H-100,G02.id)
G05.add_button('D','bDown.bmp',\
               SCREEN_W//2-35,SCREEN_H-100,G02.id)
G51.add_button('D','bDown.bmp',\
               SCREEN_W//2-35,SCREEN_H-100,G02.id)
G06.add_button('D','bDown.bmp',\
               SCREEN_W//2-35,SCREEN_H-100,G01.id)

G01.add_sway((620,290,40,50),G10.id,12)
G02.add_sway((378, 122,222,80),G20.id,12)
G04.add_sway((425, 410,181, 41),G41.id)
G41.add_sway((426, 368,181, 41),G04.id)
G05.add_sway((719, 366,153, 57),G51.id)
G51.add_sway((719, 366,153, 57),G05.id)
G11.add_sway((214, 273,115, 131),G12.id)
G37.add_sway((333, 240,44,  77),G38.id)
G38.add_sway((148, 131,377, 317),G07.id)

G01.add_pack(['drawer0.png', 'drawer1.png'],182, 68, 195,83,[0])#新建一个pack，内含1号2号和1号tool
G01.add_pack(['drawer0.png', 'drawer1.png'],182, 140, 195,80,[1])
G02.add_pack(['drawer0.png', 'drawer1.png'],607, 320, 157,65,[2])
G02.add_pack(['drawer0.png', 'drawer1.png'],607, 380,157,65,[3])
G04.add_pack(['shafa1.jpg', 'shafa2.jpg'],605, 357,188, 100,[4])
G04.add_pack(['4picture2.jpg', '4picture2.jpg'],94, 212,230, 130,[5])
G05.add_pack(['drawer0.png', 'drawer1.png'],715, 425,155, 63,[6])
G06.add_pack(['6cs1.jpg', '6cs2.jpg'],171, 149,255, 416,[7])
G02.add_pack(['2.1.jpg', '2.2.jpg'],650, 191,80, 100,[9])

G02.add_jiguan(139, 98,180, 400,G05.id,0)
G01.add_jiguan(468, 26,50 , 50, G11.id,3)
G06.add_jiguan(600, 24,189, 500, G06.id,1)
G03.add_jiguan(540, 109,235, 225, G31.id,2)
G31.add_jiguan(540, 109,235, 225, G33.id,4)


G33.add_jiguan(540, 109,235, 225, G34.id,7)
G34.add_jiguan(540, 109,235, 225, G35.id,6)
G35.add_jiguan(540, 109,235, 225, G36.id,5)
G36.add_jiguan(540, 109,235, 225, G37.id,9)

G10.add_mima([2,3,4,8],pship.font,G06.id)

pygame.mixer.music.load('bgm.mp3')
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(loops = 0)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:#keydoen事件处理
            pship.keydown(event.key)
        elif event.type == pygame.MOUSEBUTTONDOWN: 
            pship.mouse_down(event.pos,event.button)
        elif event.type == pygame.MOUSEBUTTONUP:
            pship.mouse_up(event.pos,event.button)
        elif event.type == pygame.MOUSEMOTION:
            pship.mouse_motion(event.pos)

    pship.play()#调用主框架逻辑
            
        
        

        
        

        
