from random import randint
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
reka_select = reka.select()
a = engine.execute(reka_select)
result2 = a.fetchall()

#result dla wszystkich kart
hero_select = hero.select()
c=engine.execute(hero_select)
result= c.fetchall()


class Gracz:
    def __init__(self, imie='Nieznane'):
        self.nazwa = imie
        self.talia = [i[0] for i in result]
        self.reka = []
        self.odrzucone = []
        self.wszystkie = []
        self.kupione=[]
        self.zielone = []
        self.lista = []
        self.monety = 0
        self.atak = 0
        self.zycie = 10
        self.dict = {}
        self.talia_gracz()
        self.potasuj()
        self.wszystkie_karty()
        self.kolor_talia()


    def talia_gracz(self):
        del self.talia[:54]
        #self.talia.append[30, 31, 44, 45, 46, 47,1,8,5,17,18]

    def potasuj(self):
        shuffle(self.talia)

    def wyloz_karty(self):
       # self.reka= [30, 31, 44, 45, 46, 47,1,8,5,17,18]
        self.reka = self.talia[:5]
        del self.talia[:5]
        #self.dobierz_karte()

    def zdjecie_wyswietl(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.reka)).all()
        qur2 = sorted(qur2, key=lambda o: self.reka.index(o.ID))
        zdjecie = ([i.Zdjecie for i in qur2])
        return zdjecie

    def zobacz_karty(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.wszystkie)).all()
        qur2 = sorted(qur2, key=lambda o: self.wszystkie.index(o.ID))
        zdjecie = ([i.Zdjecie for i in qur2])
        return zdjecie

    def odrzuc_karte(self):
        self.odrzucone.extend(self.talia[1])
        del self.talia[1]

    def koniec_tury(self):
        self.odrzucone.extend(self.reka[:])
        del self.reka[:]

    def koniec_talii(self):
        shuffle(self.odrzucone)
        self.talia.extend(self.odrzucone[:])
        del self.odrzucone[:]
        #shuffle(self.talia)

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
            suma += x
       # print('suma',suma)
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
            qur = session.query(hero).filter(hero.c.ID.in_(id)).filter(hero.c.ID == x)
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

    def cena_kolor(self):
        pass

    def wszystkie_karty(self):
        self.wszystkie.extend(self.reka[:])
        self.wszystkie.extend(self.odrzucone[:])
        self.wszystkie.extend(self.talia[:])
        #print(self.wszystkie)

    def kolor_talia(self):
        #self.wszytkie = self.reka + self.odrzucone + self.talia()
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.wszystkie)).all()#where(hero.c.Kolor == 'Zielony')
        qur2 = sorted(qur2, key=lambda o: self.wszystkie.index(o.ID))
        id = ([i.ID for i in qur2])
        zielony = 0
        czerwony=0
        niebieski=0
        zloty=0
        a = None

        d={}
        for x in id:
            qur = session.query(hero).filter(hero.c.ID.in_(id)).filter(hero.c.ID == x)
            #print(qur)
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

        maxi = max(zielony, zloty, niebieski, czerwony)
        if zielony is maxi:
            a = 1 #zielony
        if zloty is maxi:
            a = 2 #zloty
        if niebieski is maxi:
            a = 3 #'niebieski'
        if czerwony is maxi:
            a = 4 # 'czerwony'

      #  print(zielony, zloty, niebieski, czerwony)
        #print("AA", a)
        return(a)

    def hero_laczenie(self):
        qry = session.query(hero_laczenie).filter(hero_laczenie.c.ID.in_(self.lista)).all()
        qry = sorted(qry, key=lambda o: self.lista.index(o.ID))
        atak_laczenie = sum([i.Atak for i in qry])
        monety_laczenie = sum([i.Monety for i in qry])
        zdrowie_laczenie = sum([i.Zdrowie for i in qry])
        zdolnosci = ([i.Inne_zdolnosci for i in qry])
        self.atak = self.atak + atak_laczenie
        self.monety = self.monety + monety_laczenie
        self.zycie = self.zycie + zdrowie_laczenie

    def dobierz_karte(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.reka)).all()
        qur2 = sorted(qur2, key=lambda o: self.reka.index(o.ID))
        zdolnosci = ([i.Inne_zdolnosci for i in qur2])
        x = 0
        for i in zdolnosci:
            if i == 'Dobierz karte':
                x+=1
            if i == 'Dobierz 2 karty':
                x += 2

        if len(self.talia) >= x+5:
            self.reka.extend(self.talia[:x])
            del self.talia[:x]
        else:
            self.reka.extend(self.odrzucone[:x])
            del self.odrzucone[:x]
        print(zdolnosci, x)

        '''if x != 0:
            if len(self.talia) >= x:
                self.reka.append(self.talia[:1])
                del self.talia[:x]
            else:
                self.reka.append(self.odrzucone[:2])
                del self.talia[:x]
        '''
    def hero_laczenie_dobranie(self):
        qry = session.query(hero_laczenie).filter(hero_laczenie.c.ID.in_(self.lista)).all()
        qry = sorted(qry, key=lambda o: self.lista.index(o.ID))

        zdolnosci = ([i.Inne_zdolnosci for i in qry])
        x = 0
        for i in zdolnosci:
            if i == 'Dobierz karte':
                x += 1
            if i == 'Dobierz 2 karty':
                x += 2
        if len(self.talia)>= x:
            self.reka.extend(self.talia[:x])
            del self.talia[:x]
        else:
            self.reka.extend(self.odrzucone[:x])
            del self.odrzucone[:x]
        print(zdolnosci, x)

    def komputer(self):
        if len(self.talia) < 5:
            self.koniec_talii()
        self.wyloz_karty()
        self.dobierz_karte()
        self.kolor()
        self.wszystkie_karty()
        self.kolor_talia()
        self.hero_laczenie_dobranie()
        self.sumuj_monety()
        self.sumuj_atak()
        self.sumuj_zdrowie()
        self.hero_laczenie()











