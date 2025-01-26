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
        MainWindow.resize(739, 600)
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
        self.studentAndKeyLabel = QLabel(self.centralwidget)
        self.studentAndKeyLabel.setObjectName(u"studentAndKeyLabel")
        self.studentAndKeyLabel.setGeometry(QRect(460, 240, 231, 241))
        self.namesFrame = QFrame(self.centralwidget)
        self.namesFrame.setObjectName(u"namesFrame")
        self.namesFrame.setGeometry(QRect(10, 20, 541, 171))
        self.namesFrame.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.namesFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.namesFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.firstNameLineEdit = QLineEdit(self.namesFrame)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(50, 60, 181, 31))
        self.firstNameLineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(247, 237, 255);")
        self.lastNameLineEdit = QLineEdit(self.namesFrame)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(270, 60, 181, 31))
        self.lastNameLineEdit.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(235, 235, 255);\n"
"")
        self.lastNameLabel = QLabel(self.namesFrame)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setGeometry(QRect(260, 30, 101, 21))
        self.savePushButton = QPushButton(self.namesFrame)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(410, 130, 75, 24))
        self.savePushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);")
        self.etunimiLabel = QLabel(self.namesFrame)
        self.etunimiLabel.setObjectName(u"etunimiLabel")
        self.etunimiLabel.setGeometry(QRect(50, 40, 49, 16))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 739, 33))
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
        self.studentAndKeyLabel.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><img src=\":/png/studentAndKey.png\"/></p></body></html>", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi:", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.etunimiLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi:", None))
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menutesti.setTitle(QCoreApplication.translate("MainWindow", u"testi", None))
    # retranslateUi

