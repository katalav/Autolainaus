# ESIMERKKI TIEDOSTOKANTATESTEIHIN SOVELTUVASTA
# KÄYTTÖLIITTYMÄSTÄ QT-YMPÄRISTÖSSÄ
#==================================


# KIRJASTOJEN JA MODUULIEN LATAUS
#---------------------------------

import tietokantaTesti_ui
# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit

import dbOperations 

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

        
        # Kun Tulosta-painiketta on klikattu, kutsutaan updatePrintedLabel-metodia
        self.ui.savePushButton.clicked.connect(self.saveData)
        
        self.settingsDictionary = {'server': 'localhost', 
                      'port': '5432',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty' }
        
        #Piilotetaan kuvat ja syöttökentät sovelluksen käynnis?jatkui?
        self.ui.teacherPictureLabel.hide()
        self.ui.keyPictureabel.hide()
        # täs oli jotain vielä
        self.ui.studentPictureLabel()
        
    # OHJELMOIDUT SLOTIT
    # ------------------
    
        # Tallennetaan syötetyt tietokantaan
    def saveData(self): 
        dbconnection = dbOperations.DbConnection(self.settingsDictionary)
        data = {'etunimi': self.ui.firstNameLineEdit.text(), 
                'sukunimi': self.ui.lastNameLineEdit.text()}
        dbconnection.addToTable('person', data)
        
        #määritellään tilarivin tekstit,näyttöaika 3sek.
        
        message = f'Henkilön {self.ui.firstNameLineEdit.text()} {self.ui.lastNameLineEdit.text()} tiedot tallennettiin'
        self.ui.statusbar.showMessage(message, 3000)
        
        #Tyhennetään kentät? wut is this
        self.ui.firstNameLineEdit.clear()
        self.ui.lastNameLineEdit.clear()
        
    def takeCar(self):
    
            # Tuodaan lainauksen kuvat ja syöttökentät näkyviin
        self.ui.teacherPictureLabel.show()
        self.ui.keyPictureLabel.show()
        self.ui.ssnLineEdit.show()
        self.ui.returnCarPushButton.hide() # Piilotetaan Palauta-painike
        
        
        # Näytetään tilarivillä Ohjeteksti
        message = 'Lue ajokortin viivakoodi ensin ja sen jälkeen avaimen viivakoodi'
        self.ui.statusbar.showMessage(message)

    def showKeyLineEdit(self):
        self.ui.keyBarcodeLineEdit.show()
        self.ui.keyBarcodeLineEdit.setFocus()

    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Information)
        msgBox.setWindowTitle('Tiedot tallennettu!')
        msgBox.setText(f'Henkilön {self.ui.lastNameLineEdit.text()}: tiedot menivät tietokantaan')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä
app.exec()

    