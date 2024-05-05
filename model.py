from PyQt5.QtWidgets import QGraphicsPixmapItem
from PyQt5.QtGui import QPixmap, QImage

from player import Player

import gameio


class Model():

    UPDATE_RELOAD_MODEL_ITEMS = 0
    
    def __init__(self):
        self.vlm = None
        self.initModel()

    
    def initModel(self):

        # Players
        self.loadWorld()
        self.loadPlayers()

        # Notify View Layer Manager to reload items
        if(self.vlm != None):
            self.vlm.notify(self.UPDATE_RELOAD_MODEL_ITEMS)
        

    def loadWorld(self):

        # TODO: To be filled

        pass      


    def loadPlayers(self):
        self.playerliste = []
        
        # Spieler
        player = self.loadMainPlayer()
        self.playerliste.append(player)
        
        # Gegenspieler
        others = self.loadOtherPlayers()
        for o in others:
            self.playerliste.append(o)
        

    def saveModel(self):
        gameio.saveGameToFile(self)


    def getPlayer(self):
        return self.playerliste[0]
    
    
    def getGhost(self):
        return self.playerliste[1]
    

    def setPlayerName(self, name):
        self.getPlayer().name = name
        

    def loadMainPlayer(self):

        player = Player("Player", [100,200])
        itemPlayer = QGraphicsPixmapItem((QPixmap.fromImage(QImage("imgTestPlayer.bmp"))))
        player.setGfxItem(itemPlayer, worldScale=15)
        return player
        


    def loadOtherPlayers(self):
        
        others = []
        
        # TODO: To be filled 
                
        return others



    def handlePlayerInput(self, input):

        # TODO: To be filled

        pass
            
                

    def update_model(self):

        # TODO: To be filled

        pass


    def setView(self, viewLayerManager):
        self.vlm = viewLayerManager