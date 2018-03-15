import datetime
import csv

bestand ='inloggers.csv'

def invullen(file):
    with open(file,'w',newline='') as myCSVFile:
        writer = csv.writer(myCSVFile, delimiter=';')
        writer.writerow(('Datum','Naam','Voorl','GbDatum','E-mail'))

        while True:
            vandaag = datetime.datetime.today()
            s = vandaag.strftime("%a %d %b %Y")

            naam=input('Wat is je achternaam?')
            if naam=='einde':
                break
            else:
                voorl=input('Wat zijn je voorletters?')
                gbdatum=input('Wat is je geboortedatum?')
                email=input('Wat is je e-mail adres?')

            writer.writerow((s,voorl,naam,gbdatum,email))

invullen(bestand)
