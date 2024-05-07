n1=float(input('Reta 1: '))
n2=float(input('Reta 2: '))
n3=float(input('Reta 3: '))

r1=n1+n2
r2=n1+n3
r3=n2+n3

if r1 >=n3 and r2 >n2 and r3>n1:
    print('\033[32mE possivel fazer um triangulo!!')

else:
    print('\033[31mNao\033[m e possivel formar um triangulo ')
