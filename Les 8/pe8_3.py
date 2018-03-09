def code(invoerstring):
    for i in invoerstring:
        num=ord(i)+3
        ASCII=chr(num)
        print(ASCII, end='')


Naam=input('Wat is uw naam?')
Begin=input('Wat is uw beginstation?')
Eind=input('Wat is uw eindstation?')
Invoer=(Naam+Begin+Eind)
code(Invoer)