class CLS_tool(object):#道具类定义
    def __init__(self, typeNum):
        fileNameList = ['1ys.jpg', '1bz.jpg', '2chuizi.jpg','2chazuo.jpg','4sanjiao.jpg','4zhipian.jpg',\
                        '5zhipian .jpg','6zhipian.jpg','1bz2.jpg','2zhipian.jpg']
        self.img1 = pygame.image.load(fileNameList[typeNum])
        self.img = pygame.transform.scale(self.img1, (50,50) )
        self.img.set_colorkey( (64,64,64) )                