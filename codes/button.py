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
