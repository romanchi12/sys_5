# coding: utf8
import os
import logging
import sys

def _append_run_path():
    if getattr(sys, 'frozen', False):
        pathlist = []

        # If the application is run as a bundle, the pyInstaller bootloader
        # extends the sys module by a flag frozen=True and sets the app
        # path into variable _MEIPASS'.
        pathlist.append(sys._MEIPASS)

        # the application exe path
        _main_app_path = os.path.dirname(sys.executable)
        pathlist.append(_main_app_path)

        # append to system path enviroment
        os.environ["PATH"] += os.pathsep + os.pathsep.join(pathlist)

    logging.error("current PATH: %s", os.environ['PATH'])
_append_run_path()

from PyQt5.QtCore import pyqtSlot, pyqtSignal
from PyQt5.QtGui import QTextDocument, QFont
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog, QMessageBox

from output import PolynomialBuilder, PolynomialBuilderExpTh, PolynomialBuilderSigmoid
from solve import Solve
from task_solution import SolveExpTh
from task_solution_custom import SolveCustom

app = QApplication(sys.argv)
app.setApplicationName('lab3_sa')
#from main_window import Ui_Form
from new_main import Ui_Form
#from MAIN_WINDOW import Ui_Form
from bruteforce import BruteForceWindow


class MainWindow(QDialog, Ui_Form):
    # signals:
    input_changed = pyqtSignal('QString')
    output_changed = pyqtSignal('QString')


    def __init__(self, *args):
        super(MainWindow, self).__init__(*args)

        # setting up ui
        self.setupUi(self)

        # other initializations
        self.dimensions = [self.x1_dim.value(), self.x2_dim.value(),
                                    self.x3_dim.value(), self.y_dim.value()]
        self.degrees = [self.x1_deg.value(), self.x2_deg.value(), self.x3_deg.value()]
        self.type = 'null'
        if self.radio_combined_cheb.isChecked():
            self.type = 'combined_cheb'
        elif self.radio_laguerre.isChecked():
            self.type = 'laguerre'
        elif self.radio_sh_cheb_2.isChecked():
            self.type = 'sh_cheb_2'
        self.method = 'grad'
        if self.radioConjucateGrad.isChecked():
            self.method = 'grad'
        elif self.radioConjucateGrad.isChecked():
            self.method = 'conjucateGrad'
        elif self.radioLSTM.isChecked():
            self.method = 'lstm'
        elif self.radioCoord.isChecked():
            self.method = 'coord'
        self.custom_func_struct = self.custom_check.isChecked()
        self.input_path = self.line_input.text()
        self.output_path = self.line_output.text()
        self.samples_num = self.sample_spin.value()
        self.lambda_multiblock = self.lambda_check.isChecked()
        self.weight_method = self.weights_box.currentText().lower()
        self.custom_method = self.custom_box.currentText().lower()
        self.solution = None
        doc = self.results_field.document()
        assert isinstance(doc, QTextDocument)
        font = doc.defaultFont()
        assert isinstance(font, QFont)
        font.setFamily('Courier New')
        font.setPixelSize(12)
        doc.setDefaultFont(font)
        return

    @pyqtSlot()
    def input_clicked(self):
        filename = QFileDialog.getOpenFileName(self, 'Open data file', '.', 'Data file (*.txt *.dat)')[0]
        if filename == '':
            return
        if filename != self.input_path:
            self.input_path = filename
            self.input_changed.emit(filename)
        return

    @pyqtSlot('QString')
    def input_modified(self, value):
        if value != self.input_path:
            self.input_path = value
        return

    @pyqtSlot()
    def output_clicked(self):
        filename = QFileDialog.getSaveFileName(self, 'Save data file', '.', 'Spreadsheet (*.xlsx)')[0]
        if filename == '':
            return
        if filename != self.output_path:
            self.output_path = filename
            self.output_changed.emit(filename)
        return

    @pyqtSlot('QString')
    def output_modified(self, value):
        if value != self.output_path:
            self.output_path = value
        return

    @pyqtSlot(int)
    def samples_modified(self, value):
        self.samples_num = value
        return

    @pyqtSlot(int)
    def dimension_modified(self, value):
        sender = self.sender().objectName()
        if sender == 'x1_dim':
            self.dimensions[0] = value
        elif sender == 'x2_dim':
            self.dimensions[1] = value
        elif sender == 'x3_dim':
            self.dimensions[2] = value
        elif sender == 'y_dim':
            self.dimensions[3] = value
        return

    @pyqtSlot(int)
    def degree_modified(self, value):
        sender = self.sender().objectName()
        if sender == 'x1_deg':
            self.degrees[0] = value
        elif sender == 'x2_deg':
            self.degrees[1] = value
        elif sender == 'x3_deg':
            self.degrees[2] = value
        return

    @pyqtSlot(bool)
    def type_modified(self, isdown):
        if (isdown):
            sender = self.sender().objectName()
            if sender == 'radio_combined_cheb':
                self.type = 'combined_cheb'
            elif sender == 'radio_laguerre':
                self.type = 'laguerre'
            elif sender == 'radio_sh_cheb_2':
                self.type = 'sh_cheb_2'
        return

    @pyqtSlot(bool)
    def method_modified(self, isdown):
        if (isdown):
            sender = self.sender().objectName()
            if sender == 'radioConjucateGrad':
                self.method = 'conjucateGrad'
            elif sender == 'radioLSTM':
                self.method = 'lstm'
            elif sender == 'radioGrad':
                self.method = 'grad'
            elif sender == 'radioCoord':
                self.method = 'coord'
        return

    @pyqtSlot(bool)
    def structure_changed(self, isdown):
        self.custom_func_struct = isdown

    @pyqtSlot()
    def plot_clicked(self):
        if self.solution:
            arima_st = self.predictBox.value()
            try:
                if arima_st > 0:
                    self.solution.plot_graphs_with_prediction(arima_st)
                else:
                    self.solution.plot_graphs()
            except Exception as e:
                QMessageBox.warning(self,'Error!','Error happened during plotting: ' + str(e))
        return

    @pyqtSlot()
    def exec_clicked(self):
        self.exec_button.setEnabled(False)
        try:
            if self.custom_func_struct:
                solver = SolveCustom(self._get_params()) #SolveExpTh(self._get_params())
                solver.prepare()
                self.solution = PolynomialBuilderSigmoid(solver) #PolynomialBuilderExpTh(solver)
                self.results_field.setText(solver.show()+'\n\n'+self.solution.get_results())
            else:
                solver = Solve(self._get_params())
                solver.prepare()
                self.solution = PolynomialBuilder(solver)
                self.results_field.setText(solver.show()+'\n\n'+self.solution.get_results())
        except Exception as e:
            QMessageBox.warning(self,'Error!','Error happened during execution: ' + str(e))
        self.exec_button.setEnabled(True)
        return

    @pyqtSlot()
    def bruteforce_called(self):
        BruteForceWindow.launch(self)
        return

    @pyqtSlot(int, int, int)
    def update_degrees(self, x1_deg, x2_deg, x3_deg):
        self.x1_deg.setValue(x1_deg)
        self.x2_deg.setValue(x2_deg)
        self.x3_deg.setValue(x3_deg)
        return

    @pyqtSlot(bool)
    def lambda_calc_method_changed(self, isdown):
        self.lambda_multiblock = isdown
        return

    @pyqtSlot('QString')
    def weights_modified(self, value):
        self.weight_method = value.lower()
        return

    @pyqtSlot('QString')
    def custom_modified(self, value):
        self.custom_method = value.lower()
        return

    def _get_params(self):
        return dict(poly_type=self.type, solving_method=self.method, degrees=self.degrees, dimensions=self.dimensions,
                    samples=self.samples_num, input_file=self.input_path, output_file=self.output_path,
                    weights=self.weight_method, lambda_multiblock=self.lambda_multiblock, custom=self.custom_func_struct,
                    custom_method=self.custom_method)


# -----------------------------------------------------#
form = MainWindow()
form.setWindowTitle('System Analysis - Lab3')
form.show()
sys.exit(app.exec_())
