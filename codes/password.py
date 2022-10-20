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
