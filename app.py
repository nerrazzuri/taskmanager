from math import ceil
from datetime import datetime
from PyQt5.QtCore import Qt, QDate, QObject
from PyQt5.QtGui import QIcon, QColor
from PyQt5.QtWidgets import QApplication, QMainWindow, QHeaderView, QTableWidgetItem, QSystemTrayIcon, QMenu, QToolButton, QWidget, QHBoxLayout

from PyQt5.QtCore import pyqtSignal

from data import Data
from interface import Ui_MainWindow
from qss import qss
import sys
import schedule
import time

from threading import Thread


class App(QObject):
    refresh = pyqtSignal(list)
    application = QApplication(sys.argv)

    def __init__(self):
        super(App, self).__init__()
        self._window = QMainWindow()
        self._window.setStyleSheet(qss)
        self._ui = Ui_MainWindow()
        self._ui.setupUi(self._window)
        self._window.setWindowFlags(Qt.FramelessWindowHint)
        self._window.show()

        self._is_edit_mode = False
        self._data = None
        self._pos = 0
        self._items = None
        self.t = None
        self.thread_stop = False

        self._window.mousePressEvent = self.mousePressEvent
        self._window.mouseMoveEvent = self.mouseMoveEvent

        # resize table header
        table_width = self._ui.task_table.width()
        self._ui.task_table.setColumnWidth(0, ceil(table_width * 0.4))
        for index in range(1, self._ui.task_table.horizontalHeader().count()):
            self._ui.task_table.horizontalHeader().setSectionResizeMode(index, QHeaderView.Stretch)

        year = datetime.now().year
        month = datetime.now().month
        day = datetime.now().day

        self._ui.start_date.setDate(QDate(year, month, day))
        self._ui.end_date.setDate(QDate(year, month, day))
        self._ui.frame.setHidden(True)
        self._is_edit_mode = True
        self.set_tray_icon()
        self.signals()
        self.get_data()
        self.on_load(self._items)
        self.move_app('topright')
        self.job_thread()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._pos = event.globalPos() - self._window.pos()
            event.accept()

    def mouseMoveEvent(self, event):
        self._window.move(event.globalPos() - self._pos)
        event.accept()

    def signals(self):
        self._ui.edit_mode.clicked.connect(self.edit_mode_button_clicked)
        self._ui.filter_box.currentTextChanged.connect(self.filter_box_text_changed)
        self._ui.add_item.clicked.connect(self.add_item_button_clicked)
        self._ui.clear_item.clicked.connect(self.clear_item_button_clicked)

        self._ui.close.clicked.connect(self.on_close)
        self._ui.minimize.clicked.connect(self._window.showMinimized)
        self.refresh.connect(self.on_load)

    def on_close(self):
        self.thread_stop = True
        sys.exit(0)

    def set_tray_icon(self):
        tray_icon = QSystemTrayIcon()
        menu = QMenu()

        open_action = menu.addAction('Open')
        exit_action = menu.addAction('Exit')
        open_action.triggered.connect(self._window.showNormal)
        exit_action.triggered.connect(sys.exit)

        tray_icon.setIcon(QIcon(':/resource/resources/icons/system_tray.ico'))
        tray_icon.setContextMenu(menu)
        tray_icon.show()

    def move_app(self, position):
        if position == 'topright':
            fr = self._window.frameGeometry()
            top_right = QApplication.desktop().availableGeometry().topRight()
            fr.moveTopRight(top_right)
            self._window.move(fr.topLeft())
        elif position == 'center':
            center = QApplication.desktop().availableGeometry().center()
            fr = self._window.frameGeometry()
            fr.moveCenter(center)
            self._window.move(fr.topLeft())

    def get_data(self):
        self._data = Data()
        self._data.connect()
        self._items = list(self._data.select_item())
        self.refresh.emit(self._items)

    def on_load(self, items):
        self._ui.task_table.setColumnHidden(0, True)
        self._ui.task_table.setRowCount(0)
        for index, item in enumerate(items):
            complete_btn = QToolButton()
            cancel_btn = QToolButton()
            grid_layout = QHBoxLayout()
            widget = QWidget()

            complete_btn.setIcon(QIcon(':/resource/resources/icons/check.png'))
            complete_btn.setMinimumSize(16, 16)
            cancel_btn.setIcon(QIcon(':/resource/resources/icons/clear.png'))
            cancel_btn.setMinimumSize(16, 16)

            grid_layout.addWidget(complete_btn)
            grid_layout.addWidget(cancel_btn)

            widget.setLayout(grid_layout)

            today_date = datetime.now()
            end_date = datetime.strptime(item[3], "%m/%d/%Y")

            remaining = abs((end_date - today_date).days)

            self._ui.task_table.insertRow(index)
            self._ui.task_table.setItem(index, 0, QTableWidgetItem(str(item[0])))
            self._ui.task_table.setItem(index, 1, QTableWidgetItem(item[1]))
            self._ui.task_table.setItem(index, 2, QTableWidgetItem(item[2]))
            self._ui.task_table.setItem(index, 3, QTableWidgetItem(item[3]))
            self._ui.task_table.setItem(index, 4, QTableWidgetItem(str(remaining)))
            if remaining < 100:
                self._ui.task_table.item(index, 4).setBackground(QColor(255, 0, 0))
            self._ui.task_table.setItem(index, 5, QTableWidgetItem(item[4]))
            if item[4] == 'In Progress':
                self._ui.task_table.setCellWidget(index, 6, widget)
            complete_btn.setProperty('complete_row', index)
            cancel_btn.setProperty('cancel_row', index)
            complete_btn.clicked.connect(self.on_cell_complete_button_clicked)
            cancel_btn.clicked.connect(self.on_cell_cancel_button_clicked)

    def on_cell_complete_button_clicked(self):
        sender = self._window.sender()
        row_number = sender.property('complete_row')
        id = self._ui.task_table.item(row_number, 0).text()
        self._data.update_item(int(id), 'Completed')
        self.get_data()
        self.filter_box_text_changed(self._ui.filter_box.currentText())

    def on_cell_cancel_button_clicked(self):
        sender = self._window.sender()
        row_number = sender.property('cancel_row')
        id = self._ui.task_table.item(row_number, 0).text()
        self._data.update_item(int(id), 'Cancelled')
        self.get_data()
        self.filter_box_text_changed(self._ui.filter_box.currentText())

    def add_item_button_clicked(self):
        task = self._ui.task_text.toPlainText()
        start_date = self._ui.start_date.text()
        end_date = self._ui.end_date.text()
        self._data.add_item(task, start_date, end_date)
        self.get_data()
        self.filter_box_text_changed(self._ui.filter_box.currentText())

    def clear_item_button_clicked(self):
        self._ui.task_text.clear()
        self._ui.start_date.clear()
        self._ui.end_date.clear()

    def filter_box_text_changed(self, val):
        items = self._data.select_item(val)
        self._ui.task_table.setRowCount(0)
        for index, item in enumerate(items):
            complete_btn = QToolButton()
            cancel_btn = QToolButton()
            grid_layout = QHBoxLayout()
            widget = QWidget()

            complete_btn.setIcon(QIcon(':/resource/resources/icons/check.png'))
            complete_btn.setMinimumSize(16, 16)
            cancel_btn.setIcon(QIcon(':/resource/resources/icons/clear.png'))
            cancel_btn.setMinimumSize(16, 16)

            grid_layout.addWidget(complete_btn)
            grid_layout.addWidget(cancel_btn)

            widget.setLayout(grid_layout)

            today_date = datetime.now()
            end_date = datetime.strptime(item[3], "%m/%d/%Y")

            remaining = abs((end_date - today_date).days)

            self._ui.task_table.insertRow(index)
            self._ui.task_table.setItem(index, 0, QTableWidgetItem(str(item[0])))
            self._ui.task_table.setItem(index, 1, QTableWidgetItem(item[1]))
            self._ui.task_table.setItem(index, 2, QTableWidgetItem(item[2]))
            self._ui.task_table.setItem(index, 3, QTableWidgetItem(item[3]))
            self._ui.task_table.setItem(index, 4, QTableWidgetItem(str(remaining)))
            if remaining < 100:
                self._ui.task_table.item(index, 4).setBackground(QColor(255, 0, 0))
            self._ui.task_table.setItem(index, 5, QTableWidgetItem(item[4]))
            if item[4] == 'In Progress':
                self._ui.task_table.setCellWidget(index, 6, widget)
            complete_btn.setProperty('complete_row', index)
            cancel_btn.setProperty('cancel_row', index)
            complete_btn.clicked.connect(self.on_cell_complete_button_clicked)
            cancel_btn.clicked.connect(self.on_cell_cancel_button_clicked)

    def edit_mode_button_clicked(self):
        if self._is_edit_mode:
            self.move_app('center')
            self._ui.frame.setHidden(False)
            self._is_edit_mode = False
        else:
            self.move_app('topright')
            self._ui.frame.setHidden(True)
            self._is_edit_mode = True

    def start_job(self):
        schedule.every().day.at("00:01").do(self.get_data)
        while True:
            if self.thread_stop:
                break
            schedule.run_pending()
            time.sleep(1)

    def job_thread(self):
        self.t = Thread(target=self.start_job)
        self.t.start()

if __name__ == '__main__':
    app = App()
    sys.exit(app.application.exec())