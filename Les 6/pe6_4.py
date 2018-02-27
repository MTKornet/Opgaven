studentencijfers=[[95,92,86],[66,75,54],[89,72,100],[34,0,0]]

def gemiddelde_per_student(cijfers):
    antw=[]
    for Rij in cijfers:
        antw.append(sum(Rij)/len(Rij))
    return antw

def gemiddelde_van_alle_studenten(cijfers):
    Totaal=0
    for Rij in cijfers:
        for getallen in Rij:
            Totaal=Totaal+getallen
        antw=Totaal/(len(Rij)*len(cijfers))
    return antw

print(gemiddelde_per_student(studentencijfers))
print(gemiddelde_van_alle_studenten(studentencijfers))