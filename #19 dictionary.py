# dictionary = A changeable, unordered of unique key: value paires
#             Fast because they use hashing, allow us to acces a value quickly


capitales = {'USA': 'washinton pc',
             'india': 'new delhi',
             'Russia': ',mossco',
             'China': 'Beijing'}

capitales.update({'Germany': 'Berlin'})
capitales.update({'USA': 'LA'})
capitales.pop('China')
#capitales.clear()
print(capitales['USA'])
print(capitales.get('Germany'))
print(capitales.keys())
print(capitales.items())
print(capitales.values())

for key,value in capitales.items():
    print(key,value)

