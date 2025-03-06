# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tietokantaTesti.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QMenu, QMenuBar, QPushButton,
    QSizePolicy, QStatusBar, QWidget)
import testpictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(832, 696)
        font = QFont()
        font.setPointSize(11)
        font.setBold(True)
        MainWindow.setFont(font)
        MainWindow.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        MainWindow.setToolTipDuration(-3000)
        MainWindow.setStyleSheet(u"\n"
"background-color: rgb(51, 167, 181);")
        self.actionedellinen = QAction(MainWindow)
        self.actionedellinen.setObjectName(u"actionedellinen")
        icon = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionedellinen.setIcon(icon)
        self.actionKaikki = QAction(MainWindow)
        self.actionKaikki.setObjectName(u"actionKaikki")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.namesFrame = QFrame(self.centralwidget)
        self.namesFrame.setObjectName(u"namesFrame")
        self.namesFrame.setGeometry(QRect(110, 300, 681, 411))
        self.namesFrame.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.namesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.namesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.lueAvaimmetLabel = QLabel(self.namesFrame)
        self.lueAvaimmetLabel.setObjectName(u"lueAvaimmetLabel")
        self.lueAvaimmetLabel.setGeometry(QRect(380, 60, 221, 61))
        self.lueAvaimmetLabel.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"background-color: rgb(0, 33, 72);")
        self.lueAjokorttiiLabel = QLabel(self.namesFrame)
        self.lueAjokorttiiLabel.setObjectName(u"lueAjokorttiiLabel")
        self.lueAjokorttiiLabel.setGeometry(QRect(60, 60, 231, 61))
        self.lueAjokorttiiLabel.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"background-color: rgb(0, 33, 72);")
        self.lueAjokorttiLineEdit = QLineEdit(self.namesFrame)
        self.lueAjokorttiLineEdit.setObjectName(u"lueAjokorttiLineEdit")
        self.lueAjokorttiLineEdit.setGeometry(QRect(60, 140, 231, 81))
        self.lueAjokorttiLineEdit.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"color: rgb(3, 3, 3);\n"
"background-color: rgb(255, 255, 255);")
        self.lueAvaimmetLineEdit = QLineEdit(self.namesFrame)
        self.lueAvaimmetLineEdit.setObjectName(u"lueAvaimmetLineEdit")
        self.lueAvaimmetLineEdit.setGeometry(QRect(380, 140, 231, 81))
        self.lueAvaimmetLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 24pt \"Segoe UI\";\n"
"color: rgb(7, 7, 7);")
        self.savePushButton = QPushButton(self.namesFrame)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(570, 490, 75, 24))
        self.savePushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);")
        self.valmisPushButton = QPushButton(self.namesFrame)
        self.valmisPushButton.setObjectName(u"valmisPushButton")
        self.valmisPushButton.setGeometry(QRect(100, 240, 211, 61))
        self.valmisPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Segoe UI\";")
        self.takeCarPushButton = QPushButton(self.namesFrame)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(380, 240, 211, 61))
        self.takeCarPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"font: 24pt \"Segoe UI\";")
        self.studentAndKeyLabel = QLabel(self.centralwidget)
        self.studentAndKeyLabel.setObjectName(u"studentAndKeyLabel")
        self.studentAndKeyLabel.setGeometry(QRect(330, -40, 231, 241))
        self.lainausJaPalautusLabel = QLabel(self.centralwidget)
        self.lainausJaPalautusLabel.setObjectName(u"lainausJaPalautusLabel")
        self.lainausJaPalautusLabel.setGeometry(QRect(270, 240, 381, 41))
        self.lainausJaPalautusLabel.setStyleSheet(u"color: rgb(0, 33, 72);\n"
"font: 26pt \"Segoe UI\";")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 832, 33))
        self.menuTiedosto = QMenu(self.menubar)
        self.menuTiedosto.setObjectName(u"menuTiedosto")
        self.menutesti = QMenu(self.menuTiedosto)
        self.menutesti.setObjectName(u"menutesti")
        self.menutesti.setStyleSheet(u"background-color: rgb(42, 69, 188);\n"
"background-color: rgb(65, 67, 158);")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuTiedosto.menuAction())
        self.menuTiedosto.addSeparator()
        self.menuTiedosto.addAction(self.menutesti.menuAction())
        self.menuTiedosto.addSeparator()
        self.menuTiedosto.addAction(self.actionedellinen)
        self.menutesti.addAction(self.actionKaikki)

        self.retranslateUi(MainWindow)
        self.lueAjokorttiiLabel.linkActivated.connect(self.lueAjokorttiLineEdit.setText)
        self.lueAvaimmetLabel.linkActivated.connect(self.lueAvaimmetLineEdit.setText)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
#if QT_CONFIG(tooltip)
        MainWindow.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:11pt; font-weight:700;\">Tallentaa henkil\u00f6n tiedot tietokantaan</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.actionedellinen.setText(QCoreApplication.translate("MainWindow", u"Lopeta", None))
#if QT_CONFIG(shortcut)
        self.actionedellinen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Q", None))
#endif // QT_CONFIG(shortcut)
        self.actionKaikki.setText(QCoreApplication.translate("MainWindow", u"Kaikki", None))
        self.lueAvaimmetLabel.setText(QCoreApplication.translate("MainWindow", u"LUE AVAIMMET", None))
#if QT_CONFIG(tooltip)
        self.lueAjokorttiiLabel.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:26pt; font-weight:700;\">LUE AJOKORTTI</span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.lueAjokorttiiLabel.setText(QCoreApplication.translate("MainWindow", u"LUE AJOKORTTI", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.valmisPushButton.setText(QCoreApplication.translate("MainWindow", u"Valmis", None))
        self.takeCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Ota Auto", None))
        self.studentAndKeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/png/uiPictures/studentAndKey.png\"/></p></body></html>", None))
        self.lainausJaPalautusLabel.setText(QCoreApplication.translate("MainWindow", u"LAINAUS JA PALAUTUS", None))
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menutesti.setTitle(QCoreApplication.translate("MainWindow", u"testi", None))
    # retranslateUi

