class Player():

    def __init__(self, name, pos):
        self.name = name
        self.pos = pos
        
        self.gfxItem = None
        self.worldScale = 1.0
        
        
        
    def setGfxItem(self, gfxItem, worldScale):
        self.gfxItem = gfxItem
        self.worldScale = worldScale
        self.updateGfxItem()

    
    
    def updateGfxItem(self):
        if(self.gfxItem):
            self.gfxItem.setPos(self.pos[0] * self.worldScale, self.pos[1] * self.worldScale)

    
    def moveTo(self, newPos):
        self.pos[0] = newPos[0]
        self.pos[1] = newPos[1]
        self.nextPossible = self.calc_possible()
        self.updateGfxItem()
        
                
    def getGfxItem(self):
        return self.gfxItem
    

    def getPosition(self):
        return self.pos
                