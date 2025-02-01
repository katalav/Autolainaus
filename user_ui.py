# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user.ui'
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
        MainWindow.resize(811, 764)
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
        self.namesFrame.setGeometry(QRect(70, 230, 681, 441))
        self.namesFrame.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.savePushButton = QPushButton(self.namesFrame)
        self.savePushButton.setObjectName(u"savePushButton")
        self.savePushButton.setGeometry(QRect(570, 490, 75, 24))
        self.savePushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);")
        self.valmisPushButton = QPushButton(self.namesFrame)
        self.valmisPushButton.setObjectName(u"valmisPushButton")
        self.valmisPushButton.setGeometry(QRect(440, 320, 161, 61))
        self.valmisPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"font: 28pt \"Segoe UI\";")
        self.LueAjokorttiLineEdit = QLineEdit(self.namesFrame)
        self.LueAjokorttiLineEdit.setObjectName(u"LueAjokorttiLineEdit")
        self.LueAjokorttiLineEdit.setGeometry(QRect(60, 220, 231, 71))
        self.LueAjokorttiLineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"font: 22pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.LueAvainLineEdit = QLineEdit(self.namesFrame)
        self.LueAvainLineEdit.setObjectName(u"LueAvainLineEdit")
        self.LueAvainLineEdit.setGeometry(QRect(390, 220, 231, 71))
        self.LueAvainLineEdit.setStyleSheet(u"font: 28pt \"Segoe UI\";\n"
"background-color: rgb(255, 255, 255);\n"
"color: rgb(0, 0, 0);")
        self.lueAjokorttiLabel = QLabel(self.namesFrame)
        self.lueAjokorttiLabel.setObjectName(u"lueAjokorttiLabel")
        self.lueAjokorttiLabel.setGeometry(QRect(70, 140, 211, 51))
        self.lueAjokorttiLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"background-color: rgb(0, 33, 72);")
        self.lueAjokorttiLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lueAvainLabel = QLabel(self.namesFrame)
        self.lueAvainLabel.setObjectName(u"lueAvainLabel")
        self.lueAvainLabel.setGeometry(QRect(400, 140, 211, 51))
        self.lueAvainLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";\n"
"background-color: rgb(0, 33, 72);")
        self.lueAvainLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.teacherLabel = QLabel(self.centralwidget)
        self.teacherLabel.setObjectName(u"teacherLabel")
        self.teacherLabel.setGeometry(QRect(20, 20, 151, 151))
        self.teacherLabel.setPixmap(QPixmap(u"uiPictures/teacher.png"))
        self.teacherLabel.setScaledContents(True)
        self.soundOffushButton = QPushButton(self.centralwidget)
        self.soundOffushButton.setObjectName(u"soundOffushButton")
        self.soundOffushButton.setGeometry(QRect(650, 10, 71, 81))
        icon1 = QIcon()
        icon1.addFile(u"uiPictures/voiceOff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundOffushButton.setIcon(icon1)
        self.soundOffushButton.setIconSize(QSize(48, 48))
        self.soundOnPushButton = QPushButton(self.centralwidget)
        self.soundOnPushButton.setObjectName(u"soundOnPushButton")
        self.soundOnPushButton.setGeometry(QRect(650, 10, 75, 81))
        icon2 = QIcon()
        icon2.addFile(u"uiPictures/voiceOn.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.soundOnPushButton.setIcon(icon2)
        self.soundOnPushButton.setIconSize(QSize(38, 38))
        self.statusLabel = QLabel(self.centralwidget)
        self.statusLabel.setObjectName(u"statusLabel")
        self.statusLabel.setGeometry(QRect(260, 20, 281, 71))
        self.statusLabel.setStyleSheet(u"font: 28pt \"Segoe UI\";\n"
"color: rgb(0, 33, 72);")
        self.statusLabel.setScaledContents(False)
        self.statusLabel.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.takeCarPushButton = QPushButton(self.centralwidget)
        self.takeCarPushButton.setObjectName(u"takeCarPushButton")
        self.takeCarPushButton.setGeometry(QRect(190, 110, 211, 61))
        self.takeCarPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);\n"
"color: rgb(255, 255, 255);\n"
"font: 24pt \"Segoe UI\";")
        self.returnCarPushButton = QPushButton(self.centralwidget)
        self.returnCarPushButton.setObjectName(u"returnCarPushButton")
        self.returnCarPushButton.setGeometry(QRect(460, 110, 211, 61))
        self.returnCarPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);\n"
"font: 24pt \"Segoe UI\";")
        self.PalaaTakaisinPushButton = QPushButton(self.centralwidget)
        self.PalaaTakaisinPushButton.setObjectName(u"PalaaTakaisinPushButton")
        self.PalaaTakaisinPushButton.setGeometry(QRect(500, 130, 251, 61))
        font1 = QFont()
        font1.setPointSize(24)
        self.PalaaTakaisinPushButton.setFont(font1)
        self.PalaaTakaisinPushButton.setStyleSheet(u"\n"
"background-color: rgb(0, 33, 72);\n"
"")
        icon3 = QIcon()
        icon3.addFile(u":/png/uiPictures/goBackArrow.drawio", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.PalaaTakaisinPushButton.setIcon(icon3)
        self.PalaaTakaisinPushButton.setIconSize(QSize(24, 24))
        self.timeLabel = QLabel(self.centralwidget)
        self.timeLabel.setObjectName(u"timeLabel")
        self.timeLabel.setGeometry(QRect(510, 20, 121, 41))
        self.timeLabel.setStyleSheet(u"font: 20pt \"Segoe UI\";")
        self.dateLabel = QLabel(self.centralwidget)
        self.dateLabel.setObjectName(u"dateLabel")
        self.dateLabel.setGeometry(QRect(160, 20, 151, 41))
        self.dateLabel.setStyleSheet(u"font: 22pt \"Segoe UI\";")
        self.clockLabel = QLabel(self.centralwidget)
        self.clockLabel.setObjectName(u"clockLabel")
        self.clockLabel.setGeometry(QRect(110, 170, 41, 41))
        self.clockLabel.setPixmap(QPixmap(u":/png/clock.drawio"))
        self.clockLabel.setScaledContents(True)
        self.calendarLabel = QLabel(self.centralwidget)
        self.calendarLabel.setObjectName(u"calendarLabel")
        self.calendarLabel.setGeometry(QRect(40, 170, 31, 41))
        self.calendarLabel.setPixmap(QPixmap(u":/png/calendar.drawio"))
        self.calendarLabel.setScaledContents(True)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 811, 33))
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
        self.savePushButton.setText(QCoreApplication.translate("MainWindow", u"Tallenna", None))
        self.valmisPushButton.setText(QCoreApplication.translate("MainWindow", u"Valmis", None))
        self.LueAjokorttiLineEdit.setText("")
        self.LueAvainLineEdit.setText("")
        self.lueAjokorttiLabel.setText(QCoreApplication.translate("MainWindow", u"Lue ajokortti", None))
        self.lueAvainLabel.setText(QCoreApplication.translate("MainWindow", u"Lue avain", None))
        self.teacherLabel.setText("")
        self.soundOffushButton.setText("")
        self.soundOnPushButton.setText("")
        self.statusLabel.setText(QCoreApplication.translate("MainWindow", u"Autonlainaus", None))
        self.takeCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.returnCarPushButton.setText(QCoreApplication.translate("MainWindow", u"Palautus", None))
        self.PalaaTakaisinPushButton.setText(QCoreApplication.translate("MainWindow", u"Palaa Takaisin", None))
        self.timeLabel.setText(QCoreApplication.translate("MainWindow", u"09:51", None))
        self.dateLabel.setText(QCoreApplication.translate("MainWindow", u"31.01.2025", None))
        self.clockLabel.setText("")
        self.calendarLabel.setText("")
        self.menuTiedosto.setTitle(QCoreApplication.translate("MainWindow", u"Tiedosto", None))
        self.menutesti.setTitle(QCoreApplication.translate("MainWindow", u"testi", None))
    # retranslateUi

