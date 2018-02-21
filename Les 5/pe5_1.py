def convert(Celsius):
    Fahrenheit=(Celsius*1.8)+32
    return Fahrenheit
def table():
    print('   F  ', '   C  ')
    formattable = '{:6.1f},{:6.1f}'
    for temperatuur in range(-30,41,10):
        Fahrenheit=convert(temperatuur)
        print(formattable.format(Fahrenheit,temperatuur))

print(table())
