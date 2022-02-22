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
import time

app = Flask(__name__)

partia = None
ID_GRACZA = 0
powodzenie = None
wylozono = None


@app.route('/start', methods=['GET', 'POST'])
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
            if len(aktualny.talia) < 5:
                aktualny.koniec_talii()
            aktualny.wyloz_karty()
            aktualny.dobierz_karte()
            aktualny.kolor()
            aktualny.wszystkie_karty()
            aktualny.kolor_talia()
            aktualny.hero_laczenie_dobranie()
            aktualny.sumuj_monety()
            aktualny.sumuj_atak()
            aktualny.sumuj_zdrowie()
            aktualny.hero_laczenie()
            wylozono = 1

        if request.form['action'] == "KUP":
            sprzedane = partia.karta(request.form.getlist('karta', type=int))
            kupione = aktualny.kup(sprzedane)
            partia.aktualizuj_sklep(kupione)

        if request.form['action'] == "Zadaj atak":
            d = {}
            for i in range(len(partia.gracze)):
                if i == ID_GRACZA:
                    continue
                atak = request.form.get(f'atak{i+1}', type=int)
                slownik =partia.gracze[i].slownik(i, atak, d)
            print("irew", slownik)
            x = list(slownik.keys())
            if aktualny.suma(slownik) <= aktualny.atak:
                print("JJJJ", aktualny.suma(slownik))
                for i in x:
                    atak = request.form.get(f'atak{i + 1}', type=int)
                    print("dla gracza, atak", i, atak)
                    partia.gracze[i].atakuj(atak)
                #ID_GRACZA %= len(partia.gracze)
                aktualny.odejmij_atak(slownik)
                for gracz in partia.gracze:
                    index = partia.gracze.index(gracz)
                    print(index)
                    [partia.przegrane(gracz) for gracz in partia.gracze if gracz.zycie <= 0]
                    ID_GRACZA = partia.gracze.index(aktualny)
                    if len(partia.gracze) == 1:
                        return redirect("/win")
                powodzenie = 1
            else:
                powodzenie = 0
        if request.form['action'] == "Zakoncz ture":
            aktualny.koniec_tury()
            if len(aktualny.talia) < 5:
                aktualny.koniec_talii()
            partia.wystaw()
            aktualny.monety = 0
            aktualny.atak = 0
            ID_GRACZA += 1
            ID_GRACZA %= len(partia.gracze)
            wylozono = 0
            powodzenie = None
            if partia.gracze[ID_GRACZA].nazwa == 'komputer':
                time.sleep(3)
                aktualny = partia.gracze[ID_GRACZA]
                partia.gracze[ID_GRACZA].komputer()
                # kupowanie
                kolorek = partia.gracze[ID_GRACZA].kolor_talia()
                odrzucone = partia.gracze[ID_GRACZA].wszystkie
                sprzedane = partia.kolor_sklep(kolorek, odrzucone)
                if partia.karty_komp() <= partia.gracze[ID_GRACZA].monety:
                    kupione = partia.gracze[ID_GRACZA].kup(sprzedane)
                else:
                    sprzedane = partia.inne()
                    kupione = partia.gracze[ID_GRACZA].kup(sprzedane)
                partia.aktualizuj_sklep(kupione)
                # atakowanie
                d = {}
                lista_zyc = []
                if partia.gracze[ID_GRACZA].atak % (len(partia.gracze) - 1) == 0:
                    for i in range(len(partia.gracze)):
                        if i == ID_GRACZA:
                            continue
                        atak = partia.gracze[ID_GRACZA].atak // (len(partia.gracze) - 1)
                        slownik = partia.gracze[i].slownik(i, atak, d)
                else:
                    atak = partia.gracze[ID_GRACZA].atak
                    slownik = partia.gracze[ID_GRACZA].slownik(ID_GRACZA, atak, d)
                x = list(slownik.keys())
                if partia.gracze[ID_GRACZA].suma(slownik) <= partia.gracze[ID_GRACZA].atak:
                    if partia.gracze[ID_GRACZA].atak % (len(partia.gracze) - 1) == 0:
                        atak = partia.gracze[ID_GRACZA].atak // (len(partia.gracze) - 1)
                        for i in x:
                            if i == ID_GRACZA:
                                continue
                            if partia.gracze[ID_GRACZA].atak % (len(partia.gracze) - 1) == 0:
                                atak = partia.gracze[ID_GRACZA].atak // (len(partia.gracze) - 1)
                            partia.gracze[i].atakuj(atak)
                    else:
                        atak = partia.gracze[ID_GRACZA].atak
                        for i in range(len(partia.gracze)):
                            if i == ID_GRACZA:
                                continue
                            lista_zyc.append(partia.gracze[i].zycie)
                        min_value = min(lista_zyc)
                        min_index = lista_zyc.index(min_value)
                        partia.gracze[min_index].atakuj(atak)
                    partia.gracze[ID_GRACZA].odejmij_atak(slownik)

                    [partia.przegrane(gracz) for gracz in partia.gracze if gracz.zycie <= 0]
                    ID_GRACZA = partia.gracze.index(aktualny)
                    if len(partia.gracze) == 1:
                        return redirect("/win")
                    powodzenie = 1
                else:
                    powodzenie = 0
                partia.gracze[ID_GRACZA].monety = 0
                partia.gracze[ID_GRACZA].atak = 0
                partia.gracze[ID_GRACZA].koniec_tury()
                partia.wystaw()

                ID_GRACZA += 1
                ID_GRACZA %= len(partia.gracze)

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

@app.route('/create_komputer', methods=['GET', 'POST'])
def create_komputer():
    global partia
    if request.method == 'POST':
        partia = Partia(
            [request.form['gracz1'], request.form['gracz2'], request.form['gracz3'],'komputer'])
        ID_GRACZA = 0
        return redirect("/plansza")

    return render_template("create_komputer.html")

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
