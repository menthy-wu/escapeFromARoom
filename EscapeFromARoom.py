import pygame,sys,random
SCREEN_W,SCREEN_H = 1000,600 

class CLS_pic(object):
    def __init__(self,fileName):
        img = pygame.image.load(fileName)
        self.img = pygame.transform.scale(img,\
                                          (SCREEN_W,SCREEN_H))
        self.x,self.y = 0,0
        self.w,self.h = self.img.get_size()
    def draw(self,scr,effNum = 0,spd = 5):
        if effNum == 0 or spd == 0:
            scr.blit(self.img,(0,0))
        elif effNum == 1:#左侧移入
            for x in range(-SCREEN_W,0,spd):
                scr.blit(self.img,(x,0))
                pygame.display.update()
        elif effNum == 2:#右侧移入
            for x in range(SCREEN_W,0,-spd):
                scr.blit(self.img,(x,0))
                pygame.display.update()
        elif effNum == 4:#中心放大
            for w in range(0,SCREEN_W,spd):
                h = int(w*SCREEN_H / SCREEN_W )
                x = (SCREEN_W - w)/2
                y = (SCREEN_H - h)/2
                img = pygame.transform.scale(self.img, (w, h) )
                scr.blit(img,(x,y))
                pygame.display.update()
        elif effNum == 10:#左侧推入
            oldImg = scr.copy()
            for x in range(-SCREEN_W,0,spd):
                scr.blit(self.img,(x,0))
                scr.blit(oldImg,(x + SCREEN_W,0))
                pygame.display.update()  
        elif effNum == 11:#右侧推入
            oldImg = scr.copy()
            for x in range(SCREEN_W,0,-spd):
                scr.blit(self.img,(x,0))
                scr.blit(oldImg,(x - SCREEN_W,0))
                pygame.display.update()  
        elif effNum == 12:#从小到大
            for w in range(0,SCREEN_W,spd):
                h = int(w*SCREEN_H / SCREEN_W )
                img = pygame.transform.scale(self.img, (w, h) )
                scr.blit(img,((SCREEN_W - w)/2,(SCREEN_H-h)/2))
                pygame.display.update()     
        elif effNum == 13:#从大到小
            oldImg = scr.copy()
            for w in range(SCREEN_W,0,-spd):
                h = int(w*SCREEN_H / SCREEN_W )
                img = pygame.transform.scale(oldImg, (w, h) )
                scr.blit(img,((SCREEN_W - w)/2,(SCREEN_H-h)/2))
                pygame.display.update()
class CLS_photoship(object):
    def __init__(self):
        pygame.init()
        self.scr = pygame.display.set_mode((1100,SCREEN_H))
        pygame.display.set_caption('RT Photoship')
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('STXINGKA.TTF',32)
        self.spd = 10 #show图速度，1最慢
        self.guideList = []
        self.guideID = 0#当前GUIDE
        self.mousePos = 0,0
        self.toolList = []
        self.sound = pygame.mixer.Sound('2.wav')
        for i in range(10):
            self.toolList.append(CLS_tool(i))
        self.basket = CLS_basket(len(self.toolList))
        self.mouseTool = -1 #add by liuyi
    def add_guide(self,guide):
        guide.id = len(self.guideList)
        self.guideList.append(guide)
    def play(self):#主逻辑函数
        for guide in self.guideList:
            guide.draw(self.scr)
        self.basket.draw(self.scr)
        if self.mouseTool >= 0:#add by liuyi
            self.scr.blit(self.toolList[self.mouseTool].img, (self.mousePos[0]-25, self.mousePos[1]-25))
        pygame.display.update()
        self.clock.tick(50)
    def keydown(self,key):#keydown事件处理
        pass
    def mouse_down(self,pos,btn):
        self.guideList[self.guideID].mouse_down(pos,btn)
    def mouse_up(self,pos,btn):
        self.guideList[self.guideID].mouse_up(pos,btn)
    def mouse_motion(self,pos):
        self.guideList[self.guideID].mouse_motion(pos)
class CLS_guide(object):#Guide类定义
    def __init__(self,picName):
        self.pic = CLS_pic(picName)
        self.btnList = []#图片的所有button，button内含有连接图片
        self.id = 0
        self.textList = []
        self.swayList = []
        self.packList = []
        self.jiguanList = []
        self.mimaList = []
    def draw(self,scr):
        if pship.guideID != self.id:
            return
        scr.blit(self.pic.img,(0,0))
        for btn in self.btnList:
            btn.draw(scr)
        for text in self.textList:
            text.draw(scr)
        for pack in self.packList:
            pack.draw(scr)
        for mima in self.mimaList:
            mima.draw(scr)
    def add_button(self,name,picFile,x,y,guideID):
        b = CLS_button(name,picFile,x,y,guideID)
        self.btnList.append(b)
    def add_text(self,txt,font,x,y,c,rect):
        t = CLS_text(txt,font,x,y,c,rect)
        self.textList.append(t)
    def add_sway(self,rect,guideID,effNum=0):
        t = CLS_sway(rect,guideID,effNum)
        self.swayList.append(t)
    def add_pack(self,picFileNameList,x,y,w,h,toolList):
        p = CLS_pack(picFileNameList,x,y,w,h,toolList)
        self.packList.append(p)
    def add_jiguan(self,x0,y0,w,h,guideID, toolid,effNum=0):
        j = CLS_jiguan(x0,y0,w,h,guideID, toolid,effNum)
        self.jiguanList.append(j)
    def add_mima(self,txt,font,guideID):
        m = CLS_mima(txt,font,guideID)
        self.mimaList.append(m)
    def mouse_down(self,pos,button):
        for btn in self.btnList:
            btn.mouse_down(pos,button)
        for sway in self.swayList:
            sway.mouse_down(pos,button)
        for pack in self.packList:
            pack.mouse_down(pos,button)
        for jiguan in self.jiguanList:
            jiguan.mouse_down(pos,button)
        for mima in self.mimaList:
            mima.mouse_down(pos,button)
    def mouse_up(self,pos,button):
        for btn in self.btnList:
            btn.mouse_up(pos,button)
    def mouse_motion(self,pos):
        pship.mousePos = pos
class CLS_button(object):#button按钮类定义
    def __init__(self,name,picFile,x,y,guideID):
        self.name = name
        self.img = pygame.image.load(picFile)
        self.img.set_colorkey( (38,38,38) )
        self.w ,self.h = self.img.get_width()//2,\
                         self.img.get_height()
        self.x,self.y = x,y
        self.rect  = pygame.Rect(self.x,self.y,\
                                 self.w,self.h)
        self.status = 0#状态，1为按下
        self.guideID = guideID#点击指向此guide
    def draw(self,scr):
        scr.blit(self.img,(self.x,self.y),\
                  (self.status*self.rect.w,0,\
                   self.rect.w,self.rect.h))
    def mouse_down(self,pos,button):
        if self.rect.collidepoint(pos):# if is in Button  冲突点
            pship.sound.play()
            self.status = 1#button置为按下状态
            pship.mouseTool = -1 #add by liuyi
    def mouse_up(self,pos,button):#mouse up时处理button动作
        self.status = 0##button置为松开状态
        if not self.rect.collidepoint(pos):#if not in Button
            return
        if self.name =="U":#上
            pship.guideList[self.guideID].pic.draw(pship.scr,\
                                                   12,pship.spd)
        elif self.name =='D':#下
            pship.guideList[self.guideID].pic.draw(pship.scr,\
                                                   13,pship.spd)
        elif self.name =='L':#左
            pship.guideList[self.guideID].pic.draw(pship.scr,\
                                                   10,pship.spd)
        elif self.name =='R':#右
            pship.guideList[self.guideID].pic.draw(pship.scr,\
                                                   11,pship.spd)
        pship.guideID = self.guideID#更新当前guide
class CLS_text(object):
    def __init__(self,txt,font,x,y,c,rect):
        self.txt = txt
        self.img = font.render(txt,True,c)
        self.x,self.y = x, y
        self.c = c
        self.rect = pygame.Rect(rect)#文本敏感区
    def draw(self,scr):
        if self.rect.collidepoint(pship.mousePos):
            scr.blit(self.img, (self.x, self.y))
class CLS_sway(object):
    def __init__(self,rect,guideID, effNum = 0):
        self.rect = pygame.Rect(rect)
        self.guideID = guideID
        self.effNum = effNum
    def mouse_down(self,pos,button):
        if self.rect.collidepoint(pos):#if is in sway
            pship.sound.play()
            pship.guideList[self.guideID].pic.draw(pship.scr,\
                                                   self.effNum,pship.spd)
            pship.guideID = self.guideID#更新“当前guide            
            pship.mouseTool = -1 #add by liuyi
            
class CLS_tool(object):#道具类定义
    def __init__(self, typeNum):
        fileNameList = ['1ys.jpg', '1bz.jpg', '2chuizi.jpg','2chazuo.jpg','4sanjiao.jpg','4zhipian.jpg',\
                        '5zhipian .jpg','6zhipian.jpg','1bz2.jpg','2zhipian.jpg']
        self.img1 = pygame.image.load(fileNameList[typeNum])
        self.img = pygame.transform.scale(self.img1, (50,50) )
        self.img.set_colorkey( (64,64,64) )                
class CLS_basket(object):#右上角显示的个人篮子
    def __init__(self, toolNum):
        self.toolDataList = [0] * toolNum
        self.rect = pygame.Rect( (1000,0,100,600) )
        self.basketList = [] 
    def draw(self, scr):
        txtColor = (0, 0, 255)
        pygame.draw.rect(scr, (217,153,119), self.rect, 0)
        for i in range(len(self.basketList)):
            scr.blit(pship.basket.basketList[i].img, (self.rect.x + 8, self.rect.y + 8 + 50*i))
class CLS_pack(object):#“容器”类，可以当做抽屉使用
    def __init__(self, picFileNameList, x, y, w,h,toolList):
        self.imgList = []
        for fileName in picFileNameList:
            img1 = pygame.image.load(fileName)
            img = pygame.transform.scale(img1, (w,h) )#抽屉大小
            img.set_colorkey( (64,64,64) )
            self.imgList.append(img)
        self.rect = pygame.Rect( (x, y, self.imgList[0].get_width(), \
                                  self.imgList[0].get_height()) )
        self.status = 0 #0:CLose, 1:Open
        self.toolList = toolList
        self.key = 0
    def draw(self, scr):
        scr.blit(self.imgList[self.status], (self.rect.x, self.rect.y))
        if self.status == 1:#open
            for i in range(len(self.toolList)):
                scr.blit(pship.toolList[self.toolList[i]].img, (self.rect.x + i * 28 + 40, self.rect.y + 6))
        
    def mouse_down(self, pos, button):
        pship.sound.play()
        if self.status == 1:#如果是open状态，点击每个道具会拿到bascket里去
            for i in range(len(self.toolList)):
                x0 = self.rect.x + i * 28 + 40
                y0 = self.rect.y + 6
                w, h = pship.toolList[i].img.get_size()
                if pygame.Rect( (x0,y0,w,h) ).collidepoint(pos):
                    pship.basket.basketList.append(pship.toolList[self.toolList[i]])
                    num = self.toolList[i]
                    self.toolList.pop(i)
                    pship.basket.toolDataList[num] += 1
        if self.toolList==[9]:
            if len(pship.basket.basketList)!=0:
                for i in range(len(pship.basket.basketList)):
                    if pship.toolList[8] == pship.basket.basketList[i]:
                        x,y = 1008, 8 + 50*i
                        if pygame.Rect( (x,y,50,50) ).collidepoint(pos):
                            self.key = 1
        if self.key == 1 and self.rect.collidepoint(pos):
            self.status = 1-self.status
                                

        if self.toolList!=[9] and self.rect.collidepoint(pos):# if is in 
            self.status = 1 - self.status

class CLS_jiguan(object):
    def __init__(self,x,y,w,h,guideID, toolid,effNum=0):
        self.guideID = guideID
        self.effNum = effNum
        self.toolid = toolid
        self.key = 0
        self.key2 = 0
        self.x,self.y,self.w,self.h = x,y,w,h
    def mouse_down(self,pos,button):
        if len(pship.basket.basketList) != 0:
            pship.sound.play()
            for i in range(len(pship.basket.basketList)):
                if pship.toolList[self.toolid] == pship.basket.basketList[i]:
                    x,y = 1008, 8 + 50*i
                    self.mouseid = i
                    if pygame.Rect( (x,y,50,50) ).collidepoint(pos):
                        self.key = 1#解锁
                        pship.mouseTool = self.toolid #add by liuyi
                    if self.toolid == 1:
                        if pygame.Rect( (self.x,self.y,self.w,self.h) ).collidepoint(pos):
                            pship.basket.basketList.pop(self.mouseid)
                            pship.basket.basketList.append(pship.toolList[8])
            if self.key == 1:
                if pygame.Rect( (self.x,self.y,self.w,self.h) ).collidepoint(pos):
                    pship.guideList[self.guideID].pic.draw(pship.scr,\
                                                       self.effNum,pship.spd)
                    pship.guideID = self.guideID#更新“当前guide'''
                    pship.mouseTool = -1 #add by liuyi
                
                
class CLS_mima(object):
    def __init__(self,txt,font,guideID):
        self.txt = txt
        self.guideID = guideID
        self.font = font
        self.mimaList = []
    def draw(self,scr):
        for i in range(len(self.mimaList)):
            m = str(self.mimaList[i])
            self.img = self.font.render(m,True,(64,64,64))
            scr.blit(self.img, (409+i*20, 135))
    def mouse_down(self,pos,button):
        pship.sound.play()
        if pygame.Rect( (407,200,40,35) ).collidepoint(pos):
            self.mimaList.append(1)
        if pygame.Rect( (468,200,60,35) ).collidepoint(pos):
            self.mimaList.append(2)
        if pygame.Rect( (550,200,35,35) ).collidepoint(pos):
            self.mimaList.append(3)
            
        if pygame.Rect( (407,256,40,35) ).collidepoint(pos):
            self.mimaList.append(4)
        if pygame.Rect( (468,256,60,35) ).collidepoint(pos):
            self.mimaList.append(5)
        if pygame.Rect( (550,256,35,35) ).collidepoint(pos):
            self.mimaList.append(6)
            
        if pygame.Rect( (407,314,40,35) ).collidepoint(pos):
            self.mimaList.append(7)
        if pygame.Rect( (468,314,60,35) ).collidepoint(pos):
            self.mimaList.append(8)
        if pygame.Rect( (550,314,35,35) ).collidepoint(pos):
            self.mimaList.append(9)
        if self.mimaList == self.txt:
            pship.guideList[self.guideID].pic.draw(pship.scr,0,pship.spd)
            pship.guideID = self.guideID#更新“当前guide'''
        if len(self.mimaList) == 4:
            self.mimaList = []


#————————————main——————————
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
            
        
        

        
        

        
