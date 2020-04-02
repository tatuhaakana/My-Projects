import sqlite3
from sqlite3 import Error

from Asiakas import Asiakas
from Tilaus import Tilaus
from Tuotteet import Tuotteet


def create_connection(db_file):
    ## Esimerkki sivustolta: https://www.sqlitetutorial.net/sqlite-python/ 
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
 
    return conn
 
 
# Funktio, joka tulostaa valikon, ja palauttaa tehdyn valinnan
def valikko():
    print("\nKauppa-tietokannan raportointisovellus")
    print("1 - Listaa kaikki asiakkaat")
    print("2 - Listaa kaikki tuotteet")
    print("3 - Listaa kaikki halutun asiakkaan tilaukset")
    print("4 - Listaa kaikki halutun tuotteen tilaukset")
    print("5 - Listaa halutun tilauksen tilausrivit")
    print("6 - Listaa kaikki tilaukset halutusta päivämäärästä lähtien")
    print("0 - lopeta")
    jatka = input("Anna valinta: ")
    return jatka
 



### PÄÄOHJELMA ###

## Laita tähän se polku, jossa kauppa.db on omalla koneellasi
tietokanta = r"C:\Users\Intel\source\repos\Kauppasovellus\kauppa.db"

# luodaan yhteys tietokantaan
conn = create_connection(tietokanta)
 
if conn is not None:  # Mikäli tietokantayhteys saatiin luotua:
       
    jatka = valikko()
    while jatka != "0":
        if jatka == "1":
            asi = Asiakas(conn)
            asi.HaeKaikkiAsiakkaat()
        elif jatka == "2":
            tte = Tuotteet(conn)
            tte.HaeKaikkiTuotteet()
        elif jatka == "3":
            asi = Asiakas(conn)
            numero = input("Hakuehto: ")
            asi.HaeAsiakasNumerolla(numero)
            asi.TulostaAsiakkaanTilaukset(numero)
        elif jatka == "4":
            tte = Tuotteet(conn)
            numero = input("Hakuehto: ")
            tte.HaeTuoteNumerolla(numero)
        elif jatka == "5":
            til = Tilaus(conn)
            numero = input("Hakuehto: ")
            til.HaeTilausNumerolla(numero)
        elif jatka == "6":
            til = Tilaus(conn)
            numero = input("Hakuehto: ")
            til.HaeTilausNumerolla(numero)
        else:
            print("Virheellinen valinta")

        jatka = valikko()
            
    conn.close()   # suljetaan yhteys

else:
    print("Virhe! Yhteyttä tietokantaan ei voida luoda.")




    
        #elif jatka == "2":
        #    asiakas = Asiakas(conn)
        #    nimi = input("Anna asiakkaan sukunimi: ")
        #    asiakas.HaeAsiakasNimella(nimi)