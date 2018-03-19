import xmltodict
def openXML(bestand):
    with open(bestand) as myXMLFile:
        Inhoud=myXMLFile.read()
        Dict=xmltodict.parse(Inhoud)
        return Dict

print(openXML("artikelen.xml"))