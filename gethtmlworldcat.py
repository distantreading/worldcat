"""
Script zum Download der html-Seiten von worldcat
Die Metadaten-Tabelle wird dabei als Input gegeben
Output sind die entsprechenden html-Seiten zu jedem Werk in der Metadaten-Tabelle

Beispiel-Suchstring, nach erweiterter Suche, Titel, Autor, nur gedruckte Bücher angewählt;
Suche nach Microfiche und E-Book abgewählt;
Sprache Französisch ausgewählt

https://www.worldcat.org/search?q=ti%3ABelle+rivi%C3%A8re+au%3AAimard&dblist=638&fq=+%28x0%3Abook-+OR+%28x0%3Abook+x4%3Aprintbook%29+-%28%28x0%3Abook+x4%3Adigital%29%29+-%28%28x0%3Abook+x4%3Amic%29%29%29+%3E+x0%3Abook+%3E+ln%3Afre&qt=facet_ln%3A

Dieser Suchstring wird als plain_suchstring übergeben; Autor und Titel wurden mit {} für die .format-Methode ersetzt

"""

import requests
from os.path import join
import pandas as pd


#wdir = ""
#csv_file = join(wdir, "metadata.csv")
#write_file = join(wdir, "html")

plain_suchstring = "https://www.worldcat.org/search?q=ti%3A{}+au%3A{}&dblist=638&fq=+%28x0%3Abook-+OR+%28x0%3Abook+x4%3Aprintbook%29+-%28%28x0%3Abook+x4%3Adigital%29%29+-%28%28x0%3Abook+x4%3Amic%29%29%29+%3E+x0%3Abook+%3E+ln%3Afre&qt=facet_ln%3A"


def read_csv(csv_file):
    """
    Metadaten-Tabelle wird eingelesen
    """
    with open(csv_file, encoding = "utf8") as infile:
        data = pd.read_csv(infile, sep = ",")
        #print(data.head())
    return data
   
def get_author(data):
    """
    Autoren-Name wird aus Metadaten-Tabelle entnommen
    """
    author = data["au-name"]
    author = author.split(",")[0]
    #print(author)
    return author

def get_title(data):
    """
    Titel wird der Metadaten-Tabelle entnommen
    """
    title = data["title"]
    title = title.split(" :")[0]
    #print(title)
    return title
    
def generate_suchstring(plain_suchstring, title, author):
    """
    Die Url wird über .format mit Titel und Autor modifiziert
    """
    suchstring = plain_suchstring.format(title, author)
    #print(suchstring)
    return suchstring

def get_html(suchstring):
    """
    Mit requests wird die html heruntergeladen
    """
    html = requests.get(suchstring)
    html = html.text
    #print(html)
    return html
    
def save_html(data, write_file, html, author, title):
    """
    Die html-Seiten werden abgespeichert; im Folgenden werden die Dateien mit Autor_Titel_html.html gespeichert
    """
    #with open(join(write_file, "{}_{}_html.html".format(author, title)), "w", encoding="utf8") as outfile:
    #    outfile.write(html)
    
    """
    Besser zur Weiterverarbeitung: filename oder xml-id aus Metadatentabelle:
    """
    
    filename = data["filename"]
    xmlid = data["xmlid"]
    with open(join(write_file, "{}_html.html".format(filename)), "w", encoding="utf8") as outfile:
        outfile.write(html)

def main(plain_suchstring, csv_file):

    data = read_csv(csv_file)
    for index, data in data.iterrows():
        author = get_author(data)
        title = get_title(data)
        suchstring = generate_suchstring(plain_suchstring, title, author)
        html = get_html(suchstring)
        save_html(data, write_file, html, author, title)
    
main(plain_suchstring, csv_file)
