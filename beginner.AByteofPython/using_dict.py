ab = {'Swaroop': 'swaroop@swaroopch.com',
      'Larry': 'larry@wall.org',
      'Matsumoto': 'matz@ruby-lang.org',
      'Spammer': 'spammer@hotmail.com'
      }

print('Address of swaroop: ', ab['Swaroop'])

del ab['Spammer']
print('\n In address book {0} contacts\n'.format(len(ab)))

for name, address in ab.items():
      print('Contact {0} has address {1}'.format(name,address))

ab['Guido']= 'guido@python.org'

if 'Guido' in ab:
      print('\nAddress of Guido:',ab['Guido'])

print(ab)