#Calculadora Simples
# n1 = int(input('escreva um numero? '))
# n2 = int(input('escreva ums segundo numero? '))
# c = input('escreva o tipo de calculo: +, -, *, /, **, //, raiz-quadrada: ')
# a = n1 + n2
# m = n1 - n2
# sub = n1 * n2
# d = n1 / n2
# p = n1 ** n2
# di = n1 // n2
# r = n1 ** (1/2)
#
# if c == '+':
#    print('A adiçao dos numeros {0} + {1} = {2} '.format(n1, n2, a))
# elif c == '-':
#
#    print('A subtraçao dos numeros {0} - {1} = {2} '.format(n1, n2, sub))
#
# if c == '*':
#    print('A multiplicaçao dos numeros {0} * {1} = {2} '.format(n1, n2, m))
# elif c == '/':
#
#    print('A divisao dos numeros {0} / {1} = {2:.3} '.format(n1, n2, d))
#
# if c == '**':
#    print('A potencia dos numeros {0} ** {1} = {2} '.format(n1, n2, p))
#
# elif c == '//':
#    print('A multiplicaçao-inteira dos numeros {0} // {1} = {2} '.format(n1, n2, di))
#
# if c == 'raiz-quadrada':
#    print('a raiz quadrada dos numeros {0} ** 1/2 = {1}'.format(n1, r))
#
# n1 = int(input('escreva um numero? '))
# n2 = int(input('escreva ums segundo numero? '))
# c = input('escreva o tipo de calculo: +, -, *, /, **, //, raiz-quadrada: ')

#-----------------------------------------------------------------------------------------------------------------------

#Antecesor e Sucessor

# n = int(input('Escreva um numero e descubra seu antecesor e sucessor: '))
#
# print('O numero digitado {0}, seu atecesor {1}, seu sucessor {2}'.format(n, n-1, n+1))

#-----------------------------------------------------------------------------------------------------------------------

#Dobro, triplo e raiz

# n = int(input('Escreva um valor: '))
# d = n ** 2
# t = n ** 3
# r = n ** 0.5
#
# print('O valor digitado: {}\n O dobro: {}\n O triplo: {}\n A raiz: {:.3}'.format(n,d,t,r))

#-----------------------------------------------------------------------------------------------------------------------

#Media do Jorge

# p = 7.0
# m = 6.9
# me = p+m
# me = me/2
# print('As notas do Jorge em portugues: {} matematica: {} e a sua media e de {}'.format(p, m, me))

#Segundo teste de codigo
# p = float(input('Primeira nota do aluno: '))
# s = float(input('Segunda nota do aluno: '))
# t = float(input('Terceira nota do aluno: '))
# me = (p+s+t)/3
# print('A nota do primeiro trimestre foi: {}, do segundo: {}, do terceiro: {}, e sua media e de: {:.2f}'.format(p,s,t,me))
#-----------------------------------------------------------------------------------------------------------------------

#Conversor de mediadas
#
# m = float(input('Coloque sua medida em metros: '))
# km = m / 1000
# hm = m / 100
# dam = m / 10
# dm = m * 10
# cm = m * 100
# mm = m * 1000
# print('A medida em {0}m\n{1}km\n{2}hm\n{3}dam\n{4}dm\n{5:.0f}cm\n{6:.0f}mm'.format(m,km,hm,dam,dm,cm,mm))
#-----------------------------------------------------------------------------------------------------------------------

#tabuada

# n = int(input('Digite um numero e descubra sua tabuada: '))
# print('-'* 15 + '\n{} x 1 = {} \n{} x 2 = {}\n{} x 3 = {}\n{} x 4 = {}\n'
#       '{} x 5 = {}\n{} x 6 = {}\n{} x 7 = {}\n{} x 8 = {}\n{} x 9 = {}\n{} x 10 = {}\n--------------'.format(n,(n*1), n,(n*2), n,(n*3), n,(n*4), n,(n*5),
# n,(n*6), n,(n*7), n,(n*8), n,(n*9), n,(n*10)))
#
#
# #print('{} x {} = {}'.format(n, 1092, 10*1092))


#-----------------------------------------------------------------------------------------------------------------------

#Consersor de moedas
#
# real = float(input('Quanto dinheiro voce tem na carteira, em reais: '))
# dolar = real / 5.62
# euro = real / 6.36
#
# print('O dinheiro real que voce tem: {:.2f}, voce consegue comprar UR${:.2f} e em EUR${:.2f}'.format(real, dolar, euro))

#-----------------------------------------------------------------------------------------------------------------------

#Calculadora de tinta
#
# a = float(input('Quantos metros de altura tem a parede: '))
# l = float(input('Quantos metros de largura tem sua parede: '))
#
# area = a * l
# t = area / 2
#
# print('a area da sua parede é {}m²com isso conseguimos usar {}L de tinta'.format(area, t))

#-----------------------------------------------------------------------------------------------------------------------

#Calculadora de desconto
#
# prod = float(input('quanto custa esse produto: R$ '))
# desc = prod - (prod*5/100)
# print('O produto de valor R$ {:.2f}, recebeu um desconto de 5% e agora vale R$ {:.2f}'.format(prod, desc))

#-----------------------------------------------------------------------------------------------------------------------

#calculador de aumento
#
# sl = float(input('Qual e o salario do funcionario: R$'))
# aum = sl + (sl*15/100)
# print('O funcionario que ganhava R${:.2f} com um aumento de 15% ganhara R${:.2f}'.format(sl, aum))

#-----------------------------------------------------------------------------------------------------------------------

#Conversor de Temperatura C -> F -> K
#
# C = float(input('Qual a temperatura em Celsius: '))
# F = (C * 9/5) + 32
# K = C + 273.15
# print('O valor em graus Celsius {}°, o valor em Fahrenheit {}F e o valor em Kelvin {}K'.format(C, F, K))

#-----------------------------------------------------------------------------------------------------------------------
#
# #Alugeu de carro
#
# Km = float(input('Quantos Km percorridos: '))
# D = int(input('Quantos dias alugados: '))
#
# diasP = D * 60
# kmrP = Km * 0.15
# preço = diasP + kmrP
#
# print('O preço pago de aluguel e de R${:.2f}'.format(preço))

#-----------------------------------------------------------------------------------------------------------------------






