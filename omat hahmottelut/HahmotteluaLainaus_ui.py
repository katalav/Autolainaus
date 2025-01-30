# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'HahmotteluaLainaus.ui'
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
        MainWindow.resize(844, 661)
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
        self.lueavainframe = QFrame(self.centralwidget)
        self.lueavainframe.setObjectName(u"lueavainframe")
        self.lueavainframe.setGeometry(QRect(40, 150, 581, 441))
        self.lueavainframe.setStyleSheet(u"background-color: rgb(51, 167, 181);")
        self.lueavainframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.lueavainframe.setFrameShadow(QFrame.Shadow.Raised)
        self.lueViivakoodiLabol = QLabel(self.lueavainframe)
        self.lueViivakoodiLabol.setObjectName(u"lueViivakoodiLabol")
        self.lueViivakoodiLabol.setGeometry(QRect(30, 30, 321, 41))
        font1 = QFont()
        font1.setPointSize(22)
        self.lueViivakoodiLabol.setFont(font1)
        self.viivakoodiFrame = QFrame(self.lueavainframe)
        self.viivakoodiFrame.setObjectName(u"viivakoodiFrame")
        self.viivakoodiFrame.setGeometry(QRect(30, 90, 301, 80))
        self.viivakoodiFrame.setStyleSheet(u"background-color: rgb(26, 84, 91);")
        self.viivakoodiFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.viivakoodiFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.esimerkkilabel = QLabel(self.viivakoodiFrame)
        self.esimerkkilabel.setObjectName(u"esimerkkilabel")
        self.esimerkkilabel.setGeometry(QRect(20, 20, 281, 41))
        self.lainaaPushButton = QPushButton(self.lueavainframe)
        self.lainaaPushButton.setObjectName(u"lainaaPushButton")
        self.lainaaPushButton.setGeometry(QRect(310, 250, 141, 51))
        font2 = QFont()
        font2.setPointSize(24)
        self.lainaaPushButton.setFont(font2)
        self.lainaaPushButton.setStyleSheet(u"background-color: rgb(238, 44, 130);")
        self.okTaiErrorLabel = QLabel(self.lueavainframe)
        self.okTaiErrorLabel.setObjectName(u"okTaiErrorLabel")
        self.okTaiErrorLabel.setGeometry(QRect(200, 190, 101, 41))
        self.okTaiErrorLabel.setStyleSheet(u"background-color: rgb(0, 98, 117);")
        self.ylaframe = QFrame(self.centralwidget)
        self.ylaframe.setObjectName(u"ylaframe")
        self.ylaframe.setGeometry(QRect(0, 10, 971, 80))
        self.ylaframe.setStyleSheet(u"background-color: rgb(0, 33, 72);")
        self.ylaframe.setFrameShape(QFrame.Shape.StyledPanel)
        self.ylaframe.setFrameShadow(QFrame.Shadow.Raised)
        self.LainausLabel = QLabel(self.ylaframe)
        self.LainausLabel.setObjectName(u"LainausLabel")
        self.LainausLabel.setGeometry(QRect(30, 20, 411, 41))
        self.LainausLabel.setFont(font2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 844, 33))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(24)
        font3.setBold(False)
        font3.setItalic(False)
        self.menubar.setFont(font3)
        self.menubar.setStyleSheet(u"font: 24pt \"Segoe UI\";\n"
"border-top-color: rgb(2, 3, 109);\n"
"")
        self.menuK_ytt_ehdot = QMenu(self.menubar)
        self.menuK_ytt_ehdot.setObjectName(u"menuK_ytt_ehdot")
        self.menuK_ytt_ehdot.setGeometry(QRect(535, 156, 255, 98))
        self.menuK_ytt_ehdot.setFont(font3)
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
        self.lueViivakoodiLabol.setText(QCoreApplication.translate("MainWindow", u"Lue Avainten Viivakoodi", None))
        self.esimerkkilabel.setText(QCoreApplication.translate("MainWindow", u"T\u00e4h\u00e4n kamera valinta ja k\u00e4sinkirjoitus vaihtoehto", None))
        self.lainaaPushButton.setText(QCoreApplication.translate("MainWindow", u"Lainaa", None))
        self.okTaiErrorLabel.setText(QCoreApplication.translate("MainWindow", u"   OK TAI ERROR", None))
        self.LainausLabel.setText(QCoreApplication.translate("MainWindow", u"Lainaus", None))
        self.menuK_ytt_ehdot.setTitle(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00f6ehdot", None))
        self.menuKirjaudu.setTitle(QCoreApplication.translate("MainWindow", u"Valikko", None))
        self.menuKirjaudu_ulos.setTitle(QCoreApplication.translate("MainWindow", u"K\u00e4ytt\u00e4j\u00e4", None))
    # retranslateUi

