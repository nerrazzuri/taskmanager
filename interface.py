# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(609, 438)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.filter_box = QtWidgets.QComboBox(self.centralwidget)
        self.filter_box.setObjectName("filter_box")
        self.filter_box.addItem("")
        self.filter_box.addItem("")
        self.filter_box.addItem("")
        self.filter_box.addItem("")
        self.gridLayout_3.addWidget(self.filter_box, 1, 1, 1, 2)
        self.edit_mode = QtWidgets.QToolButton(self.centralwidget)
        self.edit_mode.setObjectName("edit_mode")
        self.gridLayout_3.addWidget(self.edit_mode, 1, 3, 1, 1)
        self.task_table = QtWidgets.QTableWidget(self.centralwidget)
        self.task_table.setObjectName("task_table")
        self.task_table.setColumnCount(7)
        self.task_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.task_table.setHorizontalHeaderItem(6, item)
        self.gridLayout_3.addWidget(self.task_table, 2, 0, 1, 4)
        self.close = QtWidgets.QToolButton(self.centralwidget)
        self.close.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resource/resources/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.close.setIcon(icon)
        self.close.setObjectName("close")
        self.gridLayout_3.addWidget(self.close, 0, 3, 1, 1)
        self.minimize = QtWidgets.QToolButton(self.centralwidget)
        self.minimize.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resource/resources/icons/minimize.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.minimize.setIcon(icon1)
        self.minimize.setObjectName("minimize")
        self.gridLayout_3.addWidget(self.minimize, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem, 1, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.clear_item = QtWidgets.QToolButton(self.frame)
        self.clear_item.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resource/resources/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.clear_item.setIcon(icon2)
        self.clear_item.setObjectName("clear_item")
        self.gridLayout.addWidget(self.clear_item, 3, 4, 1, 1)
        self.add_item = QtWidgets.QToolButton(self.frame)
        self.add_item.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resource/resources/icons/check.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_item.setIcon(icon3)
        self.add_item.setObjectName("add_item")
        self.gridLayout.addWidget(self.add_item, 3, 3, 1, 1)
        self.end_date = QtWidgets.QDateEdit(self.frame)
        self.end_date.setObjectName("end_date")
        self.gridLayout.addWidget(self.end_date, 1, 2, 1, 3)
        self.task_text = QtWidgets.QTextEdit(self.frame)
        self.task_text.setObjectName("task_text")
        self.gridLayout.addWidget(self.task_text, 0, 0, 4, 1)
        self.end_date_label = QtWidgets.QLabel(self.frame)
        self.end_date_label.setObjectName("end_date_label")
        self.gridLayout.addWidget(self.end_date_label, 1, 1, 1, 1)
        self.start_date = QtWidgets.QDateEdit(self.frame)
        self.start_date.setObjectName("start_date")
        self.gridLayout.addWidget(self.start_date, 0, 2, 1, 3)
        self.start_date_label = QtWidgets.QLabel(self.frame)
        self.start_date_label.setObjectName("start_date_label")
        self.gridLayout.addWidget(self.start_date_label, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 2, 1, 1, 1)
        self.reminder = QtWidgets.QSpinBox(self.frame)
        self.reminder.setObjectName("reminder")
        self.gridLayout.addWidget(self.reminder, 2, 2, 1, 3)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 2)
        self.gridLayout_3.addWidget(self.frame, 3, 0, 1, 4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.filter_box.setItemText(0, _translate("MainWindow", "All"))
        self.filter_box.setItemText(1, _translate("MainWindow", "In Progress"))
        self.filter_box.setItemText(2, _translate("MainWindow", "Cancelled"))
        self.filter_box.setItemText(3, _translate("MainWindow", "Completed"))
        self.edit_mode.setText(_translate("MainWindow", "..."))
        item = self.task_table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "id"))
        item = self.task_table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Task"))
        item = self.task_table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Start"))
        item = self.task_table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "End"))
        item = self.task_table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Remaining"))
        item = self.task_table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Status"))
        item = self.task_table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Operation"))
        self.end_date_label.setText(_translate("MainWindow", "End Date"))
        self.start_date_label.setText(_translate("MainWindow", "Start Date"))
        self.label.setText(_translate("MainWindow", "Reminder"))
import resource_rc
