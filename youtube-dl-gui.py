#!/usr/bin/env python3


# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '0.0.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import subprocess
import sys


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(351, 228)
        MainWindow.setWindowTitle("youtube-dl-gui")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.DownloadButton = QtWidgets.QPushButton('Download', self.centralwidget)
        self.DownloadButton.setGeometry(QtCore.QRect(260, 170, 85, 27))
        self.DownloadButton.setObjectName("Download")
        self.UrlInput = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.UrlInput.setGeometry(QtCore.QRect(0, 30, 351, 31))
        self.UrlInput.setPlaceholderText("Download URL")
        self.UrlInput.setAccessibleName("")
        self.UrlInput.setDocumentTitle("")
        self.UrlInput.setObjectName("UrlInput")
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(0, 130, 351, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.label = QtWidgets.QLabel('Download Path', self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 110, 100, 15))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.DownloadButton.clicked.connect(self.download)

    def download(self):
        self.path = self.plainTextEdit.toPlainText()
        self.url = self.UrlInput.toPlainText()
        subprocess.run(['youtube-dl',
                        '-o',
                        self.path,
                        self.url])

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())









