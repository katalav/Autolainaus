# TIETOKANTA YHTEYKSIEN TESTAUS
# ============================

import pytest # virheilmoituksen testaus vaatii 
from lendingModules import dbOperations # varsinainen testattava moduuli

settingsDictionary = {'server': 'localhost', 
                      'port': '5432',
                      'database': 'autolainaus',
                      'userName': 'postgres',
                      'password': 'Q2werty' }

newVolues = {'etunimi': 'Calle',
             'sukunimi':'Keckerlberg'}

newVolues = {'etunimi': 'Herkko',
             'sukunimi':'Hyväusko'}


dbConnection = dbOperations.DbConnection(settingsDictionary)

# : luo tietokanta yhteys-objekti testejä varten
def test_connectionString():
    assert dbConnection.connectionString == f'dbname=testaus user=postgres password=Q2werty host=localhost port=5432'
#  Testaa, että yhteysmerkkijono muodostuu oikein
def test_readOneRow():
    resultList = dbConnection.readAllColumnsFromTable('person') # Hakee taulun kaikki rivit listaan
    assert resultList[0] ==(1,'Ville', 'Virtanen')# Ensimmäinen rivi pitäisi olla 1 Ville Virtanen

# TODO: Testataan tietueen / rivin (record / row) lisäys tauluun (table)

def test_addRow():
    dbConnection.addToTable('person', newVolues)
    resultList = dbConnection.readAllColumnsFromTable('person')
    rowCount = len(resultList)
    assert resultList[rowCount] == (rowCount, 'Herkko', 'Hyväusko')
    
    