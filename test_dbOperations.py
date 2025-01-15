# TIETOKANTA YHTEYKSIEN TESTAUS
# ============================

import pytest # virheilmoituksen testaus vaatii 
import dbOperations # varsinainen testattava moduuli

settingsDictionary = {'server': 'localhost', 
                      'port': '5432',
                      'database': 'testaus',
                      'userName': 'postgres',
                      'password': 'Q2werty' }

dbConnection = dbOperations.DbConnection(settingsDictionary)

# TODO: luo tietokanta yhteys-objekti testejä varten
def test_connectionString():
    assert dbConnection.connectionString == f'dbname=testaus user=postgres password=Q2werty host=localhost port=5432'
# TODO: Testaa, että yhteysmerkkijono muodostuu oikein


# TODO: Mieti mitä muita testejä pitää kirjoittaa.
    