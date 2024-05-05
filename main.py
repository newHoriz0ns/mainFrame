import sys

from PyQt5.QtGui import QSurfaceFormat 
from PyQt5.QtWidgets import QApplication

import mainFrame.mainFrame as mf
import mainFrame.viewLayerManager as viewLayerManager

# Replace in own App
import model

CONTINOUS_UPDATE = True


if __name__ == "__main__":

    # Starten der GUI Anwendung

    print ("Starte Anwendung ....")

    app = QApplication(sys.argv)


    # Render Format
    format = QSurfaceFormat()
    format.setDepthBufferSize(24)
    format.setStencilBufferSize(8)
    format.setVersion(3, 2)
    format.setProfile(QSurfaceFormat.CoreProfile)
    QSurfaceFormat.setDefaultFormat(format)



    # Init Model
    m = model.Model()

    # Init Viel Layer Manager
    viewLayerManager = viewLayerManager.ViewLayerManager(m)

    # Init MainFrame
    window = mf.MainFrame(m)
 
    # Setze Controller in View
    window.set_viewLayerManager(viewLayerManager)
    
    # Setze View in Controller 
    viewLayerManager.set_viewContainer(window.view)

    # Setze View in Model (notify)
    m.setView(viewLayerManager)

    # StartUp Finished -> Start UpdateTimer
    if(CONTINOUS_UPDATE):
        window.init_updateRoutine()
        window.start_updateRoutine()

    window.showMaximized()

    app.exec()


    # TODO: Icon
    # TODO: Icon in Taskleiste
    # TODO: Single Open
    # TODO: Crash abfangen