import math
co=float(input('\033[31mꞵ\033[m: '))
ca=float(input('\033[32mA\033[m: '))

#1

b=co*co
a=ca*ca
s=b+a
r=math.sqrt(s)
print('\033[34m#1: A Hipotenusa e: {:.2f}²'.format(r))

#ou


#2
hi=math.hypot(co,ca)
print('\033[36m#2: A Hipotenusa e: {:.2f}²'.format(hi))