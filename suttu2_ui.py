# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'suttu2.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QLineEdit, QMainWindow, QMenuBar,
    QPushButton, QSizePolicy, QStatusBar, QWidget)
import testpictures_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(845, 600)
        font = QFont()
        font.setPointSize(24)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"background-color: rgb(117, 51, 65);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 10, 221, 441))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.testausLineEdit = QLineEdit(self.frame)
        self.testausLineEdit.setObjectName(u"testausLineEdit")
        self.testausLineEdit.setGeometry(QRect(20, 240, 161, 51))
        self.testausLineEdit.setFont(font)
        self.testausLineEdit.setStyleSheet(u"color: rgb(0, 0, 0);")
        self.testausLineEdit.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.teacherLabel = QLabel(self.frame)
        self.teacherLabel.setObjectName(u"teacherLabel")
        self.teacherLabel.setGeometry(QRect(20, 20, 171, 191))
        self.teacherLabel.setPixmap(QPixmap(u":/png/uiPictures/teacher.png"))
        self.okPushButton = QPushButton(self.frame)
        self.okPushButton.setObjectName(u"okPushButton")
        self.okPushButton.setGeometry(QRect(40, 330, 131, 41))
        self.okPushButton.setStyleSheet(u"background-color: rgb(168, 109, 216);\n"
"font: 20pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.resetPositionspushButton = QPushButton(self.centralwidget)
        self.resetPositionspushButton.setObjectName(u"resetPositionspushButton")
        self.resetPositionspushButton.setGeometry(QRect(94, 480, 151, 51))
        self.resetPositionspushButton.setStyleSheet(u"background-color: rgb(0, 62, 186);\n"
"color: rgb(4, 4, 4);\n"
"font: 20pt \"Segoe UI\";")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(263, 220, 298, 58))
        self.gridLayout = QGridLayout(self.widget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.lastnameLineEdit = QLineEdit(self.widget)
        self.lastnameLineEdit.setObjectName(u"lastnameLineEdit")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.lastnameLineEdit)

        self.lastFocusPushButton = QPushButton(self.widget)
        self.lastFocusPushButton.setObjectName(u"lastFocusPushButton")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lastFocusPushButton)

        self.firstNameLineEdit = QLineEdit(self.widget)
        self.firstNameLineEdit.setObjectName(u"firstNameLineEdit")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.firstNameLineEdit)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.pushButton_2)


        self.gridLayout.addLayout(self.formLayout, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 845, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.testausLineEdit.setText(QCoreApplication.translate("MainWindow", u"testaus", None))
        self.teacherLabel.setText("")
        self.okPushButton.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.resetPositionspushButton.setText(QCoreApplication.translate("MainWindow", u"palauta", None))
        self.lastFocusPushButton.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"LastFocus", None))
    # retranslateUi

