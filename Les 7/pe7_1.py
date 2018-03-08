Lijst=[]
Getal =eval(input('Geef een getal'))

while not Lijst.append(Getal):
    Getal =eval(input('Geef een getal'))
    if Getal==0:
        break

print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(Lijst),sum(Lijst)))