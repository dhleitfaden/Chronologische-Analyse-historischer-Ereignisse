Kontext:
Ein digitales Archiv stellt eine CSV-Datei mit einer Liste historischer Ereignisse bereit, die Jahr, Titel und Ort jedes Ereignisses enthält. Deine Aufgabe ist es, diese Daten zu lesen, chronologisch zu ordnen und in einer einfachen Zeitachse darzustellen.

Ziel:
Schreibe ein Python-Skript, das:

1. Eine CSV-Datei mit historischen Ereignissen liest.


2. Die Ereignisse nach Jahr sortiert.


3. Eine einfache textbasierte Zeitachse anzeigt.


4. [Optional] Die Ereignisse nach Jahrhundert gruppiert und zählt.



Struktur der CSV-Datei (historische_ereignisse.csv):

jahr,titel,ort
1492,Entdeckung Amerikas,Amerika
1789,Französische Revolution,Frankreich
1861,Italienische Einigung,Italien
1914,Beginn des Ersten Weltkriegs,Europa


---

Aufgabenstellung:

1. Erstelle eine Funktion lade_ereignisse(pfad) zum Einlesen der CSV-Datei.


2. Erstelle eine Funktion sortiere_ereignisse(ereignisse), die nach Jahr sortiert.


3. Erstelle eine Funktion zeige_zeitachse(ereignisse), die eine einfache textuelle Zeitachse ausgibt:

1492: Entdeckung Amerikas (Amerika)
1789: Französische Revolution (Frankreich)


4. [Optional] Erstelle eine Funktion zaehle_nach_jahrhundert(ereignisse), die die Ereignisse nach Jahrhundert zählt und das Ergebnis ausgibt.




---

Lösung in Python (auf Deutsch):

import csv
from collections import defaultdict

def lade_ereignisse(pfad):
    ereignisse = []
    with open(pfad, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for zeile in reader:
            ereignis = {
                'jahr': int(zeile['jahr']),
                'titel': zeile['titel'],
                'ort': zeile['ort']
            }
            ereignisse.append(ereignis)
    return ereignisse

def sortiere_ereignisse(ereignisse):
    return sorted(ereignisse, key=lambda e: e['jahr'])

def zeige_zeitachse(ereignisse):
    for e in ereignisse:
        print(f"{e['jahr']}: {e['titel']} ({e['ort']})")

def zaehle_nach_jahrhundert(ereignisse):
    jahrhunderte = defaultdict(int)
    for e in ereignisse:
        jahrhundert = (e['jahr'] - 1) // 100 + 1
        jahrhunderte[jahrhundert] += 1
    for jh in sorted(jahrhunderte):
        print(f"{jh}. Jahrhundert: {jahrhunderte[jh]} Ereignisse")

# Beispielverwendung
ereignisse = lade_ereignisse('historische_ereignisse.csv')
ereignisse = sortiere_ereignisse(ereignisse)
zeige_zeitachse(ereignisse)
print("\nVerteilung nach Jahrhundert:")
zaehle_nach_jahrhundert(ereignisse)


---

Datei: historische_ereignisse.csv

jahr,titel,ort
1492,Entdeckung Amerikas,Amerika
1789,Französische Revolution,Frankreich
1861,Italienische Einigung,Italien
1914,Beginn des Ersten Weltkriegs,Europa
1945,Ende des Zweiten Weltkriegs,Weltweit
1989,Fall der Berliner Mauer,Deutschland

 
