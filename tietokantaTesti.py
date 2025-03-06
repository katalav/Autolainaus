# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

import lendingModules.dbOperations

from lendingModules import dbOperations

from PySide6 import QtWidgets # Qt-vimpaimet
from tietokantaTesti_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

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

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun tallennuspainiketta on klikattu, kutsutaan -metodia
        # self.ui.savePushButton.clicked.connect(self.saveData)

        # Kun Lainaa-painiketta on painettu, kutsutaan takeCar-metodia
        self.ui.takeCarPushButton.clicked.connect(self.takeCar)

        # Kun Henkilötunnus-kentästä poistutaan enterillä, 
        # tuodaan näkyviin Rekisterinumero-kenttä

        self.ui.ssnLineEdit.returnPressed.connect(self.showKeyLineEdit)

        self.settingsDictionary = {'server': 'localhost',
                      'port': '5432',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty'}
        
        # Piilotetaan kuvat ja syöttökentät sovelluksen käynnistyksessä
        self.ui.lueAvaimmetLabel.hide()
        self.ui.lueAvaimmetLineEdit.hide()
        self.ui.lueAjokorttiLineEdit.hide()
        self.ui.lueAjokorttiiLabel.hide()
        self.ui.studentAndKeyLabel.hide()
        self.ui.valmisPushButton.hide()
        self.ui.namesFrame.hide()


    # OHJELMOIDUT SLOTIT
    # ------------------

    # Tallennetaan syötety tiedot tietokantaan
    def saveData(self):
        dbconnection = dbOperations.DbConnection(self.settingsDictionary)
        data = {'etunimi': self.ui.lastNameLineEdit.text(),
                'sukunimi': self.ui.lastNameLineEdit.text()}
        dbconnection.addToTable('person', data)

        # Määritellään tilarivin teksti, näyttöaika 3 sek.
        message = f'Henkilön {self.ui.lueAjokorttiLineEdit.text()} {self.ui.lueAjokorttiLineEdit.text()} tiedot tallennettiin'
        self.ui.statusbar.showMessage(message, 3000)

        # Tyhjennetään kentät
        self.ui.lueAvaimmetLineEdit.clear()
        self.ui.lueAjokorttiiLabel.clear()
        
    def takeCar(self):

        # Tuodaan lainauksen kuvat ja syöttökentät näkyviin
        self.ui.studentAndKeyLabel.show()
        self.ui.valmisPushButton.show()
        self.ui.lainausJaPalautusLabel.show()
        self.ui.valmisPushButton.hide() # Piilotetaan Palauta-painike

        # Näytetään tilarivillä Ohjeteksti
        message = 'Lue ajokortin viivakoodi'
        self.ui.statusbar.showMessage(message)

    def showKeyLineEdit(self):
        self.ui.keyBarcodeLineEdit.show()
        self.ui.keyBarcodeLineEdit.setFocus()
        message = 'Ota ajokortti pois lukijasta ja laita avaimenperä lukijaan'
    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Tiedot tallennettu')
        msgBox.setText(f'Henkilön {self.ui.lastNameLineEdit.text()} tiedot meinivät tietokantaan')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()

    