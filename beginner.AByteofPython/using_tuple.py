zoo = 'python', 'elephant', 'penguin'
print('Number of animals in zoo: ', len(zoo))
new_zoo = 'monkey', 'camel', zoo
print('Number cells in zoo', len(new_zoo))
print('All animals in new zoo: ', new_zoo)
print('Animals from old zoo: ', new_zoo[2])
print('Last animal from old zoo: ',new_zoo[2][2])
print('Number animals in new zoo: ', len(new_zoo)-1+len(new_zoo[2]))
