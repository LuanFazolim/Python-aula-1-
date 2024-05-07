n=str(input('Seu nome completo: ')).strip()
l=len(n)
l1=l+1

lo=n.upper()
r=lo[0:l1] == 'SILVA'



print(' {} \033[33mSilva\033[m no começo'.format(r))