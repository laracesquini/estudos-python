#operadores aritméticos
n1 = int(input('Um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1*n2
d = n1/n2
di = n1//n2
e = n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}'.format(s, m, d), end =' ') #o end='' impede a quebra de linha no final do print
print('Divisão inteira é {} e a potência é {}'.format(di, e))