
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsScene
from PyQt5.QtGui import QPen, QBrush, QColor

"""
author: Paul
version: v0.4
lastChange: 05.05.24

Koordination von Layern (Views) mit Widgets und Daten

# Layout
# Widgets in Layout zur Darstellung von Inhalten
# Einfache Funktionen zum ändern von Werten in Inhalten
# Aktualisierug der Inhalte durch Widgets

"""

from model import Model
from viewLayerPlay import ViewLayerPlay

class ViewLayerManager():

    # STATES
    STATE_PLAY = 0

    # VIEW_IDs
    VIEW_PLAY = 0



    def __init__(self, model: Model):
        self.m = model
        self.vc = None                      # ViewContainer
        self.state = self.STATE_PLAY


    def set_viewContainer(self, view):
        self.vc = view
        # Initialisiere Views
        self.init_views()
        # Aktiviere aktuelle View
        self.update_viewLayout()


    def init_views(self):
        
        self.vlPlay = ViewLayerPlay(self.m)
        self.vc.add_view(self.VIEW_PLAY, self.vlPlay)


    def notify(self, _id):
        if(_id == Model.UPDATE_RELOAD_MODEL_ITEMS):
            self.vlPlay.weltView.wgs.reloadItems()


    def update_vlm(self):
        self.vlPlay.updateView()



    def update_viewLayout(self):
        """
        Entsprechned aktuellem self.state wird layout der View angepasst.
        """

        if(self.state == self.STATE_PLAY):
            self.vc.set_currentView(self.VIEW_PLAY)
        else:
            print ("What")


    def toggleState(self):
        self.update_viewLayout()


################
# EVENT Handler
#

    def handleKeyPress(self, e):
        pass

    def handleKeyRelease(self, e):
        # Auto steuern

        print(e.key())

        input = {}

        self.m.handlePlayerInput(input)