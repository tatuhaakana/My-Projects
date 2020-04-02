## Tilaus-luokka

class Tilaus:
    # Tilauksella on seuraavat tiedot tietokantataulussa nimeltä tilaus:
    # tilausnro - tilausnumero
    # pvm       - tilauksen päivämäärä, muodossa ppkkvvvv
    # asnro     - tilauksen tehneen asiakkaan asiakasnumero

    # Parametrisoitu muodostinfunktio - constructor
    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()


    # Haetaan kaikki tilaukset
    # Tämän sisällä kutsutaan TulostaTilaus()
    def HaeKaikkiTilaukset(self):
        try:
            self.cur.execute("SELECT asiakas.snimi, pvm, tilausnro FROM tilaus, asiakas where asiakas.asnro = tilaus.asnro")
            rivit = self.cur.fetchall()
            self.TulostaTilaus(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan tilaus-taulusta: {}.".format(e)) 

    def HaeTilausNumerolla(self, _hakunro):
        try:
            hakulause = "SELECT tilausnro, pvm, asnro FROM tilaus where tilausnro = '" + _hakunro + "'"
            hakulause2 = "SELECT tuotenro, kpl FROM tilausrivi where tilausnro = '" + _hakunro + "'"
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            self.cur.execute(hakulause2)
            rivit2 = self.cur.fetchall()
            self.TulostaTilaus(rivit)
            self.TulostaTilausrivi(rivit2)
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))

    # Tulostetaan 1 asiakas kerrallaan
    # Tänne parametrina rivit, jotka select on hakenut
    def TulostaTilaus(self, rivit):
        print("\nTilausnumero   Pvm               Asiakasnumero")
        for rivi in rivit:
            print(str(rivi[0])+ "         " + str(rivi[1]) + "          " + str(rivi[2]))

    def TulostaTilausrivi(self, rivit):
        print("Tuotenumero    Kpl")
        for rivi in rivit:
            print(str(rivi[0]) + "           " + str(rivi[1]))
