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
            