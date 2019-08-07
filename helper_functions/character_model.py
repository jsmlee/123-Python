import pygame 

wLeft = []
wRight = []
still =[]
num_sprite = 10
#sprite correlating to  action,add to if more actions are added
class player():
    def __init__(self,xPos,yPos,pWidth,pHeight):
        self.xPos = xPos
        self.yPos = yPos
        self.pWidth = pWidth
        self.pHeight = pHeight
        self.wLeft = False
        self.wRight = False 
        self.walkPos = 0
    def draw(self, win):
        if walkPos > num_sprite:
            walkPos = 0
        if self.wLeft:
                win.blit(wLeft[self.walkPos], (self.xPos,self.yPos))
        elif self.wRight:
                win.blit(wRight[self.walkPos], (self.xPos,self.yPos))
        else:
                win.blit(still, (self.xPos,self.yPos))
    
