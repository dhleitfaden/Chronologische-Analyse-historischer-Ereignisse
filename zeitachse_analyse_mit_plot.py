import csv
from collections import defaultdict
import matplotlib.pyplot as plt

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
    return jahrhunderte

def zeichne_balkendiagramm(jahrhunderte):
    jahrhunderte = dict(sorted(jahrhunderte.items()))
    labels = [f"{jh}. Jh." for jh in jahrhunderte.keys()]
    werte = list(jahrhunderte.values())

    plt.figure(figsize=(10, 6))
    plt.bar(labels, werte, color='skyblue')
    plt.title("Anzahl historischer Ereignisse pro Jahrhundert")
    plt.xlabel("Jahrhundert")
    plt.ylabel("Anzahl der Ereignisse")
    plt.tight_layout()
    plt.show()

# Beispielverwendung
ereignisse = lade_ereignisse('historische_ereignisse.csv')
ereignisse = sortiere_ereignisse(ereignisse)
zeige_zeitachse(ereignisse)
print("\nVerteilung nach Jahrhundert:")
jahrhunderte = zaehle_nach_jahrhundert(ereignisse)
zeichne_balkendiagramm(jahrhunderte)
