## Asiakas-luokka

class Asiakas:

    # Asiakkaalla on seuraavat tiedot tietokantataulussa nimeltä asiakas:
    # asnro - asiakasnumero
    # snimi - sukunimi
    # enimi - etunimi
    # email - sähköpostiosoite
    # puh   - puhelinnumero

    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()


    # Asiakkaan haku asiakasnumerolla
    # Tämän sisällä kutsutaan TulostaAsiakas()
    def HaeAsiakasNumerolla(self, _hakunro):
        try:
            hakulause = "SELECT * FROM asiakas where asnro = '" + _hakunro + "'"
            self.cur.execute(hakulause)  
            rivi = self.cur.fetchall()
            self.TulostaAsiakas(rivi)
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))

    # Asiakkaan haku sukunimellä
    def HaeAsiakasNimella(self, _hakunimi):
        try:
            hakulause = "SELECT * FROM asiakas where snimi = '" + _hakunimi + "'"
            self.cur.execute(hakulause)  

            rivi = self.cur.fetchall()
            self.TulostaAsiakas(rivi)
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas-taulusta: {}.".format(e))
      

    # Haetaan kaikki asiakkaat
    # Tämän sisällä kutsutaan TulostaAsiakas()
    def HaeKaikkiAsiakkaat(self):
        try:
            self.cur.execute("SELECT * FROM asiakas")
            rivit = self.cur.fetchall()
            self.TulostaAsiakas(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan asiakas-taulusta: {}.".format(e)) 

    # Tulostetaan 1 asiakas kerrallaan
    # Tänne parametrina rivit, jotka select on hakenut
    def TulostaAsiakas(self, rivit):
        print("\nAsiakasnumero  Nimi                Email                         Puhelin")
        for rivi in rivit:
           print(rivi[0] + "           " + rivi[2] + " " +rivi[1] + "        " + rivi[3] + "          " + str(rivi[4]))
           

    # Tulostetaan 1 asiakkaan kaikki tilaukset
    def TulostaAsiakkaanTilaukset(self, _hakunro):
        eka = True
        try:
            hakulause = "SELECT asiakas.asnro, tilausnro, pvm FROM asiakas, tilaus where asiakas.asnro = tilaus.asnro and asiakas.asnro = '" + _hakunro + "'"
            self.cur.execute(hakulause)  
            rivit = self.cur.fetchall()
            for rivi in rivit:
                if (eka):
                    print("Tilausnro      Pvm")
                    eka = False 
                print(str(rivi[1]) + "         " + str(rivi[2]))
        except Exception as e:
            print("Riviä ei pystytty lukemaan asiakas- tai tilaus-taulusta: {}.".format(e))