import xmltodict
def openXML(bestand):
    with open(bestand) as myXMLFile:
        Inhoud=myXMLFile.read()
        Dict=xmltodict.parse(Inhoud)
        return Dict

Dict=openXML("stations.xml")
Stations=Dict['Stations']['Station']

print('Dit zijn de codes en types van de {} stations:'.format(len(Stations)))
for station in Stations:
    print('{} - {}'.format(station['Code'],station['Type']))

print('\nDit zijn alle stations me één of meer synoniemen:')
for station in Stations:
    if station['Synoniemen']['Synoniem'] != None:
        print('{} - {}'.format(station['Code'],station['Synoniemen']['Synoniem']))

print('\nDit is de lange naam van elk station:')
for station in Stations:
    print('{} - {}'.format(station['Code'],station['Namen']['Lang']))


