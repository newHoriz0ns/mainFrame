
from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QVBoxLayout, QPushButton, QGraphicsScene, QLineEdit

from weltGraphicsViewWidget import WeltGraphicsViewWidget

from model import Model

class ViewLayerPlay(QGroupBox):

    def __init__(self, model:Model):

        super().__init__("Game")

        self.m = model

        layout = QHBoxLayout()
        self.setLayout(layout)

        ##############
        # Left (Welt)
        
        #qgs = QGraphicsScene()
        #qgs.addRect(100,100,100,100,QPen(),QBrush(QColor(0,0,0)))
        self.weltView = WeltGraphicsViewWidget(self.m)
        layout.addWidget(self.weltView)
        
        
        ##############
        # Right (Status)
        
        self.statusGroup = QGroupBox()
        self.statusLayout = QVBoxLayout()
        self.statusGroup.setLayout(self.statusLayout)
        self.statusGroup.setFixedWidth(250)
        layout.addWidget(self.statusGroup)
        
        # Name
        self.statusNameGroup = QGroupBox("Spieler")
        self.statusNameLayout = QHBoxLayout()
        self.statusNameGroup.setLayout(self.statusNameLayout)
        self.statusNameText = QLineEdit(self.m.getPlayer().name)
        self.statusNameText.textChanged.connect(self.m.setPlayerName)
        self.statusNameLayout.addWidget(self.statusNameText)
        self.statusLayout.addWidget(self.statusNameGroup)
        
        
        # Abstandhalter
        self.statusLayout.addStretch(1)
        
        # Speichern
        self.statusSpeichernButton = QPushButton("Speichern")
        self.statusSpeichernButton.clicked.connect(self.m.saveModel)
        self.statusLayout.addWidget(self.statusSpeichernButton)
        
        # Restart
        self.statusRestartButton = QPushButton("Neustart")
        self.statusRestartButton.clicked.connect(self.m.initModel)
        self.statusLayout.addWidget(self.statusRestartButton)
        
        
    def updateView (self):
        self.weltView.update_graphicsView()