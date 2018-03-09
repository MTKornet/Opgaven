def wachtwoord(string):
    if len(string)!=4:
        return False
    else:
        return True

while True:
    Woord = input('Geef een string van vier letters:')
    if wachtwoord(Woord):
        print('Inlezen van correcte string: {} is geslaagd'.format(Woord))
        break
    else:
        print('{} heeft {} letters'.format(Woord,len(Woord)))