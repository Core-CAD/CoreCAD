import FreeCAD as App
import FreeCADGui as Gui

try:
    from PySide2 import QtCore, QtGui, QtWidgets
except ImportError:
    try:
        from PySide6 import QtCore, QtGui, QtWidgets
    except ImportError:
        from PySide import QtCore, QtGui, QtWidgets

class CoreCADTitleFilter(QtCore.QObject):
    def eventFilter(self, obj, event):
        # Dynamically intercept window title changes
        if event.type() == QtCore.QEvent.WindowTitleChange:
            title = obj.windowTitle()
            if "FreeCAD" in title:
                obj.setWindowTitle(title.replace("FreeCAD", "Core CAD"))
        return super().eventFilter(obj, event)

def apply_core_cad_branding():
    main_win = Gui.getMainWindow()
    if not main_win:
        return

    # 1. Force window title override
    if "FreeCAD" in main_win.windowTitle():
        main_win.setWindowTitle(main_win.windowTitle().replace("FreeCAD", "Core CAD"))

    # Install event filter to prevent system resets
    if not hasattr(main_win, "_core_cad_filter"):
        main_win._core_cad_filter = CoreCADTitleFilter()
        main_win.installEventFilter(main_win._core_cad_filter)

    # 2. Replace application icon with a solid black icon
    pixmap = QtGui.QPixmap(64, 64)
    pixmap.fill(QtGui.QColor("black"))
    black_icon = QtGui.QIcon(pixmap)
    main_win.setWindowIcon(black_icon)
    QtWidgets.QApplication.setWindowIcon(black_icon)

    # 3. Hide default native workbenches
    workbenches_to_remove = ["StartWorkbench", "NoneWorkbench", "TestWorkbench", "WebWorkbench"]
    for wb in workbenches_to_remove:
        try:
            Gui.removeWorkbench(wb)
        except Exception:
            pass

# Apply branding once GUI event loop is active
QtCore.QTimer.singleShot(500, apply_core_cad_branding)
QtCore.QTimer.singleShot(2000, apply_core_cad_branding)