# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(1126, 800)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(214, 207, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(214, 207, 207))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(162, 162, 162))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        gradient = QtGui.QLinearGradient(0.0, 0.0, 1.0, 0.0)
        gradient.setSpread(QtGui.QGradient.PadSpread)
        gradient.setCoordinateMode(QtGui.QGradient.ObjectBoundingMode)
        gradient.setColorAt(0.0, QtGui.QColor(255, 178, 102))
        gradient.setColorAt(0.55, QtGui.QColor(235, 148, 61))
        gradient.setColorAt(0.98, QtGui.QColor(0, 0, 0))
        gradient.setColorAt(1.0, QtGui.QColor(0, 0, 0, 0))
        brush = QtGui.QBrush(gradient)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        Form.setPalette(palette)
        Form.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(255, 178, 102, 255), stop:0.55 rgba(235, 148, 61, 255), stop:0.98 rgba(0, 0, 0, 255), stop:1 rgba(0, 0, 0, 0))")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_5 = QtWidgets.QGroupBox(Form)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_3.sizePolicy().hasHeightForWidth())
        self.groupBox_3.setSizePolicy(sizePolicy)
        self.groupBox_3.setStyleSheet("background-color: rgba(255, 178, 102, 255)")
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.radio_combined_cheb = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_combined_cheb.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.radio_combined_cheb.setChecked(True)
        self.radio_combined_cheb.setObjectName("radio_combined_cheb")
        self.verticalLayout.addWidget(self.radio_combined_cheb)
        self.radio_laguerre = QtWidgets.QRadioButton(self.groupBox_3)
        self.radio_laguerre.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.radio_laguerre.setObjectName("radio_laguerre")
        self.verticalLayout.addWidget(self.radio_laguerre)
        self.structureType = QtWidgets.QComboBox(self.groupBox_3)
        self.structureType.setObjectName("structureType")
        self.structureType.addItem("")
        self.structureType.addItem("")
        self.verticalLayout.addWidget(self.structureType)
        self.horizontalLayout.addWidget(self.groupBox_3)
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setStyleSheet("background-color: rgba(255, 178, 102, 255)")
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.x1_deg = QtWidgets.QSpinBox(self.groupBox_4)
        self.x1_deg.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.x1_deg.setSingleStep(1)
        self.x1_deg.setProperty("value", 2)
        self.x1_deg.setObjectName("x1_deg")
        self.gridLayout_4.addWidget(self.x1_deg, 0, 1, 1, 1)
        self.x3_deg = QtWidgets.QSpinBox(self.groupBox_4)
        self.x3_deg.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.x3_deg.setProperty("value", 2)
        self.x3_deg.setObjectName("x3_deg")
        self.gridLayout_4.addWidget(self.x3_deg, 2, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(self.groupBox_4)
        self.label_7.setStyleSheet("background-color: rgba(255, 178, 102, 255)")
        self.label_7.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_7.setObjectName("label_7")
        self.gridLayout_4.addWidget(self.label_7, 2, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setStyleSheet("background-color: rgba(255, 178, 102, 255)")
        self.label_8.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_8.setObjectName("label_8")
        self.gridLayout_4.addWidget(self.label_8, 1, 0, 1, 1)
        self.x2_deg = QtWidgets.QSpinBox(self.groupBox_4)
        self.x2_deg.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.x2_deg.setProperty("value", 1)
        self.x2_deg.setObjectName("x2_deg")
        self.gridLayout_4.addWidget(self.x2_deg, 1, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.groupBox_4)
        self.label_6.setStyleSheet("background-color: rgba(255, 178, 102, 255)")
        self.label_6.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_6.setObjectName("label_6")
        self.gridLayout_4.addWidget(self.label_6, 0, 0, 1, 1)
        self.gridLayout_4.setColumnStretch(0, 1)
        self.horizontalLayout.addWidget(self.groupBox_4)
        self.verticalLayout_2.addWidget(self.groupBox_5)
        self.groupBox = QtWidgets.QGroupBox(Form)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.radio_reanim3 = QtWidgets.QRadioButton(self.groupBox)
        self.radio_reanim3.setObjectName("radio_reanim3")
        self.gridLayout_5.addWidget(self.radio_reanim3, 2, 0, 1, 1)
        self.radio_norma = QtWidgets.QRadioButton(self.groupBox)
        self.radio_norma.setObjectName("radio_norma")
        self.gridLayout_5.addWidget(self.radio_norma, 1, 0, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label = QtWidgets.QLabel(Form)
        self.label.setStyleSheet("background-color:  rgba(255, 178, 102, 255);")
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.predictionLength = QtWidgets.QLineEdit(Form)
        self.predictionLength.setObjectName("predictionLength")
        self.horizontalLayout_3.addWidget(self.predictionLength)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.groupBox_7 = QtWidgets.QGroupBox(Form)
        self.groupBox_7.setTitle("")
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_9 = QtWidgets.QLabel(self.groupBox_7)
        self.label_9.setStyleSheet("background-color: rgba(255, 178, 102, 255)")
        self.label_9.setObjectName("label_9")
        self.horizontalLayout_2.addWidget(self.label_9)
        self.weights_box = QtWidgets.QComboBox(self.groupBox_7)
        self.weights_box.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.weights_box.setObjectName("weights_box")
        self.weights_box.addItem("")
        self.weights_box.addItem("")
        self.horizontalLayout_2.addWidget(self.weights_box)
        self.verticalLayout_2.addWidget(self.groupBox_7)
        self.groupBox_6 = QtWidgets.QGroupBox(Form)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout.setObjectName("gridLayout")
        self.predictBox = QtWidgets.QSpinBox(self.groupBox_6)
        self.predictBox.setVisible(False)
        self.predictBox.setObjectName("predictBox")
        self.gridLayout.addWidget(self.predictBox, 2, 2, 1, 1)
        self.pauseButton = QtWidgets.QPushButton(self.groupBox_6)
        self.pauseButton.setEnabled(False)
        self.pauseButton.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.pauseButton.setObjectName("pauseButton")
        self.gridLayout.addWidget(self.pauseButton, 2, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(self.groupBox_6)
        self.label_10.setEnabled(True)
        self.label_10.setVisible(False)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 2, 0, 1, 1)
        self.plot_button = QtWidgets.QPushButton(self.groupBox_6)
        self.plot_button.setEnabled(False)
        self.plot_button.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.plot_button.setObjectName("plot_button")
        self.gridLayout.addWidget(self.plot_button, 0, 2, 2, 2)
        self.exec_button = QtWidgets.QPushButton(self.groupBox_6)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(184, 184, 184))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.exec_button.setPalette(palette)
        self.exec_button.setAutoFillBackground(False)
        self.exec_button.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.exec_button.setDefault(True)
        self.exec_button.setFlat(False)
        self.exec_button.setObjectName("exec_button")
        self.gridLayout.addWidget(self.exec_button, 0, 0, 2, 2)
        self.resumeButton = QtWidgets.QPushButton(self.groupBox_6)
        self.resumeButton.setEnabled(False)
        self.resumeButton.setStyleSheet("background-color: rgb(184, 184, 184);")
        self.resumeButton.setObjectName("resumeButton")
        self.gridLayout.addWidget(self.resumeButton, 3, 3, 1, 1)
        self.label_10.raise_()
        self.predictBox.raise_()
        self.plot_button.raise_()
        self.exec_button.raise_()
        self.pauseButton.raise_()
        self.resumeButton.raise_()
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        self.weights_box.setCurrentIndex(1)
        self.exec_button.clicked.connect(Form.exec_clicked)
        self.plot_button.clicked.connect(Form.plot_clicked)
        self.x1_deg.valueChanged['int'].connect(Form.degree_modified)
        self.x2_deg.valueChanged['int'].connect(Form.degree_modified)
        self.x3_deg.valueChanged['int'].connect(Form.degree_modified)
        self.radio_combined_cheb.toggled['bool'].connect(Form.type_modified)
        self.radio_laguerre.toggled['bool'].connect(Form.type_modified)
        self.weights_box.currentIndexChanged['QString'].connect(Form.weights_modified)
        self.radio_norma.toggled['bool'].connect(Form.data_changed)
        self.radio_reanim3.toggled['bool'].connect(Form.data_changed)
        self.pauseButton.clicked.connect(Form.pause_clicked)
        self.resumeButton.clicked.connect(Form.resume_clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.radio_combined_cheb, self.x1_deg)
        Form.setTabOrder(self.x1_deg, self.x2_deg)
        Form.setTabOrder(self.x2_deg, self.x3_deg)
        Form.setTabOrder(self.x3_deg, self.exec_button)
        Form.setTabOrder(self.exec_button, self.plot_button)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form1"))
        self.groupBox_5.setTitle(_translate("Form", "ВИБІР ПОЛІНОМІВ"))
        self.groupBox_3.setTitle(_translate("Form", "Типи"))
        self.radio_combined_cheb.setText(_translate("Form", "Вид 1"))
        self.radio_laguerre.setText(_translate("Form", "Вид 2"))
        self.structureType.setItemText(0, _translate("Form", "multiplicative"))
        self.structureType.setItemText(1, _translate("Form", "additive"))
        self.groupBox_4.setTitle(_translate("Form", "Степені"))
        self.label_7.setText(_translate("Form", "X3"))
        self.label_8.setText(_translate("Form", "X2"))
        self.label_6.setText(_translate("Form", "X1"))
        self.groupBox.setTitle(_translate("Form", "ДАНI"))
        self.radio_reanim3.setText(_translate("Form", "Reanim-3"))
        self.radio_norma.setText(_translate("Form", "Norma"))
        self.label.setText(_translate("Form", "Кількість значень для прогнозу"))
        self.label_9.setText(_translate("Form", "Ваги:"))
        self.weights_box.setItemText(0, _translate("Form", "Average"))
        self.weights_box.setItemText(1, _translate("Form", "Scaled"))
        self.groupBox_6.setTitle(_translate("Form", "ВИКОНАННЯ ПРОГРАМИ"))
        self.pauseButton.setText(_translate("Form", "Зупинити"))
        self.label_10.setText(_translate("Form", "Кроки передбачення:"))
        self.plot_button.setText(_translate("Form", "Старт"))
        self.exec_button.setText(_translate("Form", "Завантажити"))
        self.resumeButton.setText(_translate("Form", "Продовжити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
