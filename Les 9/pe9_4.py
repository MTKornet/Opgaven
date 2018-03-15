import csv

def inlezen(file):
    maximum = 0
    minimum = 1000000000000000
    aantal = 0
    with open(file,'r') as myCSVFile:
        reader=csv.DictReader(myCSVFile,delimiter=';')

        for Rij in reader:
            Prijs=eval(Rij['Prijs'])
            Voorraad=int(Rij['Voorraad'])
            aantal=aantal+Voorraad
            if Prijs>maximum:
                maximum=Prijs
                max='Het duurste artikel is {} en die kost {} Euro'.format(Rij['Naam'],Rij['Prijs'])
            elif Voorraad<minimum:
                minimum=Voorraad
                min='Er zijn slechts {} exemplaren in voorraad van het product met nummer {}'.format(Rij['Voorraad'],Rij['Artikelnummer'])

        print(max)
        print(min)
        print('In totaal hebben wij {} producten in ons magazijn liggen'.format(aantal))

inlezen('producten.csv')