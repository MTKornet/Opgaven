def Selectie(lijst):
    List=[]
    for woord in lijst:
        if len(woord)==4:
            List.append(woord)
    return List

Lijst=eval(input('Geef lijst van minimaal 10 strings!'))
print(Selectie(Lijst))