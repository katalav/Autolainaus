# CIPHER.PY -MODUULIN YKSIKKÖTESTIT
# ==================================

import pytest # Järjestelmätason virheiden testaus
from lendingModules import cipher #testataan moduulin lataus

plainText = b'Selkokieliteksti'
key = b'yeDCerOn-3YZgtVt1Mp0J36cm_AF3iW9Q3DsaiqOS-g='
cipherEngine = cipher.createChipher(key)
cryptoText = cipher.encrypt(cipherEngine, plainText)

def test_decrypt():
    assert cipher.decrypt(cipherEngine, cryptoText, True) == plainText
    
# TODO: Tee tähän testi decrypString-funktiosta
    
# Luodaan salateksti käyttämällä encryptStringi-funktiota
cryptoText2 = cipher.encryptString('Selkokieliteksti')
#Tehdään testi, joka käyttää decryptString-funktiota
    
def test_decryptString():
    assert cipher.decryptString(cryptoText2)