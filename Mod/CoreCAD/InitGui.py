import FreeCAD as App
import FreeCADGui as Gui
from PySide import QtCore, QtGui

class CoreCADWorkbench(Gui.Workbench):
    MenuText = "Core CAD"
    ToolTip = "Core CAD Primary Workbench"

    def Initialize(self):
        # Add custom toolbars or commands here if needed
        pass

    def GetClassName(self):
        return "Gui::PythonWorkbench"

# Register Core CAD as an official workbench
Gui.addWorkbench(CoreCADWorkbench())

def customize_core_cad_ui():
    # 1. Update main window title
    main_win = Gui.getMainWindow()
    if main_win:
        main_win.setWindowTitle("Core CAD")

    # 2. Hide unwanted native workbenches
    workbenches_to_remove = ["StartWorkbench", "NoneWorkbench", "TestWorkbench", "WebWorkbench"]
    for wb in workbenches_to_remove:
        try:
            Gui.removeWorkbench(wb)
        except Exception:
            pass

# Execute UI customization right after the Qt GUI event loop starts
QtCore.QTimer.singleShot(500, customize_core_cad_ui)