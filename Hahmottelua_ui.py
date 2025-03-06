# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Hahmottelua.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenu, QMenuBar, QPlainTextEdit, QPushButton,
    QSizePolicy, QStatusBar, QTextEdit, QWidget)
import testpictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(967, 661)
        font = QFont()
        font.setPointSize(26)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(42, 138, 149);\n"
"\n"
"\n"
"\n"
"")
        self.actionRekister_ityminen = QAction(MainWindow)
        self.actionRekister_ityminen.setObjectName(u"actionRekister_ityminen")
        self.actionLainaus = QAction(MainWindow)
        self.actionLainaus.setObjectName(u"actionLainaus")
        self.actionK_ytt_ehdot = QAction(MainWindow)
        self.actionK_ytt_ehdot.setObjectName(u"actionK_ytt_ehdot")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(570, 520, 191, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(80, 90, 401, 441))
        self.frame.setStyleSheet(u"background-color: rgb(51, 167, 181);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.firstNamelabel = QLabel(self.frame)
        self.firstNamelabel.setObjectName(u"firstNamelabel")
        self.firstNamelabel.setGeometry(QRect(30, 30, 121, 41))
        font2 = QFont()
        font2.setPointSize(22)
        self.firstNamelabel.setFont(font2)
        self.lastNamelabel = QLabel(self.frame)
        self.lastNamelabel.setObjectName(u"lastNamelabel")
        self.lastNamelabel.setGeometry(QRect(30, 150, 151, 41))
        self.lastNamelabel.setFont(font2)
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 260, 211, 51))
        self.label_3.setFont(font2)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(80, 330, 271, 64))
        self.plainTextEdit_2.setFont(font2)
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(80, 70, 271, 61))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(80, 200, 271, 64))
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"color: rgb(2, 2, 2);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 0, 971, 80))
        self.frame_2.setStyleSheet(u"background-color: rgb(2, 3, 109);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.textEdit_2 = QTextEdit(self.centralwidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(660, 200, 104, 64))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 967, 33))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(24)
        font4.setBold(False)
        font4.setItalic(False)
        self.menubar.setFont(font4)
        self.menubar.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"")
        self.menuAutolainaus = QMenu(self.menubar)
        self.menuAutolainaus.setObjectName(u"menuAutolainaus")
        self.menuAutolainaus.setFont(font4)
        self.menuAutolainaus.setStyleSheet(u"border-top-color: rgb(12, 12, 129);")
        self.menuK_ytt_ehdot = QMenu(self.menubar)
        self.menuK_ytt_ehdot.setObjectName(u"menuK_ytt_ehdot")
        self.menuK_ytt_ehdot.setFont(font4)
        self.menuK_ytt_ehdot.setStyleSheet(u"background-color: rgb(51, 167, 181);")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.plainTextEdit, self.textEdit)
        QWidget.setTabOrder(self.textEdit, self.plainTextEdit_2)
        QWidget.setTabOrder(self.plainTextEdit_2, self.pushButton)

        self.menubar.addAction(self.menuAutolainaus.menuAction())
        self.menubar.addAction(self.menuK_ytt_ehdot.menuAction())
        self.menuAutolainaus.addSeparator()
        self.menuAutolainaus.addAction(self.actionRekister_ityminen)
        self.menuAutolainaus.addAction(self.actionLainaus)
        self.menuAutolainaus.addAction(self.actionK_ytt_ehdot)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRekister_ityminen.setText(QCoreApplication.translate("MainWindow", u"Rekister\u00f6ityminen", None))
        self.actionLainaus.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.actionK_ytt_ehdot.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"TALLENNA", None))
        self.firstNamelabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi :", None))
        self.lastNamelabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Oppilastunnus :", None))
#if QT_CONFIG(tooltip)
        self.plainTextEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.menuAutolainaus.setTitle(QCoreApplication.translate("MainWindow", u"Autolainaus", None))
        self.menuK_ytt_ehdot.setTitle(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
    # retranslateUi

