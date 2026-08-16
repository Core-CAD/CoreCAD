import FreeCAD as App
import FreeCADGui as Gui

# Compatibility check for Qt bindings across FreeCAD versions
try:
    from PySide2 import QtCore
except ImportError:
    try:
        from PySide6 import QtCore
    except ImportError:
        from PySide import QtCore

class CoreCADTitleFilter(QtCore.QObject):
    def eventFilter(self, obj, event):
        # Intercept window title changes and override them
        if event.type() == QtCore.QEvent.WindowTitleChange:
            title = obj.windowTitle()
            if "FreeCAD" in title:
                obj.setWindowTitle(title.replace("FreeCAD", "Core CAD"))
        return super().eventFilter(obj, event)

def apply_core_cad_branding():
    main_win = Gui.getMainWindow()
    if main_win:
        # Override initial title
        if "FreeCAD" in main_win.windowTitle():
            main_win.setWindowTitle(main_win.windowTitle().replace("FreeCAD", "Core CAD"))
        
        # Attach event filter to persist window title dynamically
        if not hasattr(main_win, "_core_cad_filter"):
            main_win._core_cad_filter = CoreCADTitleFilter()
            main_win.installEventFilter(main_win._core_cad_filter)

# Delay execution slightly to allow full GUI initialization
QtCore.QTimer.singleShot(1000, apply_core_cad_branding)