# dictionay is a changeble, unordred colection of unique key:value pairs
#   fast because they use hashing, allow us to access quickly
capitals = {'USA': 'washington DC',
            'INDIA': 'NEW Delhi',
            'China': 'Beijing',
            'Russia': 'Moscow'}
capitals.update({'Germany': 'Berlin'})
capitals.update({'USA': 'Las Vegas'})
capitals.pop('China')
# capitals.clear()
# print(capitals['Russia'])
# # print(capitals['Germany'])
# print(capitals.get('Germany'))
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())

for key, value in capitals.items():
    print(key, value)
