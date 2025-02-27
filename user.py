# PYSIDE6-MALLINE SOVELLUKSEN PÄÄIKKUNAN LUOMISEEN
# KÄÄNNETYSTÄ KÄYTTÖLIITTYMÄTIEDOSTOSTA (mainWindow_ui.py)
# =====================================================

# KIRJASTOJEN JA MODUULIEN LATAUKSET
# ----------------------------------
import os # Polkumääritykset
import sys # Käynnistysargumentit
import json # JSON-tiedostojen käsittely

from PySide6 import QtWidgets # Qt-vimpaimet

from lendingModules import sound #äänitoiminnot
from lendingModules import dbOperations # Tietokantatoiminnot
from lendingModules import cipher # Salausmoduuli
 
# mainWindow_ui:n tilalle käännetyn pääikkunan tiedoston nimi
# ilman .py-tiedostopäätettä
from user_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

# Määritellään luokka, joka perii QMainWindow- ja Ui_MainWindow-luokan
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    """A class for creating main window for the application"""
    
    # Määritellään olionmuodostin ja kutsutaan yliluokkien muodostimia
    def __init__(self):
        super().__init__()

        # luodaan säikeistystä varten uusi säievatanto
        #self.treadedPool = QTreatedPool().globalInstance()
    
        # Luodaan käyttöliittymä konvertoidun tiedoston perusteella MainWindow:n ui-ominaisuudeksi. Tämä suojaa lopun MainWindow-olion ylikirjoitukselta, kun ui-tiedostoa päivitetään
        self.ui = Ui_MainWindow()

        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)
        
        # Kutsutaan käyttöliittymän muodostusmetodia setupUi
        self.ui.setupUi(self)

        # Rutiini, joka lukee asetukset, jos ne ovat olemassa
        try:
            # Avataam asetustiedosto ja muutetaan se Python sanakirjaksi
            with open('settings.json', 'rt') as settingsFile: # With sulkee tiedoston automaattisesti
                
                jsonData = settingsFile.read()
                self.currentSettings = json.loads(jsonData)
                
            # Puretaan salasana tietokantaoperaatioita varten  
            self.plainTextPassword = cipher.decryptString(self.currentSettings['password'])
        
        # Jos asetusten luku ei onnistu, näytetään virhedialogi
        except Exception as error:
            title = 'Tietokanta-asetusten luku ei onnistunut'
            text = 'Tietokanta-asetuksien avaaminen ja salasanan purku ei onnistunut'
            detailText = str(error)
            self.openWarning(title, text, detailText)
            
        
        # Ohjelman käynnistyksessä piilotetaan tarpeettomat elementit
        self.setInitialElements()




        # OHJELMOIDUT SIGNAALIT
        # ---------------------


        # Kun lainaa painiketta kutsutaan activateLender-metodia
        self.ui.takeCarPushButton.clicked.connect(self.activateLender)

        #Kun ajokortin viivakoodia painetaan, kutsutaan activateKey-metodia
        self.ui.readIdLineEdit.returnPressed.connect(self.activateKey)
        
        #Kun avaimmenperä on luettu, kutsutaan set lendingData
        self.ui.keyBarcodeLineEdit.returnPressed.connect(self.setLendingData)

        # kun ok painiketta on painettu, tallenna tiedot ja palauta käyttöliittymä alkutilaan
        self.ui.savePushButton.clicked.connect(self.saveLendingData)
        
        #kun palauta painiketta painetaan kutsutaan activateLender-metodia
        self.ui.returnCarPushButton.clicked.connect(self.activateReturnCar)
        
        #kun tallenna painiketta on painettu
        self.ui.savePushButton.clicked.connect(self.saveReturnCarData)
        
        # Kun mykistä painiketta painetaan, kutsutaan mute-metodia
        self.ui.soundOffPushButton.clicked.connect(self.mute)

        # Kun äänipäiniketta painetaan, kutsutaan unmute-metodia
        self.ui.soundOnPushButton.clicked.connect(self.unmute)

        # Kun kumoa painiketta painetaan palautetaan UI-alkutilaan
        self.ui.goBackPushButton.clicked.connect(self.goBack)
  
        
    # OHJELMOIDUT SLOTIT
    # ------------------
    
    #soita parametrina annettu äänitiedosto
    
    
        #Palauta käyttöliittymä alkutilanteeseen
    def setInitialElements(self):
        self.ui.startFrame.show()
        self.ui.ajossaLabel.show()
        self.ui.vapaanaLabel.show()
        self.ui.availablePlainTextEdit.show()
        self.ui.rentedPlainTextEdit.show()
        self.ui.namesFrame.show()
        self.ui.teacherLabel.show()
        self.ui.statusbar.show()
        self.ui.returnCarPushButton.show()
        self.ui.takeCarPushButton.show()
        self.ui.goBackPushButton.hide()
        self.ui.readIdLineEdit.hide()
        self.ui.readIdLineEdit.clear()
        self.ui.keyBarcodeLineEdit.hide()
        self.ui.keyBarcodeLineEdit.clear()
        self.ui.calendarLabel.hide()
        self.ui.clockLabel.hide()
        self.ui.dateLabel.hide()
        self.ui.readIdLabel.hide()
        self.ui.keyBarcodeLabel.hide()
        self.ui.savePushButton.hide()
        self.ui.namesFrame.hide()
        self.ui.timeLabel.hide()
        self.ui.soundOnPushButton.hide()
        self.ui.StudentsNameStatusLabel.hide()
        self.ui.carsInfoStatusLabel.hide()
        self.ui.keyBarcodeReturnLineEdit.hide()
        self.ui.keyBarcodeReturnLineEdit.clear()
        self.ui.lainausInfoframe.hide()
        
    
        
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi

        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            freeVehicles = dbConnection.readAllColumnsFromTable('vapaana')
           # muodostetaan luettelo vapaista autoista createCatalog-metodilla
            catalogData = self.createCatalog(freeVehicles, 'paikkaa')

            self.ui.availablePlainTextEdit.setPlainText(catalogData)
            
        except Exception as e:
            title = 'Autotietojen lukeminen ei onnistu'
            text = 'Vapaiden autojen tiedot eivät ole saatavissa'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)
        
        # TODO: Lisää rutiini joka hakee ajossa olevat autot 
        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            rentedVehicles = dbConnection.readAllColumnsFromTable('ajossa')
           # muodostetaan luettelo vapaista autoista createCatalog-metodilla
            catalogData = self.createCatalog(rentedVehicles)

            self.ui.rentedPlainTextEdit.setPlainText(catalogData)
            
        except Exception as e:
            title = 'Autotietojen lukeminen ei onnistu'
            text = 'Ajossa olevien autojen tiedot eivät ole saatavissa'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)
        
    # Näyttää "lue ajokortti" labolin ja syöttö kentän
    def activateLender(self):
        self.ui.namesFrame.show()
        self.ui.statusLabel.setText('Auton Lainaus')
        self.ui.goBackPushButton.show()
        self.ui.readIdLineEdit.show()
        self.ui.readIdLabel.show()
        self.ui.keyBarcodeLineEdit.hide()
        self.ui.startFrame.hide()
        self.ui.keyBarcodeLabel.hide()
        self.ui.returnCarPushButton.hide()
        self.ui.takeCarPushButton.hide()
        self.ui.statusLabel.show()
        self.ui.savePushButton.hide()
        self.ui.startFrame.hide()
        
    #Näyttää "syätä avain" labolin ja avaimmen syöttö kentän
    def activateKey(self):
        self.ui.keyBarcodeLineEdit.show()
        self.ui.keyBarcodeLabel.show()
        self.ui.keyBarcodeLineEdit.setFocus()
        self.ui.StudentsNameStatusLabel.show()
        self.ui.savePushButton.hide()
    


        #näyttää lainauksen tiedot näytölle
    def setLendingData(self):
        self.ui.carsInfoStatusLabel.show()
        self.ui.dateLabel.show()
        self.ui.calendarLabel.show()
        self.ui.clockLabel.show()
        self.ui.timeLabel.show()
        self.ui.savePushButton.show()
        self.ui.lainausInfoframe.show()
    
       # Tallennetaan lainauksen tiedot ja palautetaan käyttöliittymä alkutilaan
    def saveLendingData(self):
        # Save data to the database
        # Luetaan tietokanta-asetukset paikallisiin muuttujiin
        dbSettings = self.currentSettings
        plainTextPassword = self.plainTextPassword
        dbSettings['password'] = plainTextPassword # Vaidetaan selväkieliseksi

        try:
            # Luodaan tietokantayhteys-olio
            dbConnection = dbOperations.DbConnection(dbSettings)
            ssn = self.ui.readIdLineEdit.text()
            key = self.ui.keyBarcodeLineEdit.text()
            dataDictionary = {'hetu': ssn,
                            'rekisterinumero': key}
            dbConnection.addToTable('lainaus', dataDictionary)

            self.setInitialElements()
            self.ui.statusbar.showMessage('Auton lainaustiedot tallennettiin', 5000)
            if self.soundOn:
                sound.playWav('sounds\\lendingOk.WAV')   
        except Exception as e:
            title = 'Lainaustietojen tallentaminen ei onnistu'
            text = 'Ajokorttin tai auton tiedot virheelliset, ota yhteys henkilökuntaan!'
            detailedText = str(e)
            self.openWarning(title, text, detailedText)
            
    # painettu lainaa-painiketta, kutsutaan activateReturnCar 
    def activateReturnCar(self):
        self.ui.goBackPushButton.show()
        self.ui.startFrame.hide()
        self.ui.namesFrame.show()
        self.ui.statusLabel.setText('Auton palautus')
        self.ui.goBackPushButton.show()
        self.ui.readIdLineEdit.hide()
        self.ui.readIdLabel.hide()
        self.ui.keyBarcodeReturnLineEdit.show()
        self.ui.keyBarcodeLineEdit.hide()
        self.ui.keyBarcodeLabel.show()
        self.ui.returnCarPushButton.hide()
        self.ui.takeCarPushButton.hide()
        self.ui.statusLabel.show()
        self.ui.savePushButton.show()
        self.ui.returnDayLabel.hide()
        self.ui.keyBarcodeReturnLineEdit.setFocus()
        
    # Tallennetaan palautuksen tiedot tietokantaan ja palautetaan UI alkutilaan
    def saveReturnCarData(self):
        self.ui.statusbar.showMessage('auto palautettu')
        self.setInitialElements()
            
    # Mykistetään äänet
    def mute(self):
        self.ui.soundOffPushButton.hide()
        self.ui.soundOnPushButton.show()
        self.ui.statusbar.showMessage('Äänet mykistetty')
        self.soundOn = False
    
    # Poistetaan mykistys
    def unmute(self):
        self.ui.soundOffPushButton.show()
        self.ui.soundOnPushButton.hide()
        self.ui.statusbar.showMessage('Äänet käytössä')
        self.soundOn = True
    
    def goBack(self):
        self.setInitialElements()
        self.ui.statusbar.showMessage('Toiminto peruutettiin', 5000)

    # Metodi monirivisen luettelon muodostamiseen taulu tai näkymän datasta
    def createCatalog(self, tupleList: list, suffix='') -> str:
        """Creates a catalog like text for plainText edits from list of tuples.
        Typically list comes from a database table or view


        Args:
            tupleList (list): list of tuples containing table data
            suffix (str, optional): phraset to add to the end of the line. Defaults to ''.

        Returns:
            str: Plain text for thr catalog
        """
        # määritellään vapaana olevien autojen tiedot
        #availablePlainTextEdit
        catalogData = ''
        rowText = ''
            
        for vehiclTuple in tupleList:
            rowData = ''
            for vehicleData in vehiclTuple:
                rowData = rowData + f'{vehicleData} '
            rowText = rowData + f'{suffix}\n'
            catalogData = catalogData + rowText
        return catalogData

            
    # Avataan MessageBox
    def openWarning(self):
        msgBox = QtWidgets.QMessageBox()
        msgBox.setIcon(QtWidgets.QMessageBox.Critical)
        msgBox.setWindowTitle('Tietokantayhteyttä ei voitu muodostaa!')
        msgBox.setText('Otayhteyttä järjestelmän valvojaan')
        msgBox.setStandardButtons(QtWidgets.QMessageBox.Ok)
        msgBox.exec()


# Luodaan sovellus
app = QtWidgets.QApplication(sys.argv)

# Luodaan objekti pääikkunalle ja tehdään siitä näkyvä
window = MainWindow()
window.show()

# Käynnistetään sovellus ja tapahtumienkäsittelijä (event loop)
app.exec()
