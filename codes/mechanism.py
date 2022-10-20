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