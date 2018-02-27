def seizoen(maand):
    if maand in [12,1,2]:
        print('Winter')
    elif maand in [3,4,5]:
        print('Lente')
    elif maand in [6,7,8]:
        print('Zomer')
    elif maand in [9,10,11]:
        print('Herfst')

NrMaand=eval(input('Welke maandnummer is het vandaag?'))
print(seizoen(NrMaand))