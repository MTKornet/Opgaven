import datetime
vandaag = datetime.datetime.today()
s=vandaag.strftime("%a %d %b %Y")

def Tekst(input,tijd):
    NBestand=open('hardlopers.txt','a')
    NBestand.write(tijd+', '+input+'\n')
    NBestand.close()
    return True

Input=input('Noteer tijd en naam(\"mm:ss:nn, Naam")')
while Tekst(Input,s):
    Input=input('Noteer tijd en naam(\"mm:ss:nn, Naam")')

