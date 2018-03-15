def kosten(prijs):
    try:
        Aantal=int(input('Met hoeveel personen zijn jullie?'))
        if Aantal>0:
            kosten=int(prijs)//Aantal
            print('De prijs is {} per persoon'.format(kosten))
        else:
            print('Negatieve getallen zijn niet toegestaan!')
    except ZeroDivisionError:
        print('Delen door nul kan niet!')
    except ValueError:
        print('Gebruik cijfers voor het invoeren van het aantal!')
    except:
        print('Onjuiste invoer!')

Prijs=4356
kosten(Prijs)

