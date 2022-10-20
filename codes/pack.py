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