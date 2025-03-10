# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'tietokantaTestiKuva.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
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
        MainWindow.setStyleSheet(u"background-color: rgb(139, 62, 83);")
        self.actionedellinen = QAction(MainWindow)
        self.actionedellinen.setObjectName(u"actionedellinen")
        icon = QIcon(QIcon.fromTheme(u"application-exit"))
        self.actionedellinen.setIcon(icon)
        self.actionKaikki = QAction(MainWindow)
        self.actionKaikki.setObjectName(u"actionKaikki")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.firstNameLineEdit = QLineEdit(self.centralwidget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")
        self.firstNameLineEdit.setGeometry(QRect(10, 60, 181, 31))
        self.firstNameLineEdit.setStyleSheet(u"color: rgb(255, 252, 254);\n"
"background-color: rgb(247, 237, 255);")
        self.firstNameiLabel = QLabel(self.centralwidget)
        self.firstNameiLabel.setObjectName(u"firstNameiLabel")
        self.firstNameiLabel.setGeometry(QRect(20, 30, 71, 16))
        self.lastNameLineEdit = QLineEdit(self.centralwidget)
        self.lastNameLineEdit.setObjectName(u"lastNameLineEdit")
        self.lastNameLineEdit.setGeometry(QRect(230, 60, 181, 31))
        self.lastNameLineEdit.setStyleSheet(u"color: rgb(248, 238, 255);\n"
"background-color: rgb(235, 235, 255);\n"
"")
        self.lastNameLabel = QLabel(self.centralwidget)
        self.lastNameLabel.setObjectName(u"lastNameLabel")
        self.lastNameLabel.setGeometry(QRect(240, 30, 101, 21))
        self.savePushButton = QPushButton(self.centralwidget)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(320, 110, 75, 24))
        self.studentPictureLabel = QLabel(self.centralwidget)
        self.studentPictureLabel.setObjectName(u"studentPictureLabel")
        self.studentPictureLabel.setGeometry(QRect(30, 120, 191, 181))
        self.studentPictureLabel.setStyleSheet(u"")
        self.studentPictureLabel.setPixmap(QPixmap(u"student.png"))
        self.studentPictureLabel.setScaledContents(True)
        self.keyPictureabel = QLabel(self.centralwidget)
        self.keyPictureabel.setObjectName(u"keyPictureabel")
        self.keyPictureabel.setGeometry(QRect(200, 160, 131, 111))
        self.keyPictureabel.setPixmap(QPixmap(u"key.png"))
        self.keyPictureabel.setScaledContents(True)
        self.teacherPictureLabel = QLabel(self.centralwidget)
        self.teacherPictureLabel.setObjectName(u"teacherPictureLabel")
        self.teacherPictureLabel.setGeometry(QRect(200, 280, 171, 171))
        self.teacherPictureLabel.setPixmap(QPixmap(u"teacher.png"))
        self.teacherPictureLabel.setScaledContents(True)
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
        self.firstNameLineEdit.textEdited.connect(self.firstNameiLabel.setText)

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
        self.firstNameiLabel.setText(QCoreApplication.translate("MainWindow", u"Etunimi:", None))
        self.lastNameLabel.setText(QCoreApplication.translate("MainWindow", u"Sukunimi:", None))
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.studentPictureLabel.setText("")
        self.keyPictureabel.setText("")
        self.teacherPictureLabel.setText("")
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menutesti.setTitle(QCoreApplication.translate("MainWindow", u"testi", None))
    # retranslateUi

