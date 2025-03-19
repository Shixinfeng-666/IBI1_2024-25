a = 15 # the walk tim to the bus station
b = 75 # bus journey time for the bus method
c = a + b # total commute time for the bus method
d = 90 # the driving time time in  minutes
e = 5 # the walking time to the car
f = d + e # the total time for diving
print('Total time for the walking + bus:', c, 'minutes')
print('Total time for driving + walking:', f ,'minutes')
if c<f:
    print('Walking to the bus stop and taking the bus is quicker.')
elif c>f:
    print('Driving to the car park and then walking is quicker')
else:
    print('Both commuting methods take the same time')
    # taking the bus is quicker, so it is supposed to print 'Walking to the bus ... is quicker'

X = True
Y = False
W = X and Y
print('X:', X)
print('Y:', Y)
print('W (X and Y):', W)
#truth table
#  X     | Y     | W
#  True  | True  | True
#  True  | False | False
#  False | False | False
#  False | True  | False