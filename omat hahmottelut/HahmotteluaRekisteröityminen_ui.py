# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HahmotteluaRekisteröityminen.ui'
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
    QSizePolicy, QStatusBar, QWidget)
import testpictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(846, 736)
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
        self.actionRekister_idy = QAction(MainWindow)
        self.actionRekister_idy.setObjectName(u"actionRekister_idy")
        self.actionKirjaudu_sis_n = QAction(MainWindow)
        self.actionKirjaudu_sis_n.setObjectName(u"actionKirjaudu_sis_n")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.TallennapushButton = QPushButton(self.centralwidget)
        self.TallennapushButton.setObjectName(u"TallennapushButton")
        self.TallennapushButton.setGeometry(QRect(570, 520, 191, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.TallennapushButton.setFont(font1)
        self.TallennapushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);")
        self.tayttotiedotFrame = QFrame(self.centralwidget)
        self.tayttotiedotFrame.setObjectName(u"tayttotiedotFrame")
        self.tayttotiedotFrame.setGeometry(QRect(70, 170, 401, 441))
        self.tayttotiedotFrame.setStyleSheet(u"background-color: rgb(51, 167, 181);")
        self.tayttotiedotFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.tayttotiedotFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.etunimiRekisLlabel = QLabel(self.tayttotiedotFrame)
        self.etunimiRekisLlabel.setObjectName(u"etunimiRekisLlabel")
        self.etunimiRekisLlabel.setGeometry(QRect(30, 30, 121, 41))
        font2 = QFont()
        font2.setPointSize(22)
        self.etunimiRekisLlabel.setFont(font2)
        self.etunimiRekisLlabel.setStyleSheet(u"color: rgb(0, 33, 72);")
        self.sukunimiRekLabel = QLabel(self.tayttotiedotFrame)
        self.sukunimiRekLabel.setObjectName(u"sukunimiRekLabel")
        self.sukunimiRekLabel.setGeometry(QRect(30, 150, 151, 41))
        self.sukunimiRekLabel.setFont(font2)
        self.sukunimiRekLabel.setStyleSheet(u"background-color: rgb(51, 167, 181);\n"
"color: rgb(0, 33, 72);")
        self.oppilastunnusRekLabel = QLabel(self.tayttotiedotFrame)
        self.oppilastunnusRekLabel.setObjectName(u"oppilastunnusRekLabel")
        self.oppilastunnusRekLabel.setGeometry(QRect(30, 270, 211, 51))
        self.oppilastunnusRekLabel.setFont(font2)
        self.oppilastunnusRekLabel.setStyleSheet(u"color: rgb(0, 33, 72);")
        self.oppilastunnusPlainTextEdit_2 = QPlainTextEdit(self.tayttotiedotFrame)
        self.oppilastunnusPlainTextEdit_2.setObjectName(u"oppilastunnusPlainTextEdit_2")
        self.oppilastunnusPlainTextEdit_2.setGeometry(QRect(80, 340, 271, 64))
        self.oppilastunnusPlainTextEdit_2.setFont(font2)
        self.oppilastunnusPlainTextEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.etunimiPlainTextEdit = QPlainTextEdit(self.tayttotiedotFrame)
        self.etunimiPlainTextEdit.setObjectName(u"etunimiPlainTextEdit")
        self.etunimiPlainTextEdit.setGeometry(QRect(80, 80, 271, 61))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setItalic(False)
        self.etunimiPlainTextEdit.setFont(font3)
        self.etunimiPlainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);\n"
"font: 9pt \"Segoe UI\";\n"
"alternate-background-color: rgb(255, 255, 255);")
        self.sukunimiPlainTextEdit = QPlainTextEdit(self.tayttotiedotFrame)
        self.sukunimiPlainTextEdit.setObjectName(u"sukunimiPlainTextEdit")
        self.sukunimiPlainTextEdit.setGeometry(QRect(80, 200, 271, 64))
        self.sukunimiPlainTextEdit.setFont(font2)
        self.sukunimiPlainTextEdit.setStyleSheet(u"color: rgb(2, 2, 2);\n"
"alternate-background-color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 255, 255);")
        self.ylaframe = QFrame(self.centralwidget)
        self.ylaframe.setObjectName(u"ylaframe")
        self.ylaframe.setGeometry(QRect(0, 10, 971, 80))
        self.ylaframe.setStyleSheet(u"background-color: rgb(0, 33, 72);")
        self.ylaframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.ylaframe.setFrameShadow(QFrame.Shadow.Raised)
        self.RekisteritymineLlabel = QLabel(self.ylaframe)
        self.RekisteritymineLlabel.setObjectName(u"RekisteritymineLlabel")
        self.RekisteritymineLlabel.setGeometry(QRect(30, 20, 281, 41))
        font4 = QFont()
        font4.setPointSize(24)
        self.RekisteritymineLlabel.setFont(font4)
        self.studentandkeylabel = QLabel(self.centralwidget)
        self.studentandkeylabel.setObjectName(u"studentandkeylabel")
        self.studentandkeylabel.setGeometry(QRect(530, 250, 271, 231))
        self.studentandkeylabel.setPixmap(QPixmap(u"studentAndKey.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 846, 33))
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
        self.menuK_ytt_ehdot.setGeometry(QRect(455, 147, 255, 98))
        self.menuK_ytt_ehdot.setFont(font5)
        self.menuK_ytt_ehdot.setStyleSheet(u"background-color: rgb(2, 3, 109);\n"
"alternate-background-color: rgb(2, 3, 109);")
        self.menuKirjaudu = QMenu(self.menubar)
        self.menuKirjaudu.setObjectName(u"menuKirjaudu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.etunimiPlainTextEdit, self.sukunimiPlainTextEdit)
        QWidget.setTabOrder(self.sukunimiPlainTextEdit, self.oppilastunnusPlainTextEdit_2)
        QWidget.setTabOrder(self.oppilastunnusPlainTextEdit_2, self.TallennapushButton)

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
        self.TallennapushButton.setText(QCoreApplication.translate("MainWindow", u"TALLENNA", None))
        self.etunimiRekisLlabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi :", None))
        self.sukunimiRekLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi :", None))
        self.oppilastunnusRekLabel.setText(QCoreApplication.translate("MainWindow", u"Oppilastunnus :", None))
#if QT_CONFIG(tooltip)
        self.oppilastunnusPlainTextEdit_2.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.RekisteritymineLlabel.setText(QCoreApplication.translate("MainWindow", u"Rekister\u00f6ityminen", None))
        self.studentandkeylabel.setText("")
        self.menuK_ytt_ehdot.setTitle(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
        self.menuKirjaudu.setTitle(QCoreApplication.translate("MainWindow", u"Kirjaudu", None))
    # retranslateUi

