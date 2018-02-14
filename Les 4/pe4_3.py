lengte=eval(input('Wat is uw lengte in cm'))
if lengte >= 120:
    def lang_genoeg():
        return 'Je bent lang genoeg voor de attractie!'
else:
    def lang_genoeg():
        return 'Sorry, je bent te klein!'
print(lang_genoeg())