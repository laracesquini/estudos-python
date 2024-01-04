#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

n = float(input('Informe a temperatura em graus Celsius: '))
f = ((9*n)/5) + 32  #De acordo com a ordem de precedência, podemos tiras os parenteses e a conta também estaria certa. Ex: 9*n/5 + 32
print('Essa temperatura corresponde a {:.2f} graus Fahrenheit.'.format(f))