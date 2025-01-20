# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HahmotteluaKirjaudu.ui'
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
        MainWindow.resize(845, 748)
        font = QFont()
        font.setPointSize(26)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(51, 167, 181);\n"
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
        self.actionRekister_idy = QAction(MainWindow)
        self.actionRekister_idy.setObjectName(u"actionRekister_idy")
        self.actionKirjaudu_sis_n = QAction(MainWindow)
        self.actionKirjaudu_sis_n.setObjectName(u"actionKirjaudu_sis_n")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.kirjaudusisnBushButton = QPushButton(self.centralwidget)
        self.kirjaudusisnBushButton.setObjectName(u"kirjaudusisnBushButton")
        self.kirjaudusisnBushButton.setGeometry(QRect(570, 520, 191, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.kirjaudusisnBushButton.setFont(font1)
        self.kirjaudusisnBushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(70, 170, 401, 441))
        self.frame.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.etunimiLabel = QLabel(self.frame)
        self.etunimiLabel.setObjectName(u"etunimiLabel")
        self.etunimiLabel.setGeometry(QRect(30, 30, 121, 41))
        font2 = QFont()
        font2.setPointSize(22)
        font2.setBold(True)
        self.etunimiLabel.setFont(font2)
        self.etunimiLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.sukunimiLabel = QLabel(self.frame)
        self.sukunimiLabel.setObjectName(u"sukunimiLabel")
        self.sukunimiLabel.setGeometry(QRect(30, 150, 151, 41))
        self.sukunimiLabel.setFont(font2)
        self.sukunimiLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.oppilastunnusLabel = QLabel(self.frame)
        self.oppilastunnusLabel.setObjectName(u"oppilastunnusLabel")
        self.oppilastunnusLabel.setGeometry(QRect(30, 260, 211, 51))
        self.oppilastunnusLabel.setFont(font2)
        self.oppilastunnusLabel.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.oppilastunnusPlainTextEdit = QPlainTextEdit(self.frame)
        self.oppilastunnusPlainTextEdit.setObjectName(u"oppilastunnusPlainTextEdit")
        self.oppilastunnusPlainTextEdit.setGeometry(QRect(80, 330, 271, 64))
        font3 = QFont()
        font3.setPointSize(22)
        self.oppilastunnusPlainTextEdit.setFont(font3)
        self.oppilastunnusPlainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.sukunimiLextEdit = QTextEdit(self.frame)
        self.sukunimiLextEdit.setObjectName(u"sukunimiLextEdit")
        self.sukunimiLextEdit.setGeometry(QRect(80, 200, 271, 64))
        self.sukunimiLextEdit.setFont(font3)
        self.sukunimiLextEdit.setStyleSheet(u"color: rgb(2, 2, 2);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.etunimiTextEdit = QTextEdit(self.frame)
        self.etunimiTextEdit.setObjectName(u"etunimiTextEdit")
        self.etunimiTextEdit.setGeometry(QRect(80, 80, 271, 61))
        self.etunimiTextEdit.setFont(font3)
        self.etunimiTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.ylaFrame = QFrame(self.centralwidget)
        self.ylaFrame.setObjectName(u"ylaFrame")
        self.ylaFrame.setGeometry(QRect(0, 10, 841, 80))
        self.ylaFrame.setStyleSheet(u"background-color: rgb(0, 33, 72);")
        self.ylaFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ylaFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.kirjauduLabel = QLabel(self.ylaFrame)
        self.kirjauduLabel.setObjectName(u"kirjauduLabel")
        self.kirjauduLabel.setGeometry(QRect(30, 20, 281, 41))
        font4 = QFont()
        font4.setPointSize(24)
        font4.setBold(True)
        self.kirjauduLabel.setFont(font4)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(530, 250, 271, 231))
        self.label_4.setPixmap(QPixmap(u"studentAndKey.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 845, 33))
        font5 = QFont()
        font5.setFamilies([u"Segoe UI"])
        font5.setPointSize(24)
        font5.setBold(False)
        font5.setItalic(False)
        self.menubar.setFont(font5)
        self.menubar.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"border-top-color: rgb(2, 3, 109);\n"
"")
        self.menuK_ytt_ehdot = QMenu(self.menubar)
        self.menuK_ytt_ehdot.setObjectName(u"menuK_ytt_ehdot")
        self.menuK_ytt_ehdot.setGeometry(QRect(474, 182, 255, 98))
        self.menuK_ytt_ehdot.setFont(font5)
        self.menuK_ytt_ehdot.setStyleSheet(u"background-color: rgb(2, 3, 109);\n"
"alternate-background-color: rgb(2, 3, 109);")
        self.menuKirjaudu = QMenu(self.menubar)
        self.menuKirjaudu.setObjectName(u"menuKirjaudu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.sukunimiLextEdit, self.oppilastunnusPlainTextEdit)
        QWidget.setTabOrder(self.oppilastunnusPlainTextEdit, self.kirjaudusisnBushButton)

        self.menubar.addAction(self.menuK_ytt_ehdot.menuAction())
        self.menubar.addAction(self.menuKirjaudu.menuAction())
        self.menuKirjaudu.addAction(self.actionKirjaudu_sis_n)
        self.menuKirjaudu.addAction(self.actionRekister_idy)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRekister_ityminen.setText(QCoreApplication.translate("MainWindow", u"Kirjautuminen", None))
        self.actionLainaus.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.actionK_ytt_ehdot.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
        self.actionRekister_idy.setText(QCoreApplication.translate("MainWindow", u"Rekister\u00f6idy", None))
        self.actionKirjaudu_sis_n.setText(QCoreApplication.translate("MainWindow", u"Kirjaudu sis\u00e4\u00e4n", None))
        self.kirjaudusisnBushButton.setText(QCoreApplication.translate("MainWindow", u"Kirjaudu sis\u00e4\u00e4n", None))
        self.etunimiLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi :", None))
        self.sukunimiLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi :", None))
        self.oppilastunnusLabel.setText(QCoreApplication.translate("MainWindow", u"Oppilastunnus :", None))
#if QT_CONFIG(tooltip)
        self.oppilastunnusPlainTextEdit.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.kirjauduLabel.setText(QCoreApplication.translate("MainWindow", u"Kirjaudu", None))
        self.label_4.setText("")
        self.menuK_ytt_ehdot.setTitle(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
        self.menuKirjaudu.setTitle(QCoreApplication.translate("MainWindow", u"Kirjaudu", None))
    # retranslateUi

