import FreeCADGui

class CoreCADWorkbench(FreeCADGui.Workbench):
    MenuText = "Core CAD"
    ToolTip = "Interface Principal do Core CAD"

    def Initialize(self):
        pass

    def Activated(self):
        mw = FreeCADGui.getMainWindow()
        if mw:
            mw.setWindowTitle("Core CAD - Sistema CAD Mecânico")

    def Deactivated(self):
        pass

FreeCADGui.addWorkbench(CoreCADWorkbench())

def aplicar_branding():
    mw = FreeCADGui.getMainWindow()
    if mw:
        mw.setWindowTitle("Core CAD - Sistema CAD Mecânico")

# Importação rápida do Qt
try:
    from PySide2 import QtCore
    QtCore.QTimer.singleShot(0, aplicar_branding)
except Exception:
    try:
        from PySide6 import QtCore
        QtCore.QTimer.singleShot(0, aplicar_branding)
    except Exception:
        pass