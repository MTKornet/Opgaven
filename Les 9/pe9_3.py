import csv
def inlezen(file):
    maximum = 0
    with open(file,'r') as myCSVFile:
        reader=csv.reader(myCSVFile,delimiter=';')
        for rij in reader:
            waarden=int(rij[2])
            if waarden>maximum:
                maximum=waarden
                output='De hoogste score is: {} op {} behaald door {}'.format(rij[2],rij[1],rij[0])
        return output
print(inlezen('gamerscore.csv'))