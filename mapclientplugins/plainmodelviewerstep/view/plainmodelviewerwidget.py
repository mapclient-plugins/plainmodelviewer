__author__ = 'hsor001'

from PySide6 import QtWidgets

from cmlibs.zinc.context import Context

from mapclientplugins.plainmodelviewerstep.view.ui_plainmodelviewerwidget import Ui_PlainModelViewerWidget


class PlainModelViewerWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(PlainModelViewerWidget, self).__init__(parent)
        self._ui = Ui_PlainModelViewerWidget()
        self._ui.setupUi(self)

        self._context = Context('view')
        self._setup_zinc()

        self._callback = None
        self._model_data = None

        self._make_connections()

    def _setup_zinc(self):
        self._zinc = self._ui.widgetZinc
        self._zinc.setContext(self._context)
        self._define_standard_materials()
        self._define_standard_glyphs()

    def _make_connections(self):
        self._ui.pushButtonDone.clicked.connect(self._done_button_clicked)

    def _done_button_clicked(self):
        self._callback()

    def register_done_execution(self, callback):
        self._callback = callback

    def set_model_data(self, model_data):
        self._model_data = model_data
        self._visualise()

    def _define_standard_glyphs(self):
        """
        Helper method to define the standard glyphs
        """
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()

    def _define_standard_materials(self):
        """
        Helper method to define the standard materials.
        """
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()

    def _visualise(self):
        """
        Read model data
        """
