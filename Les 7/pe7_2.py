def wachtwoord(string):
    if len(string)<4 or len(string)>4:
        print('{} heeft {} letters'.format(string,len(string)))

Woord=input('Geef een string van vier letters:')
while not wachtwoord(Woord):
    Woord = input('Geef een string van vier letters:')
    if len(Woord) ==4:
        print('Inlezen van correcte string: {} is geslaagd'.format(Woord))
    break