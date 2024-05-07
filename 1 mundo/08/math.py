#Import toda matematia
import math
n=float(input(''))
r = math.sqrt(n)
print(r)

print('')
#Import so um (raiz)
from math import sqrt
r=sqrt(n)
print('importa so um {}= {}'.format(n,r))

print('')

#import dois ou mais
from math import sqrt,floor
r2=sqrt(n)
print('com dois {}= {}'.format(n,floor(r2)))