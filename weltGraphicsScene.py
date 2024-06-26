from PyQt5 import QtCore
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsPixmapItem, QGraphicsRectItem, QGraphicsSceneMouseEvent, QGraphicsTextItem
from PyQt5.QtGui import QColor, QBrush, QKeyEvent, QPen, QPixmap, QImage, QFont

from model import Model

SCALE_FACTOR = 15   # Pixel pro Feld



class WeltGraphicsScene(QGraphicsScene):


    def __init__(self, m: Model):
        super().__init__()
        
        self.m = m

        # Model Items
        self.reloadItems()

        # Setze Fokus auf (centerOn durch testView)
        # self.set_centerItem(self.itemPlayer)
        

    def reloadItems(self):

        self.clear()

        # StatusMsg 
        self.itemText = QGraphicsTextItem("")
        self.itemText.setPos(0, -25)
        font = QFont("Arial", 8, QFont.Normal)
        self.itemText.setFont(font)
        self.addItem(self.itemText)

        self.loadWorldItems()
        self.loadOverlayTiles()

        # Other Players
        for i in range (1,len(self.m.playerliste)):
            self.addItem(self.m.playerliste[i].gfxItem)
            # self.set_statusText(self.m.getGhost().name)

        # Player 
        self.addItem(self.m.getPlayer().gfxItem)
        



    def loadWorldItems(self):

        # TODO: To be filled / adopted

        self.imgTest = QImage("imgTest.bmp")
        item = QGraphicsPixmapItem(QPixmap.fromImage(self.imgTest))
        item.setPos(100 * SCALE_FACTOR, 100 * SCALE_FACTOR)
        self.addItem(item)



    def loadOverlayTiles(self):

        # TODO: To be filled

        self.overlayTiles:QGraphicsRectItem = []
        item = OverlayItem(self)
        self.overlayTiles.append(item)
        self.addItem(item)



    def update_graphicsScene(self):
        self.updateOverlay()




    def updateOverlay(self):
        # TODO: To be filled
        pass


    def centerItem(self):
        return self.__centerItem
    
    
    def set_centerItem(self, item):
        self.__centerItem = item
        
        
    def set_statusText(self, text):
        self.itemText.setHtml("<p style='color:blue'>" + text + "</p>")
        




class OverlayItem(QGraphicsRectItem):
    
    def __init__(self, scene : WeltGraphicsScene):
        super().__init__(QtCore.QRectF(0, 0, SCALE_FACTOR - 2, SCALE_FACTOR - 2))
        self.setPen(QtCore.Qt.red)
        self.s = scene
        self.m = scene.m


    def mouseDoubleClickEvent(self, event: QGraphicsSceneMouseEvent) -> None:

        # TODO: To be filled

        return super().mouseDoubleClickEvent(event)