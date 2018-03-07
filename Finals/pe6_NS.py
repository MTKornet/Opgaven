def toon_aantal_kluizen_vrij(tekst):
    'Bereken aantal vrije kluizen'
    Kluizen=open(tekst,'r')
    Regels=Kluizen.readlines()
    Kluizen.close()
    return 12-len(Regels)

def nieuwe_kluis(tekst):
    'Nieuwe kluis aanvragen'
    Lijst=['1','2','3','4','5','6','7','8','9','10','11','12']
    Kluizen=open(tekst,'r')
    Regels=Kluizen.readlines()
    Kluizen.close()

    'Bepaal aantal vrije kluizen'
    for nummer in Regels:
        Split = nummer.split(';')
        for kluis in Split:
            if kluis in Lijst:
                Lijst.remove(kluis)

    'Kluis toewijzen'
    if Lijst == []:
        print('Momenteel zijn alle kluizen in gebruik!')
    else:
        NKluis=input('Voer een wachtwoord in voor deze kluis')
        if len(NKluis)>3:
            print('Kluis {} is aan uw toegewezen'.format(Lijst[0]))
        else:
            print('Ongeldig wachtwoord')

    'Kluis registreren'
    NBestand = open('kluizen', 'a')
    if Lijst[0]>1:
        NBestand.write('\n{}; {}'.format(Lijst[0],NKluis))
        NBestand.close
    else:
        NBestand.write('{}; {}'.format(Lijst[0], NKluis))
        NBestand.close

def kluis_openen(tekst):
    'Kluis openen via wachtwoord'
    Lijst=[]
    Kluizen=open(tekst,'r')
    Regels=Kluizen.readlines()
    Kluizen.close()

    'Controleer gegevens'
    Nr=input('Wat is uw kluisnummer?')
    Wachtwoord=input('Wat is uw wachtwoord?')
    for combinatie in Regels:
        if '{}; {}'.format(Nr, Wachtwoord) in combinatie:
            Lijst.append(combinatie)
            print('Uw kluis is open!')
    if Lijst==[]:
        print('Uw kluisnummer of wachtwoord is onjuist!')

def kluis_teruggeven(tekst):
    'Kluis verwijderen via wachtwoord'
    Lijst=[]
    Kluizen = open(tekst, 'r')
    Regels = Kluizen.readlines()
    Kluizen.close()

    'Controleer gegevens'
    Nr = input('Wat is uw kluisnummer?')
    Wachtwoord = input('Wat is uw wachtwoord?')
    for combinatie in Regels:
        Lijst.append(combinatie)
    for kluis in Lijst:
        if '{}; {}'.format(Nr, Wachtwoord) in kluis:
            Lijst.remove(kluis)
            print('Uw kluis is vrijgegeven!')

    'Bestand bijwerken'
    NBestand = open('kluizen', 'w')
    for Kluis in Lijst:
            NBestand.write(Kluis)
    NBestand.close()

    if Lijst == []:
        print('Uw kluisnummer of wachtwoord is onjuist!')

'Scherm uitvoering'
def Start(Menu):
    'Uitvoering keuzemenu'
    if Menu == 1:
        print(toon_aantal_kluizen_vrij('kluizen'))
    elif Menu == 2:
        print(nieuwe_kluis('kluizen'))
    elif Menu == 3:
        print(kluis_openen('kluizen'))
    elif Menu == 4:
        print(kluis_teruggeven('kluizen'))
    elif Menu == 5:
        return False

Menu=int(input("1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: Ik wil stoppen\n"))

while Start(Menu) != False:
    Menu = int(input("1: Ik wil weten hoeveel kluizen nog vrij zijn\n2: Ik wil een nieuwe kluis\n3: Ik wil even iets uit mijn kluis halen\n4: Ik geef mijn kluis terug\n5: Ik wil stoppen\n"))