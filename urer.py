# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

from PySide6 import QtWidgets # Qt-vimpaimet

# mainWindow_ui:n tilalle käännetyn pääikkunan tiedoston nimi
# ilman .py-tiedostopäätettä
from user_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)
        
        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        self.ui.PalaaTakaisinPushButton.hide()
        self.ui.LueAjokorttiLineEdit.hide()
        self.ui.LueAvainLineEdit.hide()
        self.ui.calendarLabel.hide()
        self.ui.clockLabel.hide()
        self.ui.dateLabel.hide()
        self.ui.lueAjokorttiLabel.hide()
        self.ui.lueAvainLabel.hide()
        self.ui.savePushButton.hide()
        self.ui.namesFrame.hide()
        self.ui.timeLabel.hide()
        self.ui.valmisPushButton.hide()
        self.ui.soundOnPushButton.hide()




        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun Tulosta-painiketta on klikattu, kutsutaan updatePrintedLabel-metodia
        self.ui.takeCarPushButton.clicked.connect(self.activateLender)
        self.ui.valmisPushButton.clicked.connect(self.activateLender)


        
        # self.ui.tulostaPushButton.clicked.connect(self.updatePrintedLabel)

        
   
   
    # OHJELMOIDUT SLOTIT
    # ------------------
    #auton lainaus
    def activateLender(self):
        self.ui.namesFrame.show()
        self.ui.statusLabel.setText('Auton Lainaus')
        self.ui.PalaaTakaisinPushButton.show()
        self.ui.lueAjokorttiLabel.show()
        self.ui.LueAjokorttiLineEdit.show()
        self.ui.LueAvainLineEdit.show()
        self.ui.lueAvainLabel.show()
        self.ui.returnCarPushButton.hide()
        self.ui.takeCarPushButton.hide()
        self.ui.statusLabel.show()
        self.ui.valmisPushButton.show()
        
    #auton palautus


    

        #Kun Lue ajokortti on täytetty siirretään lue avain kohtaan
    
    
    
    # Muutetaan tulostettuLabel:n sisältö: teksti ja väri
    def updatePrintedLabel(self):
        self.ui.tulostettuLabel.setText('Tulostettu')
        self.ui.tulostettuLabel.setStyleSheet(u"color: rgb(0, 255, 0);")

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Hirveetä!')
        msgBox.setText('Jotain kamalaa tapahtui')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()
