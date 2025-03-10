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
from suttu2_ui import Ui_MainWindow # Käännetyn käyttöliittymän luokka

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
        self.lastEditedElementName = 'Ei mikään'

        # OHJELMOIDUT SIGNAALIT
        # ---------------------
        
        # Kun Tulosta-painiketta on klikattu, kutsutaan updatePrintedLabel-metodia
        self.ui.okPushButton.clicked.connect(self.buttonPressSlot)
        
        # kun Palautapainiketta on painettu siirrä ikkuna takaisin
        self.ui.resetPositionspushButton.clicked.connect(self.resetPositions)

    # kun kenttä menettää fokuksen kirjoitetaan kentän nimi ominaisuuteen tastEditedElement
        self.ui.lastnameLineEdit.editingFinished.connect(self.setLastEditedElement)
        
        
        # LAst Focus- painike
        self.ui.lastFocusPushButton.clicked.connect(self.showLastElemenentName)
   
   
    # OHJELMOIDUT SLOTIT
    # ------------------

    # Muutetaan tulostettuLabel:n sisältö: teksti ja väri
    
    def setLastEditedElement(self):
        self.lastEditedElementName = 'firstNameLineEdit'

        
    def showLastElemenentName(self):
        message = f'viimeksi käytetty kenttä on{self.lastEditedElementName}'
        self.ui.statusbar.showMessage(message)
        element =self.findChild(QtWidgets.QLineEdit, self.lastEditedElementName)
        element.setFocud()
        
    def buttonPressSlot(self):
        self.ui.statusbar.showMessage('Painoit sitte nappulaa..', 500)
        self.ui.frame.move(300, 300)
        self.ui.teacherLabel.move(100, 100)
        height =self.ui.centralwidget.height()
        width = self.ui.centralwidget.width()
        #tää kertoo korkeus ja leveys pikselit joista näkee sit minkä kokonen ikkuna on.
        message= f'ikkunan korkeus on {height} ja leveys on {width}'
        self.ui.statusbar.showMessage(message, 5000)
        
        
    def resetPositions(self):
        self.ui.frame.move(0, 0)
        self.ui.teacherLabel.move(0, 10)
        
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

    