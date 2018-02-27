def tafels(getallen):
        for nummers in getallen:
            for index in range(1,11):
                antw=nummers*index
                print(nummers,'x',index,'=',antw)
tafel=[1,2,3,4,5,6,7,8,9,10]
print(tafels(tafel))