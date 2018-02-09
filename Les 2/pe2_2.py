cijferICOR=eval(input('Cijfer voor ICOR'))
cijferPROG=eval(input('Cijfer voor PROG'))
cijferCSN=eval(input('Cijfer voor CSN'))
totaal=(cijferICOR+cijferPROG+cijferCSN)
gemiddelde =str(totaal/3)
beloning=str(totaal*30)
overzicht='Mijn cijfers (gemiddeld een '+gemiddelde+') leveren een beloning van € '+beloning+' op!'
print(overzicht)