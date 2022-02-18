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

class Partia:
    def __init__(self, imiona=['Ala', 'Bob']):
        self.sklep_talia = [i[0] for i in result]
        self.sklep_wystawione = []
        self.gracze = [Gracz(imie) for imie in imiona if imie]
        self.sprzedane = []
        self.sprzedane_komputer = []
        self.lista = []
        self.talia()
        self.potasuj()
        self.wystaw()
        self.cena()
        #self.kolor_sklep()
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
        Y = self.cena()
        X = self.sklep_wystawione
        Z = [x for _, x in sorted(zip(Y, X), key=lambda pair: pair[0])]
        self.sklep_wystawione = Z

    def karta(self, sprzedane):
        if len(self.sklep_wystawione) != 0:
            self.sprzedane = [self.sklep_wystawione[x] for x in sprzedane]
            return self.sprzedane
        else:
            print("koniec sklepu")
        return

    def kolor_sklep(self, kolorek, odrzucone):
        #self.wszytkie = self.reka + self.odrzucone + self.talia()
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.sklep_wystawione)).all()#where(hero.c.Kolor == 'Zielony')
        qur2 = sorted(qur2, key=lambda o: self.sklep_wystawione.index(o.ID))
        id = ([i.ID for i in qur2])
        a = None
        inna = []
        zielony = 0
        czerwony=0
        niebieski=0
        zloty=0
        #print(kolor)
        d={}
        for x in id:
            qur = session.query(hero).filter(hero.c.ID.in_(id)).filter(hero.c.ID == x)
            #print(qur)
            kolor =([i.Kolor for i in qur])
            d[x]=kolor
        print(kolorek)
        #print('slownik',d)
        if kolorek == 1:
            kolorek = 'zielony'
        if kolorek == 2:
            kolorek = 'zloty'
        if kolorek == 3:
            kolorek = 'niebieski'
        if kolorek == 4:
            kolorek = 'czerwony'
        print("Kolor po", kolorek, odrzucone)
        for x in d:
            if 'Niebieski' in d[x]:
                a = 'niebieski'
            if 'Czerwony' in d[x]:
                a = 'czerwony'
            if 'Zloty' in d[x]:
                a = 'zloty'
            if 'Zielony' in d[x]:
                a='zielony'
            if a == kolorek:
                self.lista.append(x)
            else:
                inna.append(x)
        for x in self.lista:
            if x in odrzucone:
                del self.lista[x]

        if len(self.lista) >= 1:
            self.sprzedane_komputer = self.lista
        else:
            self.sprzedane_komputer = inna
        self.lista = []
        inna = []
        return self.sprzedane_komputer

    def karty_komp(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.sprzedane_komputer)).all()
        qur2 = sorted(qur2, key=lambda o: self.sprzedane_komputer.index(o.ID))
        cena = sum([i.Cena for i in qur2])
        return cena

    def inne(self):
        self.sprzedane_komputer = self.sklep_wystawione[:1]
        return self.sprzedane_komputer

    def karta_komputer(self, sprzedane):
        if len(self.sklep_wystawione) != 0:
            self.sprzedane = [self.sklep_wystawione[x] for x in sprzedane]
            return self.sprzedane

    def aktualizuj_sklep(self, kupione):
        aktualizacja_sklepu = [x for x in self.sklep_wystawione if x not in kupione]
        self.sklep_wystawione = aktualizacja_sklepu

    def cena(self):
        qur2 = session.query(hero).filter(hero.c.ID.in_(self.sklep_wystawione)).all()
        qur2 = sorted(qur2, key=lambda o: self.sklep_wystawione.index(o.ID))
        cena = ([i.Cena for i in qur2])
        return cena


    #  przegrane=[]
    #  przegrane.append(y)
    #  #del self.gracze[i]
    #  print(przegrane)
    #  for x in przegrane:
    #      del self.gracze[x]

    def przegrane(self, gracz):
        self.gracze.remove(gracz)
