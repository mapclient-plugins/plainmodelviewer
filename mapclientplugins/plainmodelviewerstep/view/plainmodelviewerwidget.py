__author__ = 'hsor001'

from PySide2 import QtWidgets

from opencmiss.zinc.context import Context

from mapclientplugins.plainmodelviewerstep.view.ui_plainmodelviewerwidget import Ui_PlainModelViewerWidget

class PlainModelViewerWidget(QtWidgets.QWidget):

    def __init__(self, parent=None):
        super(PlainModelViewerWidget, self).__init__(parent)
        self._ui = Ui_PlainModelViewerWidget()
        self._ui.setupUi(self)

        self._context = Context('view')
        self._setupZinc()

        self._callback = None
        self._model_data = None

        self._makeConnections()

    def _setupZinc(self):
        self._zinc = self._ui.widgetZinc
        self._zinc.setContext(self._context)
        self._defineStandardMaterials()
        self._defineStandardGlyphs()

    def _makeConnections(self):
        self._ui.pushButtonDone.clicked.connect(self._doneButtonClicked)

    def _doneButtonClicked(self):
        self._callback()

    def registerDoneExecution(self, callback):
        self._callback = callback

    def setModelData(self, model_data):
        self._model_data = model_data
        self._visualise()

    def _defineStandardGlyphs(self):
        '''
        Helper method to define the standard glyphs
        '''
        glyph_module = self._context.getGlyphmodule()
        glyph_module.defineStandardGlyphs()

    def _defineStandardMaterials(self):
        '''
        Helper method to define the standard materials.
        '''
        material_module = self._context.getMaterialmodule()
        material_module.defineStandardMaterials()

    def _visualise(self):
        ''' Read model data
        '''



