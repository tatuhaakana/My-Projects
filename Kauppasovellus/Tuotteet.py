class Tuotteet:

    def __init__(self, connection):
        self.conn = connection
        self.cur = self.conn.cursor()

    def HaeKaikkiTuotteet(self):
        try:
            self.cur.execute("SELECT * FROM tuote")
            rivit = self.cur.fetchall()
            self.TulostaTuote(rivit)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan tuote-taulusta: {}.".format(e)) 

    def HaeTuoteNumerolla(self, _hakunro):
        try:
            hakulause = "SELECT tuotenro, nimi, kuvaus FROM tuote where tuotenro = '" + _hakunro + "'"
            hakulause2 = "SELECT tilausnro, kpl FROM tilausrivi where tuotenro = '" + _hakunro + "'"
            self.cur.execute(hakulause)
            rivit = self.cur.fetchall()
            self.cur.execute(hakulause2)
            rivit2 = self.cur.fetchall()
            self.TulostaTuote(rivit)
            self.EtsiTilaus(rivit2)
        except Exception as e:
            print("Rivejä ei pystytty lukemaan tuote-taulusta: {}.".format(e))

    def TulostaTuote(self, rivit):
        print("\nTuotenumero   Nimi                Kuvaus")
        for rivi in rivit:
           print(rivi[0] + "          " + rivi[1] + "             " +rivi[2])

    def EtsiTilaus(self, rivit):
       eka = True
       for rivi in rivit:
            hakulause = "SELECT pvm, asnro FROM tilaus where tilausnro = '" + rivi[0] + "'"
            self.cur.execute(hakulause)
            rivit3 = self.cur.fetchall()
            tilausnro = rivi[0]
            kpl = rivi[1]
            if eka:
                print("Tilausnro     Pvm                 Asiakas             Kpl")
                eka = False
            for rivi in rivit3:
                pvm = rivi[0]
                hakulause4 = "SELECT snimi, enimi FROM asiakas where asnro = '" + rivi[1] + "'"
                self.cur.execute(hakulause4)
                rivit4 = self.cur.fetchall()
                for rivi in rivit4:
                    print(str(tilausnro) + "        " + str(pvm) + "            " + str(rivi[0]) + " " + str(rivi[1]) + "        " + str(kpl))

    def TulostaTilaukset(self, rivit):
        print("Tilausnro      Pvm                 Asiakas             Kpl")
