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