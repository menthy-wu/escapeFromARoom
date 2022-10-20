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