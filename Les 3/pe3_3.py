leeftijd=eval(input('Wat is uw leeftijd'))
paspoort=input('Heeft u een paspoort (ja/nee)')

if leeftijd>=18 and paspoort=='ja':
    print('U mag stemmen!')
else:
    print('U mag niet stemmen')