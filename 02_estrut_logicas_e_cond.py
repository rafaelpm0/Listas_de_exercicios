# Aqui serão resolvidos os exercicios da seção 05.

"""
Resolução Exercicios 01:
Faça um programa que receba dois números e mostre qual deles é o maior

exercicio_01 = int(input(f'Digite dois numeros inteiros e será retornador o maior. \nPrimeiro numero: '))
numero_02 = int(input(f'Segundo numero:'))
if exercicio_01 > numero_02:
    print('Primeiro numero maior')
else:
    print('Segundo numero maior.')


Resolução Exercicio 02:
Leia um numero. Se esse número for positivo, calcule a raiz quadrada do número. Se for negativo, retorne invalido.


import math
exercicio_02 = int(input('Digite um numero inteiro para que seja calculada a raiz quadrada: '))
if exercicio_02 > 0:
    print(f'A raiz quadrada do numero é: {math.sqrt(exercicio_02)} e {exercicio_02 **0.5}')

else:
    print('Raiz quadrada só pode ser positiva')


Resolução Exercicio 03:
Leia um numero real. Se esse numero for positivo, imprima a raiz quadrada. Do contrário imprima o seu quadrado


import math
exercicio_03 = int(input('Digite um numero inteiro, se positivo tira raiz, se negativo eleva ao quadrado: '))
if exercicio_03 > 0:
    print(f'A raiz quadrada do numero é: {math.sqrt(exercicio_03)} e {exercicio_03 **0.5}')

else:
    print(f'O quadrado deste numero é: {exercicio_03**2}')


Resolução Exercicio 04:
Leia um numero e caso este seja postivo, retorne sua raiz quadrada e seu quadrado.

import math
exercicio_04 = int(input('Digite um numero inteiro, se positivo tira raiz e eleva ao quadrado: '))
if exercicio_04 > 0:
    print(f'A raiz quadrada do numero é: {math.sqrt(exercicio_04)} e {exercicio_04 **0.5}')
    print(f'O quadrado deste numero é: {exercicio_04**2}')
else:
    print("'Algo', fiquei com dó de deixar o else em branco")


Resolução Exercicio 05:
Faça um programa que receba um numero inteiro e verifique se este númro é par ou impar


exercicio_05 = int(input('Digite um numero e será verificaro se é par ou impar: '))
if exercicio_05 % 2 == 0:
    print('É par.')
else:
    print('É impar.')


Resolução Exercicio 06:
Escreva um programa que, dados dois números inteiros, mostre na tela  o maior deles assim como a diferença entre eles

exercicio_06 = input(f'Digite 2 numeros usando o espaço como separador e sera retornado o maior e sua diferença: ')
a = int(exercicio_06.split(" ")[0])
b = int(exercicio_06.split(" ")[1])

if a > b:
    print(f'O maior numero é: {a} e a diferença entre eles é {a-b}')
else:
    print(f'O maior numero é: {b} e a diferença entre eles é {b-a}')


Resolução Exercicio 07:
Faça um programa que receba dois números e mostre o maior. Se por acaso, os dois forem iguais, retorne Números iguais


numero1 = int(input('Digite dois numeros inteiros, e irá verificar se são iguais. \nNumero 1: '))
numero2 = int(input('Numero dois: '))
if numero1 > numero2:
    print('Numero 1 é maior')
elif numero1 < numero2:
    print('Numero 2 é maior')
else:
    print('Os numeros são iguais')


Resolução Exercicio 08:
Faça um programa que leia 2 notas de um aluno, verifique se as notas estão entre 0.0 e 10.0 e caso estejam fora do
escopo, imprima esta informação e encerre o programa.

exercicio_08 = input('Digite as duas notas do aluno e será dada a media entre elas, use espaço como delimitador entre as duas notas: ')
a = float(exercicio_08.split(' ')[0])
b = float(exercicio_08.split(' ')[1])


if (a>=0 and a<= 10.00) and (b>=0 and b<= 10.00) :
    print(f'A media deste aluno foi: {(a+b)/2}')
else:
    print('Nota invalida')


Resolução Exercicio 09:
Leia o salário de um trabalhador e o valor da prestação de um empresário. Se a prestação for maior do que 20% do salário
imprima: emprestimo não concedido, caso contrário imprimá: emprestimos concedido

exercicio_09 = input('Digite o salario e o valor do emprestimo solicitado, use espaço como delimitador entre as duas notas: ')

a = float(exercicio_09.split(' ')[0])
b = float(exercicio_09.split(' ')[1])

if b > (a*0.20):
    print('Emprestimo não concedido')
else:
    print('Emprestimo concedido')


Resolução Exercicio 10:
Faça um programa que receba a altura e o sexo de uma pessoa e calcule e mostre seu peso ideal. Formulas
Homens: 72.7*h - 58  /  Mulheres: 62,1 * h - 44,7

exercicio_10 = input('Digite seu sexo [M] ou [F], sua altura e peso, use espaço como delimitador entre as duas nota: ')

s = exercicio_10.split(' ')[0].lower()
h = float(exercicio_10.split(' ')[1])
p = float(exercicio_10.split(' ')[2])

if s == 'm':
    print(f'Seu peso ideial é: {(72.7*h)-58}')
else:
    print(f'Seu peso ideial é: {(62.1*h)-44,7}')


Resolução Exercico 11:
Escreva um programa que leia um número int maior que 0 e devolva a soma de sus algarismos. Se for menor que zero,
retorne númerp inválido.

exercicio_11 = input('Digite um numero inteiro e será apresentada a soma destes algarismos: ')
if int(exercicio_11) > 0:
    soma = 0
    for i in exercicio_11:
        soma += int(i)
    print(f'Soma: {int(soma)}')
else:
    print('Numero invalido.')


Resolução Exercicio 12:
Calulo o lagaritimo de um número positivo, se for negativa devolva número invalido.

import math
exercicio_12 = int(input('Digite um numero para que seja calculado seu logaritino: '))

if exercicio_12 > 0:
    print(f'O logaritimo é {math.log(exercicio_12)}')
else:
    print('Numero menor que zero.')


Resolução Exercicio 13:
Faça um programa que calcule a média ponderada de três provas, tendo pesos 1, 1 e 3 respectivamente. As provras
deverão ter base 100.


exercicio_13 = input('Digete as três notas do aluno, notas com base 100. '
                     'Use espaço como delimitador entre as duas notas: ')

a = float(exercicio_13.split(' ')[0])
b = float(exercicio_13.split(' ')[1])
c = float(exercicio_13.split(' ')[2])

nota = ((a + b + (c*2))/4)

if nota >= 60:
    print(f'Aprovado com a média: {nota}.')
else:
    print('Reprovado.')


# Exercicio 14 é igual ao 13


Resolução Exercicio 15:

exercicio_15 = int(input('Digite um numero de 0 a 7 e será retornado o dia da semana: '))

if exercicio_15 == 1:
    print('Segunda')
elif exercicio_15 == 2:
    print('Terça')
elif exercicio_15 == 3:
    print('Quarta')
elif exercicio_15 == 4:
    print('Quinta')
elif exercicio_15 == 5:
    print('Sexta')
elif exercicio_15 == 6:
    print('Sabado')
elif exercicio_15 == 7:
    print('Doming')
else:
    print('Temos apenas 7 dias na semana kkk')


# Exercicio 16 igual ao 15

# Exercicio 17 apenas calculo de area.


Resolução Exercicio 18:
Faça um programa que mostre ao usuário um menu com 4 opções de operações matemáticas. Após escolher uma das opções,
pede dois valores e mostra o resultado.

menu = int(input('Escolha a operação matematica ser feita a partir do menu. [1] Soma, [2] Subtração, [3] Multiplicação '
                 '[4] Divisão. Menu: '))

print('Digite os dois numeros que irão realizar esta operação.')
numero1 = float(input(" Numero 01: "))
numero2 = float(input(" Numero 02: "))

if menu == 1:
    print(f'Resultado da operação foi: {numero1+numero2}')
elif menu == 2:
    print(f'Resultado da operação foi: {numero1-numero2}')
elif menu == 3:
    print(f'Resultado da operação foi: {numero1*numero2}')
elif menu == 4:
    print(f'Resultado da operação foi: {numero1/numero2}')
else:
    print('Menu inexistente')


Resolução Exercicio 19:
Faça um programa para verificar se um número inteiro é diviível por 3 ou 5, mas não os dois simulnaneamente.


exercicio_19 = int(input('Digite um numero inteiro e será verificado se este é divivel por 2 ou 5, mas não '
                         'simultaniamente: '))
if (exercicio_19 % 2 == 0) and (exercicio_19 % 5 == 0):
    print('Numero é divisiel por 2 e 5.')
else:
    print('Numero é divisel por 2 ou 5.')


Resolução Exercicio 20:

20. Dados três valores, A, B, C, verifique se eles podem ser valores dos lados de um triângulo
e, se forem, se é um triângulo escaleno, equilátero ou isóscele, considerando os seguintes
conceitos:
- O comprimento de cada lado de um triângulo é menor do que a soma dos outros dois lados.
- Chama-se equilátero o triângulo que tem três lados iguais.
- Denominam-se isósceles o triângulo que tem o comprimento de dois lados iguais.
- Recebe o nome de escaleno o triângulo que tem os três lados diferentes.


print('Informe os valores de um triando de lados a,b e c, e será classificado em Equilatero, Isoceles ou Escaleno.')
a = int(input('Lado a: '))
b = int(input('Lado b: '))
c = int(input('Lado c: '))

if (a < b + c) and (b < a + b) and (c < a + b):

    if a == b == c:
        print('Triangulo é equilatero.')
    elif a == b or b == c or a == c:
        print('Triangurlo é isóceles.')
    else:
        print('Triangulo é escaleno')
else:
    print('Não é um triangulo.')


# Exercicio 21 não vou fazer pois é a mesma coisa da calculadora e eu já havia implementado o erro.

# Resolução exercicio 22:
Leia a idade e o tempo de serviço de um trabalhador e escreva se ele pode ou não se aposentar.
As condições para aposentadoria são:
- Ter pelo menos 65 anos;
- Ou ter trabalhado pelo menos 30 anos;
- Ou ter pelo menos 60 anos e trabalhado pelo menos 25 nos.


servico = float(input(" Tempo de serviço: "))
idade = float(input(" Idade: "))

if idade >= 65 or (servico >= 30 or (idade >= 60 and servico >= 25)):
    print('Pode se aposentar')
else:
    print('Tente se aposentar ano que vem.')


# exercicio 23:
Determine se o ano é bisexto. Tdo ano bisexto é divisível por 4

ano = int(input('Digite um ano[aaaa] e será retornado se o ano é bissexto: '))
if ano % 4 == 0:
    print('Ano bissexto')
else:
    print('Não é bissexto')


Resolução Exercicio 24:
Uma empresa vende o mesmo produtos para quatro diferentes estados. Sendo o imposto para MG 7%, SP 12%, RJ 15%, MS 12%.
Faça um programa que o usuário entre com valor do produto e o estado destino. O programa deverá retornar o valor do
produto acrecido do imposto. Se o estado não for valido, mostrar mensagem de erro


print('Digite o estado destino e o valor do produto e será apresentado o valor do protudo acrescido do valor do imposto:')
us = input('Digite o estado: ')
valor = int(input('Digite o valor: '))


if us == 'MG' or 'mg':
    print(f'O valor do produto acrescido dos impostos é: {valor*1.07}')
elif us == 'SP' or 'sp':
    print(f'O valor do produto acrescido dos impostos é: {valor*1.12}')
elif us == 'RJ' or 'rj':
    print(f'O valor do produto acrescido dos impostos é: {valor*1.15}')
elif us == 'MS' or 'ms':
    print(f'O valor do produto acrescido dos impostos é: {valor*1.08}')
else:
    print('Estado invalido')


Resolução Exercicio 25:
Faça o calculo de baskara seguindo suas regras de validação e retone suas raizes


print('Informa os valores de x², b e c para que seja realizado o calculo da baskara:')
a = int(input("Digite o valor de x²: "))
b = int(input("Digite o valor de b: "))
c = int(input('Digite o valor de c: '))


delta = b**2 -(4*a*c)
raiz1 = (-b + delta ** 0.5)/(2*a)
raiz2 = (-b - (delta ** 0.5))/(2*a)

print(f"Valor de delta é igual: {delta}")

if a != 0:
    if delta < 0:
        print('Não existe raiz.')
    elif delta == 0:
        print(f'Raiz é de {raiz1}.')
    elif delta > 0:
        print(f'As raizes são {raiz1} e {raiz2}.')
else:
    print('O valor de "a" não pode ser igual a zero')


# Exercicio 26 e 27 vou pular por ser muita basico, é apenas um if aninhado.

# Resolução Exercicio 28:
Faça um programa que leia três números inteiros positivos e efetue o cáculo de uma das seguintes médias de acordo
com um valor numerico digitado pelo usuário. Médias: Geométrica, Ponderada, Harmônica, Aritmética

menu = int(input('Escolha a operação matematica ser feita a partir do menu. [1] Geometria, [2] Ponderada, [3] Harmonica '
                 '[4] Geometrica. Menu: '))

print('Digite os três numeros que irão realizar esta operação')
numero1 = float(input(" Numero 01: "))
numero2 = float(input(" Numero 02: "))
numero3 = float(input(" Numero 03: "))

if menu == 1:
    print(f'Resultado da operação foi: {(numero1*numero2*numero3) ** 1/3}')
elif menu == 2:
    print(f'Resultado da operação foi: {(numero1+(2 * numero2)+(3 * numero3)) / 3}')
elif menu == 3:
    print(f'Resultado da operação foi: {3/((1/numero1)+(1/numero2)+(1/numero3))}')
elif menu == 4:
    print(f'Resultado da operação foi: {(numero1 + numero2 + numero3)/3}')


Exercico 30 vou pular é apenas ordenação de numeros, da de usar sort nume lista
Exercicio 31 é apenas if aninhado também


#Exercicio 32:
Escreva um programa que leia o código do produto escolhido do cardápio de uma lanchonete e a quantidade.
 O programa deve calcular o valor a ser pago por aquele lanche. Considere que a cada execução somente será calculado um
 pedido, o cardápio da lanchonete segue o padrão abaixo (não vou escrever pois já vais estar na lista abaixo)

repeteco = 's'
total = 0

itens = {100: 'cachorro_quente', 101: 'bauru_simples', 102: 'bauru_com_ovo', 103: 'hamburguer',
         104: 'cheeseburguer', 105: 'suco', 106: 'refrigerante'}

valor = {100: 1.20, 101: 1.30, 102: 1.50, 103: 1.20, 104: 1.70, 105: 2.20, 106: 1.10}

print('Cardapio: ')
for i in itens:
    print(f'Item {i}: {itens[i]}, valor: {valor[i]}')

print('\nInforme quais os itens do pedidos e a quantidade e, será informado o valor total')

while repeteco == 's':
    pedido = int(input('\n Digite o numero do item: ')), int(input(' Quantidade: '))
    total =+ (valor[pedido[0]] * pedido[1])
    repeteco = input('Deseja pedir mais itens: [S]/[N]: ').lower()

print(f"O valor total da compra foi de: {total}")

Exercicios 33 e 34 é apenas if aninhado


Resolução Exercicio 35:
Leia uma data e determine se ela é valida. Ou seja, verifique se o mês estra entre 1 e 12, e se o dia existe daquele
mês. Note que Fevereiro tem 29 dias em anos bissextos, e 28 em dias em anos não bissextos

 data = input('Digite uma data no formato dd:mm:aaaa e será verificado se esta data é existe. Data: ')
d = int(data.split(':')[0])
m = int(data.split(':')[1])
a = int(data.split(':')[2])

mes_de_31 = ((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m== 12) and (0 < d < 32))
dia_30 = (0 < d > 31)
ano_bi_29 = ((a % 4==0) and (0 < d < 30) and (m==2))
fev_28 = ((a % 4 != 0) and (0 < d < 29))

if mes_de_31 or dia_30 or ano_bi_29 or fev_28:
    print("Data valida.")
    if a % 4 == 0:
        print('E ano bisexto')
else:
    print('Data invalida')



# Resolução Exercicio 36:


# Percebi que a faixa de valores é dividida em 5 faixas de 20 mil em 20 mil. Assim criei uma regra logica para
calcular essa faixa pela logica. Para calcular a comissão fixa, percebi que fora a faixa 0, segue a regra de 500 +
(50*(logica-1)). Assim consigo determinar a faixa e comissão fixa. A comissão variavel usei um if aninhado para setar
o calculo sendo venda*comissão variavel.

valor_v = int(input('Digite o valor da venda para que seja calculado o valor da comissão: '))

logica = int((valor_v/20_000))
fixo = 500 + (logica - 1) * 50

if logica < 1:
    print(f'A comissão foi de R$ {round(valor_v * 0.14 + 400, 2)}')
elif 1 <= logica < 5:
    print(f'A comissão foi de R$ {round(valor_v * 0.14 + fixo, 2)}')
else:
    print(f'A comissão foi de R$ {round(valor_v * 0.16 + fixo, 2)}')



Exercicio 37:

As tarifas de certo parque de estacionamento são as seguintes:
1º e 2º hora - R$ 1,00 cada
3º e 4º hora - R$ 1,40 cada
5º hora e seguintes - R$ 2,00 cada

O número de horas a pagar é sempre inteiro e arredondado por excesso. Deste modo, quem estacionar durante 61 minutos
pagará por duas horas, que é o mesmo que pagaria se tivesse permanecido 120 minutos. Os momentos de chegada ao parque e
partida deste são apresentados na forma de pares de inteiros, representando horas e minutos. Por exemplo, o par 12 50
representará "dez para a uma da tarde". Pretende-se criar um programa que, lidos pelo teclado os momentos de chegada e
de partida, escreva na tela o preço cobrado pelo estacionamento. Admite-se que a chegada e a partida se dão com
intervalo não superior a 24 horas. Portanto, se uma dada hora de chegada for superior à da partida, isso não é uma
situação de erro, antes significará que a partida ocorreu no dia seguinte ao da chegada.

OBS: Incrementei o exercico, caso seja colocado o parametro SIM no dia, ele irá calcular a diferença de um dia para
o outro

entrada = input('Digite o horário de entrada do estacionamento, formato hh mm: ')
saida = input('Digite o horário de saida do estacionamento,  formato hh mm: : ')
dia = input('A saida ocorreu no mesmo dia SIM [S] OU NÃO [N]: ')

entradanum = entrada.split(' ')
saidanum = saida.split(' ')

if dia == ('s' or 'S' or 'SIM' or 'Sim' or 'sim'):
    tempo_dia = ((int(saidanum[0])*60 + int(saidanum[1])) - (int(entradanum[0])*60 + int(entradanum[1])))/60
else:
    tempo_dia = ((int(saidanum[0])*60 + int(saidanum[1])) + (int(entradanum[0])*60 + int(entradanum[1])))/60

print(tempo_dia)

if tempo_dia % 1 != 0:
    tempo_dia += 1


if 0 < tempo_dia < 3:
    print(f'O valor do estacionamento é: {int(tempo_dia)}')
elif 2 < tempo_dia < 5:
    print(f'O valor do estacionamento é: {int(tempo_dia) * 1.40}')
else:
    print(f'O valor do estacionamento é: {int(tempo_dia) * 2}')


Os demais é repetição de exerciicos
"""














