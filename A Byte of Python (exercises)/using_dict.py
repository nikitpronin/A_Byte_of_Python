#adressbook

ab = { 'Swaroop'    : 'swaroop@swaroopch.com',
       'Larry'      : 'larry@wall.org'
    }
print ("Swaroop's adress:",ab['Swaroop'])

#delete pair
del ab['Larry']

for name,adress in ab.items():
    print('Contact {0} with adress {1}'.format(name,adress))

#Add pair
ab['Guido'] = 'guido@python.org'

if 'Guido' in ab:
    print ("\nAdress Guido:",ab['Guido'])
