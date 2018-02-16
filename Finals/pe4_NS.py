def standaardprijs(afstandKM):
    'Berekent standaardprijs uit afstand in Km'
    if afstandKM >50:
        prijs1=(afstandKM-50)*0.60+15
    else:
        prijs1=afstandKM*0.80
    return prijs1

def ritprijs(leeftijd, weekendrit, afstandKM):
    'Berekent kortingsprijs met de leeftijd, dag van de week en afstand in Km'
    maxprijs=standaardprijs(afstandKM)
    if leeftijd <12 or leeftijd >=65:
        if 'z' in weekendrit:
            prijs2=maxprijs*0.65
        else:
            prijs2=maxprijs*0.70
    else:
        if 'z' in weekendrit:
            prijs2=maxprijs*0.60
        else:
            prijs2=maxprijs
    return prijs2

AfstandKM = eval(input('Lengte treinrijs in KM?'))
if AfstandKM < 0:
    AfstandKM = 0
Dag=input('Welke dag is het?')
Leeftijd=eval(input('Wat is uw leeftijd'))

print(standaardprijs(AfstandKM))
print(ritprijs(Leeftijd,Dag,AfstandKM))