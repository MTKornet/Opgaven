Cijfers={'Johan':5.3,'Maarten':9.3,'Lisanne':8.1,'Andrea':6.5,'Peter':9.9,'Wendy':3.2,'Rob':7.8,'Frank':2.9}
Waarden=Cijfers.items()
for studenten in Waarden:
    if studenten[1]>9.0:
        print(studenten)