from flask import Flask
from flask import render_template
from collections import Counter
from random import randint
from random import shuffle
from flask import request, redirect
from jinja2 import Template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData, create_engine
from sqlalchemy import text
from sqlalchemy.orm import sessionmaker
from gracz import Gracz
from partia import Partia

app = Flask(__name__)

# polaczenie z baza
engine = create_engine('sqlite:///./Gra.db', connect_args={'check_same_thread': False})

META_DATA = MetaData(bind=engine)

c = engine.connect()
META_DATA.reflect()


# select kart z tabel
hero = META_DATA.tables['Hero_1']
hero_laczenie = META_DATA.tables['Hero_laczenie']
reka = META_DATA.tables['Reka']

Session = sessionmaker(bind = engine)
session = Session()

# result dla poczatkowej reki
reka_select = reka.select()
a = engine.execute(reka_select)
result2 = a.fetchall()

#result dla wszystkich kart
hero_select = hero.select()
c=engine.execute(hero_select)
result= c.fetchall()

reka_pieniadze = text("SELECT SUM(Monety) as monety FROM Reka")
# text("SELECT Monety FROM REKA")
# text("SELECT SUM(Monety) as monety FROM Reka")
b = engine.execute(reka_pieniadze)
result_monety = b.fetchall


class Partia:
    def __init__(self, imiona=['Ala', 'Bob']):
        self.sklep_talia = [i[0] for i in result]
        self.sklep_wystawione = []
        self.gracze = [Gracz(imie) for imie in imiona if imie]
        self.sprzedane = []
        self.talia()
        self.potasuj()
        self.wystaw()
        self.cena()
        # self.sprzedaj()

    def talia(self):
        del self.sklep_talia[-10:]

    def zdjecie_wyswietl(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.sklep_wystawione)).all()
        qur2 = sorted(qur2, key=lambda o: self.sklep_wystawione.index(o.ID))
        zdjecie = ([i.Zdjecie for i in qur2])
        return zdjecie

    def potasuj(self):
        shuffle(self.sklep_talia)

    def wystaw(self):
        ilosc = len(self.sklep_wystawione)
        if ilosc != 5:
            self.sklep_wystawione.extend(self.sklep_talia[:(5 - ilosc)])
            del self.sklep_talia[:(5 - ilosc)]

    def karta(self, sprzedane):
        if len(self.sklep_wystawione) != 0:
            self.sprzedane = [self.sklep_wystawione[x] for x in sprzedane]
            return self.sprzedane
        else:
            print("koniec sklepu")
        return

    def aktualizuj_sklep(self, kupione):
        aktualizacja_sklepu = [x for x in self.sklep_wystawione if x not in kupione]
        self.sklep_wystawione = aktualizacja_sklepu

    def cena(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.sklep_wystawione)).all()
        qur2 = sorted(qur2, key=lambda o: self.sklep_wystawione.index(o.ID))
        cena = ([i.Cena for i in qur2])
        return cena
    def atak(self,atak):
        return atak

    def przegrane(self, i):
        del self.gracze[i]

class Gracz:
    def __init__(self, imie='Nieznane'):
        self.nazwa = imie
        self.talia = [i[0] for i in result]
        self.reka = []
        self.odrzucone = []
        self.kupione=[]
        self.zielone = []
        self.lista = []
        self.monety = 0
        self.atak = 0
        self.zycie = 2
        self.dict = {}
        self.talia_gracz()
        self.potasuj()

    def talia_gracz(self):
        del self.talia[:54]

    def potasuj(self):
        shuffle(self.talia)

    def wyloz_karty(self):
        self.reka= [9, 13, 36, 37, 52, 44,5]
    #    self.reka = self.talia[:5]
    #    del self.talia[:5]

    def zdjecie_wyswietl(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.reka)).all()
        qur2 = sorted(qur2, key=lambda o: self.reka.index(o.ID))
        zdjecie = ([i.Zdjecie for i in qur2])
        return zdjecie

    def zobacz_karty(self):

        qur2 = session.query(hero).filter(hero.c.ID.in_(self.odrzucone)).all()
        qur2 = sorted(qur2, key=lambda o: self.odrzucone.index(o.ID))
        zdjecie = ([i.Zdjecie for i in qur2])
        return zdjecie

    def dobierz_karte(self):
        self.reka = self.talia[1]

    def odrzuc_karte(self):
        self.odrzucone.extend(self.talia[1])
        del self.talia[1]

    def koniec_tury(self):
        self.odrzucone.extend(self.reka[:])
        del self.reka[:]

    def koniec_talii(self):
        self.talia.extend(self.odrzucone[:])
        del self.odrzucone[:]
        shuffle(self.talia)

    def kup(self, sprzedane):
        if sprzedane != None:
            qur3 = session.query(hero).filter(hero.c.ID.in_(sprzedane)).all()
            # qur3 = sorted(qur3, key=lambda o: sprzedane.index(o.ID))
            cena = sum([i.Cena for i in qur3])
            if self.monety >= cena:
                self.monety = self.monety - cena
                for x in sprzedane:
                    self.odrzucone.append(x)
                for x in sprzedane:
                    self.kupione.append(x)
                return self.kupione
            else:
                return self.kupione

    def sumuj_monety(self):
        qry = session.query(hero).filter(hero.c.ID.in_(self.reka)).all()
        monety = sum([i.Monety for i in qry])
        nazwy = ([i.Nazwa for i in qry])
        self.monety = monety
        return self.monety

    def sumuj_atak(self):
        qry = session.query(hero).filter(hero.c.ID.in_(self.reka)).all()
        atak = sum([i.Atak for i in qry])
        self.atak = atak
        return self.atak
    def sumuj_zdrowie(self):
        qry = session.query(hero).filter(hero.c.ID.in_(self.reka)).all()
        zdrowie = sum([i.Zdrowie for i in qry])
        self.zycie = self.zycie + zdrowie


    def id(self, slownik):
        i = list(slownik.keys())
        return i

    def atakuj(self, atak):
        self.zycie = self.zycie - atak
        return self.zycie

    def slownik(self, i, atak, d={}):
        d[i] = atak
        return (d)

    def suma(self, slownik):
        slownik_1 = slownik
        print('SLOWNIK', slownik_1)
        atak = list(slownik_1.values())
        print('atak', atak)
        suma = 0
        for x in atak:
            suma +=x
        print('suma',suma)
        return suma

    def odejmij_atak(self,slownik):
        self.atak = self.atak - self.suma(slownik)
        #print(suma)


    def kolor(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.reka)).all()#where(hero.c.Kolor == 'Zielony')
        qur2 = sorted(qur2, key=lambda o: self.reka.index(o.ID))
        id = ([i.ID for i in qur2])
        zielony = 0
        czerwony=0
        niebieski=0
        zloty=0

        #print(kolor)
        d={}
        for x in id:
            qur = session.query(hero).filter(hero.c.ID.in_(id)).where(hero.c.ID == x)
            kolor =([i.Kolor for i in qur])
            d[x]=kolor

        #print('slownik',d)
        for x in d:
            if 'Zielony' in d[x]:
                zielony+=1
            if 'Niebieski' in d[x]:
                niebieski+=1
            if 'Czerwony' in d[x]:
                czerwony+=1
            if 'Zloty' in d[x]:
                zloty+=1
        lista = []
        for x in id:
            if zielony > 1 and 'Zielony' in d[x]:
                lista.append(x)
            if niebieski > 1 and 'Niebieski' in d[x]:
                lista.append(x)
            if czerwony > 1 and 'Czerwony' in d[x]:
                lista.append(x)
            if zloty > 1 and 'Zloty' in d[x]:
                lista.append(x)
                #return d[x]
        #print(zielony, niebieski, czerwony, zloty)
        self.lista =lista
        return(lista)

    def hero_laczenie(self):
        print(self.lista)
        qry = session.query(hero_laczenie).filter(hero_laczenie.c.ID.in_(self.lista)).all()
        qry = sorted(qry, key=lambda o: self.lista.index(o.ID))
        print(qry)
        atak_laczenie = sum([i.Atak for i in qry])
        print("ataak", atak_laczenie)
        monety_laczenie = sum([i.Monety for i in qry])
        print("monety", monety_laczenie)
        zdrowie_laczenie = sum([i.Zdrowie for i in qry])

        self.atak = self.atak + atak_laczenie
        self.monety = self.monety + monety_laczenie
        self.zycie = self.zycie + zdrowie_laczenie




partia = None
ID_GRACZA = 0
powodzenie = None
wylozono = None


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('start.html')

@app.route('/plansza', methods=['GET', 'POST'])
def plansza():
    global partia, ID_GRACZA, powodzenie, wylozono

    if partia is None:
        return redirect("/")
    if request.method == 'POST':
        aktualny = partia.gracze[ID_GRACZA]
        if request.form['action'] == "Wyloz karty":
            aktualny.wyloz_karty()
            aktualny.sumuj_monety()
            aktualny.sumuj_atak()
            aktualny.sumuj_zdrowie()
            aktualny.kolor()
            aktualny.hero_laczenie()
            wylozono = 1
        if request.form['action'] == "Zakoncz ture":
            aktualny.koniec_tury()
            if len(aktualny.talia) == 0:
                aktualny.koniec_talii()
            partia.wystaw()
            aktualny.monety = 0
            aktualny.atak = 0
            ID_GRACZA += 1
            ID_GRACZA %= len(partia.gracze)
            wylozono = 0
            powodzenie = None
        if request.form['action'] == "KUP":
            sprzedane = partia.karta(request.form.getlist('karta', type=int))
            kupione = aktualny.kup(sprzedane)
            partia.aktualizuj_sklep(kupione)
        if request.form['action'] == "Zadaj atak":
           # gracz=request.form.getlist('gracz', type=int)
            #atak = request.form.get('atak', type=int)
            #id= request.form.get('gracz', type=int)
            d = {}

            for i in range(len(partia.gracze)):
                #id = request.form.get('gracz', type=int)
                if i == ID_GRACZA:
                    continue
                atak = request.form.get(f'atak{i+1}', type=int)
                slownik =partia.gracze[i].slownik(i, atak, d)
            print('slownik', slownik)
            x = list(slownik.keys())
            print('gracze',x)

            if aktualny.suma(slownik) <= aktualny.atak:
                print(aktualny.suma(slownik) )
                for i in x:
                    atak = request.form.get(f'atak{i + 1}', type=int)
                    print("dla gracza, atak", i, atak)
                    partia.gracze[i].atakuj(atak)
                    if partia.gracze[i].zycie <= 0:
                        partia.przegrane(i)
                        del x[i]
                        #ID_GRACZA %= len(partia.gracze)
                    if len(partia.gracze) == 1:
                        return redirect("/win")
                ID_GRACZA %= len(partia.gracze)
                aktualny.odejmij_atak(slownik)
                powodzenie = 1
            else:
                powodzenie = 0

    return render_template('plansza.html', partia=partia, aktywny_gracz=ID_GRACZA, wylozono=wylozono, powodzenie=powodzenie)


@app.route('/create', methods=['GET', 'POST'])
def create():
    global partia
    if request.method == 'POST':
        partia = Partia(
            [request.form['gracz1'], request.form['gracz2'], request.form['gracz3'], request.form['gracz4']])
        ID_GRACZA = 0
        return redirect("/plansza")

    return render_template("create.html")


@app.route('/cards', methods=['GET', 'POST'])
def cards():
    global partia, ID_GRACZA
    if partia is None:
        return redirect("/plansza")

    return render_template("cards.html", partia=partia, aktywny_gracz=ID_GRACZA)

@app.route('/win', methods=['GET', 'POST'])
def win():
    global partia, ID_GRACZA
    if partia is None:
        return redirect("/start")

    return render_template("win.html", partia=partia, aktywny_gracz=ID_GRACZA)



if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5122', debug=True)
