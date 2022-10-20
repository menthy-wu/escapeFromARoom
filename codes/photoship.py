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