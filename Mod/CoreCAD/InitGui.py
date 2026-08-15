import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtCore

def aplicar_customizacao_core_cad():
    # 1. Altera o título da janela principal
    main_win = Gui.getMainWindow()
    if main_win:
        main_win.setWindowTitle("Core CAD")

    # 2. Esconde bancadas nativas indesejadas do menu suspenso
    bancadas_ocultas = ["StartWorkbench", "TestWorkbench", "WebWorkbench", "NoneWorkbench"]
    for wb in bancadas_ocultas:
        try:
            Gui.removeWorkbench(wb)
        except Exception:
            pass

# Executa a customização assim que o Qt/GUI estiver 100% carregado
QtCore.QTimer.singleShot(300, aplicar_customizacao_core_cad)