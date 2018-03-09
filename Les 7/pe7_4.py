def ticker(filename):
    dict={}
    File=open(filename,'r')
    Inhoud=File.readlines()
    File.close()

    for Combo in Inhoud:
        combo=Combo.strip().split(':')
        Item={combo[0]:combo[1]}
        dict.update(Item)
    return dict

Lijst=ticker('ticker symbols')
Company=input('Enter Company name: ')
print('Ticker symbol: {}'.format(Lijst[Company]))
Ticker=input('Enter Ticker symbol: ')
for sleutel in Lijst:
    if Lijst[sleutel]==Ticker:
        print('Company name: {}'.format(sleutel))

