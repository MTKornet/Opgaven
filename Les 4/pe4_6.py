letterlijst=['a','b','c']
print(letterlijst)
def wijzig(letter):
    letter.clear()
    letter.extend(['d','e','f'])
    return letter
print(wijzig(letterlijst))
