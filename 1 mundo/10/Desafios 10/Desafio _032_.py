from datetime import date

a=int(input('ano: '))

if a == 0:
    a=(date.today().year)

if a %4==0 and a%100 !=0 or a%400==0:
    print('O ano de {} E \033[34mBissexto\033[m'.format(a))
else:
    print('O ano de {} \033[31mNao Bissexto'.format(a))
