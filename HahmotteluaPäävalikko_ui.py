# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HahmotteluaPäävalikko.ui'
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
    QMenu, QMenuBar, QPushButton, QSizePolicy,
    QStatusBar, QWidget)
import testpictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(850, 638)
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
        self.actionMy_h_stymis_selvitys = QAction(MainWindow)
        self.actionMy_h_stymis_selvitys.setObjectName(u"actionMy_h_stymis_selvitys")
        self.actionOhje = QAction(MainWindow)
        self.actionOhje.setObjectName(u"actionOhje")
        self.actionKirjaudu_ulos = QAction(MainWindow)
        self.actionKirjaudu_ulos.setObjectName(u"actionKirjaudu_ulos")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.kirjauduulosPushButton = QPushButton(self.centralwidget)
        self.kirjauduulosPushButton.setObjectName(u"kirjauduulosPushButton")
        self.kirjauduulosPushButton.setGeometry(QRect(570, 480, 191, 61))
        font1 = QFont()
        font1.setPointSize(20)
        self.kirjauduulosPushButton.setFont(font1)
        self.kirjauduulosPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);\n"
"alternate-background-color: rgb(238, 44, 130);")
        self.valikkoframe = QFrame(self.centralwidget)
        self.valikkoframe.setObjectName(u"valikkoframe")
        self.valikkoframe.setGeometry(QRect(60, 130, 401, 371))
        self.valikkoframe.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.valikkoframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.valikkoframe.setFrameShadow(QFrame.Shadow.Raised)
        self.valikkoLabel = QLabel(self.valikkoframe)
        self.valikkoLabel.setObjectName(u"valikkoLabel")
        self.valikkoLabel.setGeometry(QRect(30, 30, 201, 41))
        font2 = QFont()
        font2.setPointSize(22)
        self.valikkoLabel.setFont(font2)
        self.lainausPushButton = QPushButton(self.valikkoframe)
        self.lainausPushButton.setObjectName(u"lainausPushButton")
        self.lainausPushButton.setGeometry(QRect(40, 90, 141, 51))
        font3 = QFont()
        font3.setPointSize(24)
        self.lainausPushButton.setFont(font3)
        self.lainausPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);")
        self.palautusPushButton = QPushButton(self.valikkoframe)
        self.palautusPushButton.setObjectName(u"palautusPushButton")
        self.palautusPushButton.setGeometry(QRect(40, 170, 141, 51))
        self.palautusPushButton.setFont(font3)
        self.palautusPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);")
        self.ylaFrame = QFrame(self.centralwidget)
        self.ylaFrame.setObjectName(u"ylaFrame")
        self.ylaFrame.setGeometry(QRect(0, 10, 971, 80))
        self.ylaFrame.setStyleSheet(u"background-color: rgb(0, 33, 72);")
        self.ylaFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.ylaFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.heiOppilaslabel = QLabel(self.ylaFrame)
        self.heiOppilaslabel.setObjectName(u"heiOppilaslabel")
        self.heiOppilaslabel.setGeometry(QRect(30, 20, 411, 41))
        self.heiOppilaslabel.setFont(font3)
        self.studentandkeyLabol = QLabel(self.centralwidget)
        self.studentandkeyLabol.setObjectName(u"studentandkeyLabol")
        self.studentandkeyLabol.setGeometry(QRect(540, 180, 271, 231))
        self.studentandkeyLabol.setPixmap(QPixmap(u"studentAndKey.png"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 850, 33))
        font4 = QFont()
        font4.setFamilies([u"Segoe UI"])
        font4.setPointSize(24)
        font4.setBold(False)
        font4.setItalic(False)
        self.menubar.setFont(font4)
        self.menubar.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"border-top-color: rgb(2, 3, 109);\n"
"")
        self.menuK_ytt_ehdot = QMenu(self.menubar)
        self.menuK_ytt_ehdot.setObjectName(u"menuK_ytt_ehdot")
        self.menuK_ytt_ehdot.setGeometry(QRect(535, 156, 255, 98))
        self.menuK_ytt_ehdot.setFont(font4)
        self.menuK_ytt_ehdot.setStyleSheet(u"background-color: rgb(2, 3, 109);\n"
"alternate-background-color: rgb(2, 3, 109);")
        self.menuKirjaudu = QMenu(self.menubar)
        self.menuKirjaudu.setObjectName(u"menuKirjaudu")
        self.menuKirjaudu_ulos = QMenu(self.menubar)
        self.menuKirjaudu_ulos.setObjectName(u"menuKirjaudu_ulos")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuKirjaudu.menuAction())
        self.menubar.addAction(self.menuKirjaudu_ulos.menuAction())
        self.menubar.addAction(self.menuK_ytt_ehdot.menuAction())
        self.menuKirjaudu.addAction(self.actionRekister_idy)
        self.menuKirjaudu.addAction(self.actionMy_h_stymis_selvitys)
        self.menuKirjaudu.addAction(self.actionOhje)
        self.menuKirjaudu_ulos.addAction(self.actionKirjaudu_ulos)
        self.menuKirjaudu_ulos.addAction(self.actionKirjaudu_sis_n)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionRekister_ityminen.setText(QCoreApplication.translate("MainWindow", u"Kirjautuminen", None))
        self.actionLainaus.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.actionK_ytt_ehdot.setText(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
        self.actionRekister_idy.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.actionKirjaudu_sis_n.setText(QCoreApplication.translate("MainWindow", u"Asetukset", None))
        self.actionMy_h_stymis_selvitys.setText(QCoreApplication.translate("MainWindow", u"Palautus", None))
        self.actionOhje.setText(QCoreApplication.translate("MainWindow", u"Ohje ", None))
        self.actionKirjaudu_ulos.setText(QCoreApplication.translate("MainWindow", u"Kirjaudu ulos", None))
        self.kirjauduulosPushButton.setText(QCoreApplication.translate("MainWindow", u"Kirjaudu Ulos", None))
        self.valikkoLabel.setText(QCoreApplication.translate("MainWindow", u"Valikko", None))
        self.lainausPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.palautusPushButton.setText(QCoreApplication.translate("MainWindow", u"Palautus", None))
        self.heiOppilaslabel.setText(QCoreApplication.translate("MainWindow", u"Hei (oppilaan nimi t\u00e4h\u00e4n)", None))
        self.studentandkeyLabol.setText("")
        self.menuK_ytt_ehdot.setTitle(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
        self.menuKirjaudu.setTitle(QCoreApplication.translate("MainWindow", u"Valikko", None))
        self.menuKirjaudu_ulos.setTitle(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4", None))
    # retranslateUi

