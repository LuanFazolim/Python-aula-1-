s=float(input('Salario: '))

if s >=1200:
    print((10 / 100 * s)+s,'\033[32mR$\033[m')

else:
    print((15 / 100 * s)+s,'\033[32mR$\033[m')