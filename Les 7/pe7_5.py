def namen():
    Lijst=[]
    Aantal = {}
    Naam=input('Volgende naam:')
    while Naam != '':
        Lijst.append(Naam)
        Naam = input('Volgende naam:')

    for naam in Lijst:
        if naam in Aantal:
            Aantal[naam]+=1
        else:
            Aantal[naam]=1

    for item in Aantal:
        if Aantal.get(item)==1:
            print('Er is {} student met de naam {}'.format(Aantal.get(item),item))
        else:
            print('Er zijn {} studenten met de naam {}'.format(Aantal.get(item),item))

print(namen())