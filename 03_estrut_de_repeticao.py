""""
Resolução Exercicio 01:
Faça um programa que mostre os cinco primeiros números multiplos de 3. Considerando os números maiores que zero


lista = []
numero = 1

while len(lista) < 5:
    if numero % 3 == 0:
        lista.append(numero)
    numero += 1

print(lista)


Resolição Exercicio 2:
Escreva um programa que escreva de 1 a 100 na tela, de 1 em 1, 2 vezes. A primeira vez deve ser for e a segunda do while.


for i in range(1, 101):
    print(i, end=', ')

print('')

b = 1
while b <= 100:
    print(b, end=', ')
    b += 1


Resolução Exercicio 03:
Faça um algoritmo utilizando um comando WHILE que mostra uma contagem regressiva na tela, iniciando em 10 e terminando
em 0. Mostrar uma mensagem 'FIM' após a contagem.

i = 10
while i >= 0:
    print(i)
    i -= 1
print('Fim')


Resolução Exercicio 04:
Faça um programa que declare um número inteiro, inicialize-o com 0, e incremente de 1000 em 1000, imprimindo seu valor
na tela, até que seu valor  seja 100_000


for i in range(0, 101_000, 1000):
    print(i)


Resolução Exercicio 05:
Faça um programa que peça ao usuário para digitar 10 valores e some-os


print('Digite 10 numeros e será apresentada a soma')

numero = 0
for i in range(1, 11):
    numero += int(input(f"Digite o {i+1}º numero: "))

print(f'O valor da soma foi de {numero}')


Resolução Exercicio 06:
Faça um programa que peça ao usuário para digitar 10 valores e imprima sua média


print('Digite 10 numeros e será apresentada sua media simples:')

numero = 0
for i in range(1, 11):
    numero += int(input(f"Digite o {i}º numero: "))

print(f'O valor da soma foi de {numero/i}')


Resolução Exercicio 07:
Faça um programa que peça ao usuário para digitar 10 valores, ignorando os inteiros não positivos e imprima sua média

numero = []
print("Digite 10 numeros e será apresentada a média dos positivos. ")

for i in range(1, 11):
    entrada = int(input(f"Digite {i}º numero:"))
    if entrada >= 1:
        numero.append(entrada)

print(f'A media foi de: {(sum(numero)/len(numero))}')

Resolução Exercicio 8:
Escreva um programa que receba 10 números e retorne o menor e maior valor lido

print('Digite 10 numero e será impresso o maior e menor numero.')

lista = []

for i in range(1, 11):
    numero = int(input(f'Digite o {i}º numero:'))
    lista.append(numero)

maxi = max(lista)
mini = min(lista)
print(f'O numero maior numero é: {maxi}, o menor numero é: {mini}')

Outra forma de resolver o exercicio 8:


valor_maior = valor_menor = int(input('Digite o 1º valor: '))
for cont in range(2, 11):
    numero = int(input(f'Digite o {cont}º valor: '))
    if numero >= valor_maior:
        valor_maior = numero
    else:
        valor_menor = numero
print(f'Maior: {valor_maior}\nMenor: {valor_menor}')

Resolução do coleguinha 9:
Faça um programa que receba um número inteiro N e depois imprima os N primeiros números naturis impares

num = int(input('Digite um numero e será retornado seus N impares: '))

for i in range(1, num+1, 2):
    print(i)

Resolução Exercicio 10:
Faça um programa que calcule e mostre a soma dos 50 primeiros números pares

num = 0
for i in range(0, 51, 2):
        num += i
print(num)

usando comprehension lis, resolução após termino do curos

pares = sum(x for x in range(0, 51, 2))
print(pares)


Resolução Exercicio 11:
Faça um programa que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
crescente.


numero = int(input('Digite um numero inteiro N e será impresso até este numero N, um a um. Numero: '))

i = 0
while i <= numero:
    print(i)
    i += 1

# ou

for i in range(0, numero+1)
    print(i)

Resolução Exercicio 12:
Faça um programa que receba um número inteiro positivo N e imprima todos os números naturais de 0 até N em ordem
decrescente.

i = int(input('Digite um numero inteiro N e será impresso até este numero N, um a um. Numero: '))

numero = 0
while i >= numero:
    print(i)
    i -= 1

# ou

for i in range(numero, 0, -1)
    print(i)

Resolução Exercicio 13:
Faça um programa que receba um número inteiro positivo par N e imprima todos os números naturais de 0 até N pares em
ordem crescente.

numero = int(input('Digite um numero inteiro par e será impresso até este numero N, apenas pares. Numero: '))

i = 0
while i <= numero:
    print(i)
    i += 2

# or

for i in range(0, numero, 2)
    print(i)

Exercicio 14:
Faça um programa que receba um número inteiro positivo par N e imprima todos os números naturais de 0 até N pares em
ordem decrescente.

i = int(input('Digite um numero inteiro N e será impresso até este numero N, um a um. Numero: '))

numero = 0
while i >= numero:
    print(i)
    i -= 2

Exercicio 15:
Faça um programa que receba um número inteiro positivo impares N e imprima todos os números naturais de 0 até N impare
em ordem crescente.

numero = int(input('Digite um impar e será impresso de 1 a N impar até o numero impar final: '))

for i in range(1, numero+1):
    if i % 2 != 0:
        print(i)

Exercicio 16:
Faça um programa que receba um número inteiro positivo impares N e imprima todos os números naturais de 0 até N impare
em ordem decrescente.

numero = int(input('Digite um impar e será impresso de 1 a N impar até o numero impar final: '))

for i in range(numero, 0, -1):
    if i % 2 != 0:
        print(i)

Exercicio 17:
Faça um programa que leia um número inteiro positivo n e calcule a soma dos n primeiros números naturais.

soma = 0
numero = int(input("Digite um numero se seá retornado a soma de deus numeros naturais. Numero: "))
for i in range(1, numero+1):
    soma += i
print(f'Soma: {soma}')

# Vi na resolução do coleguinha

numero = int(input('Digite um numero: '))
soma = numero * (numero+1)//2
print(soma)

# usando comprehension list

soma2 = sum(x for x in range(numero+1))


Exercicio 18:
Escreva um programa que leia x números (a quantidade deve se fornecida pelo usuário) e retorn o maior numero e quantas,
vezes ele foi lido


quant = int(input('Digite quantos numeros você deseja excrever. Quantidade: '))

lista = []
for i in range(1, quant+1):
    lista.append(int(input(f'Digite o {i}º numero: ')))

contador = 0
x = max(lista)

print(f'O maior numero é: {x} e foi informado {lista.count(x)} vezes')

# Meu problema era como contar o numero maxixo, ele resolveu usando a função .count que conta o numero indicado na,
lista


#Resolucao que eu fiz:

quant = int(input('Digite quantos numeros você deseja excrever. Quantidade: '))

lista = []
for i in range(1, quant+1):
    lista.append(int(input(f'Digite o {i}º numero: ')))

contador = 0
for i in range(0, quant+1):
    if max(lista) == lista[contador]:
        contador += 1

print(f'O maior numero é: {max(lista)} e foi informado {contador} vezes')


Exercicio 19:
Escreva um algoritimo que leia um número inteiro entre 100 999 e, imprima na saida cada um dos algorismos do número

num = input('Digite um numero de tres digitos entre 100 e 999: ')

while 100 <= num <= 999:
    num = input('Numero invalido. Digite um numero de tres digitos entre 100 e 999: ')

n = 0
for i in num:
    print(num[n:n+1])
    n += 1

# Após o curso. Apenas precisa fazer print(num[::-1])


Exercicio 20:
Ler uma sequencia de números inteiros e determinar se eles são pares ou não. Deverá ser informado o número de dados
lidos e o número de valores pares. O processo termina quando for digitado o valo 1000

lista = []
for i in range(1, 1001):
    if i % 2 == 0:
        lista.append(n)

print(f'O numero de dados lido foi de {n} e foi destes {len(lista)} fora par')


Exercicio 21:
Faça um program que receba dois números. Calculo e mostre, a soma dos numeros pares desse intervalor, incluindo os
digitados. E a multiplicação dos números impares desse intervalor, incluindo os digitados.

soma = 0
multi = 1

print('Digite os dois numero, sera lido a sequencia entre eles. O primeiro deve ser menor e o segundo maior ou igual:')
a = int(input('1º:'))
b = int(input('2: '))

if a < b:
    lista = list(range(a, b + 1))
else:
    lista = list(range(b, a + 1, -1))

for i in lista:
    if i % 2 == 0:
        soma += i
    if i % 2 != 0:
        multi *= i

print(f'A soma dos n pares foi {soma} e a multiplicação dos impares {multi}')


Exercicio 22:
Escreva um programa completo que permita a qualquer aluno introduzir, pelo teclado, uma sequencia arbitrária de notas
(válidas no intervalo de 10 a 20) e que mostre na tela, como resultado, a correspondente média aritmética. O número de
 notas com que o aluno pretenda efetuar o cálculo não será fornecido ao programa, o qual terminará quando for
introduzido um valor que não seja válido como nota de aprovação.

lista = []
entrada = 10

while True:
    entrada = int(input('Digite um numero: '))
    if 10 <= entrada <= 20:
        lista.append(entrada)
    else:
        break

print(f'A media aritimetica foi de {sum(lista)/len(lista)}')


Exercicio 23:
Faça um programa que leia um numero inteiro e imprima seus divisores


numero = int(input('Digite um numero inteiro e será apresentado seus divisores: '))

while numero < 0:
    numero = int(input('Digite um numero inteiro e será apresentado seus divisores, numero positivo: '))

for i in range(1, numero+1):
    n = i
    if numero % n == 0:
        print(f'Divisor: {n}')

# Duas resoluções pois curso

while (numero := int(input('Digite um numero inteiro e será apresentado seus divisores: '))) < 0:
    numero = int(input('Digite um numero inteiro e será apresentado seus divisores, numero positivo: '))
print(numero)
for i in range(1, numero+1):
    if (numero % i) == 0:
        print(f'Divisor: {i}')


divisores = [i for i in range(1, numero+1) if numero % i == 0]
print(divisores)


Exercicio 24:


numero = int(input('Digite um numero inteiro e será apresentado seus divisores: '))
n = 0
soma = 0

while numero < 0:
    numero = int(input('Digite um numero inteiro e será apresentado seus divisores, numero positivo: '))

for i in range(1, numero+1):
    n = i
    if numero % n == 0:
        print(f'Divisor: {n}')
        soma += n
print(f'A soma dos divisores é de {soma}')

Outra forma de resolver o exerccio 24:

numero = int(input('Digite um numero inteiro e será apresentado seus divisores: '))
soma = 0
for i in range(1, numero+1):
    if (numero % i == 0) and (i != numero):
        print(f'Divisor: {i}')
        soma += i

print(f'Soma {soma}')

# Usando comprehension lista para chegar na soma

soma = sum[i for i in range(1, numero) if numero % i == 0]
print(soma)

Exercicio 25:
Faça um programa que some todos os numeros naturais abaixo de 1000 que são multiplas de 3 ou 5

soma = 0
for i in range(1, 1001):
    if (i % 3 == 0) or (i % 5 == 0):
        soma += i
print(soma)

# após curso

soma = sum([i for i in range(1, 1001) if ((i % 3 == 0) or (i % 5 == 0))])
print(soma)

#Exercicio 26 vou pular, repetição do 25.

Exercico 27:
Faça um programa que leia um valor N inteiro e positivo e apresente o valor harmonico de N.

numero = int(input(f'Digite um numero para ser calculada sua serie harmonica: '))

while numero < 0:
    numero = int(input(f'Digite um numero para ser calculada sua serie harmonica, apenas naturais positivos: '))

for i in range(1, numero+1):
    if i == 1:
        harmonico = 1
    else:
        harmonico += 1/i

print(harmonico)


Exercicio 28:
Faça um programa que leia um valor N inteiro e positivo, calcule e mostre o valor E, conforme a fórmula a
seguir: E = 1 + 1/1! + 1/2! + 1/3! + 1/4!...+1/N!"

def fatorail(x):
    if x > 1:
        return x * fatorail(x-1)
    else:
        return 1


harmonico = 1
numero = int(input(f'Digite um numero para ser calculada sua serie harmonica: '))

while numero < 0:
    numero = int(input(f'Digite um numero para ser calculada sua serie harmonica, apenas naturais positivos: '))

for i in range(2, numero+1):
    harmonico += 1/fatorail(i)

print(harmonico)

Exercico 29:
Escreva um programa para calcular o valor de serie de 5 termos.   S={0 + 1/2! + 2/4! + 3/6! + 4/ 8!}


def fatorail(x):
    if x > 1:
        return x * fatorail(x-1)
    else:
        return 1

harmonico = 0
for i in range(1, numero+1):
    harmonico += i/fatorail(i*2)

print(harmonico)


Exercicio 30, repetição


Exercicio 31:
Faça um programa que escreva e calcule o valor de S
S = 1/1 + 3/2 + 5/3 + 7/4... 99/50


lista = list(range(1, 100, 2))
cont = 1
soma = 0


for i in lista:
    soma += i/cont
    cont += 1

print(soma)


Exercico 32:
Faça um program que simule o lançamento de dois dados d1 e d2, n vezes, e tem como saída o número de cada dado e a
relação entre eles (>,<=) de cada lançamento.


import random
n = int(input('Digite a quantidade de vezes que o programa deve simular o lançamento dos dados: '))

for i in range(1, n+1):

    d1 = random.randint(1,6)
    d2 = random.randint(1,6)

    if d1 > d2:
        print(f'd1 = {d1}, d2 = {d2}, logo d1 > d2')
    elif d1 < d2:
        print(f'd1 = {d1}, d2 = {d2}, logo d1 > d2')
    else:
        print(f'd1 = {d1}, d2 = {d2}, logo d1 = d2')


Exercicio 33 é repetição

Exercicio 34:
Faça um programa que calcule o menor número divisível por cada um dos números de 1 a 20.
#Exemplo: 2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10, sem sobrar resto

numero = 0
mmc = 0

while mmc != 10:
    numero += 1
    for i in range(1, 11):
        if numero % i == 0:
            mmc += 1
        else:
            mmc = 0
            break
print(numero)


35 - Junção de dois exercicios anteriores, não vou fazer


Exercicio 36:
Conforme input


n = int(input('Digite um numero e sera retornado a diferença da soma dos quadrados e do quadrado da soma do intervalor'
              '\n tomando o ultimo numero inteiro positivo como limite do intervalo. Numero: '))

soma = 0
quad =0


for i in range(1, n+1):
    soma += i
soma = soma ** 2

for i in range(1, n+1):
    quad += i ** 2

print(f' A soma dos quadradros é {soma} e o quadrado da soma é {quad}. E a diferença entre ele é {soma - quad} ')


 for d in lista:
        if str(c) == str(a)+str(b):
            print(c)

Exercicio 37:
.Escreve um programa que verifique quais números entre 1000 e 9999 (inclusive) pos- suem a propriedade seguinte: a
soma dos dois dígitos de mais baixa ordem com os dois dígitos de mais alta ordem elevada ao quadrado é igual ao próprio
numero. Por exemplo, para o inteiro 3025, temos que: 30 + 25 = 55    55^2 = 3025"


lista = []
c = 0

for i in range(1000, 10_001):
    lista.append(str(i))

for i in range(0, 9_001):
    a = lista[i][0:2]
    b = lista[i][2:5]
    c = (int(a) + int(b)) ** 2
    #  print(a, b, c)
    if str(c) == (str(a)+str(b)):
        print(c)

v2 pós curso:

lista = [str(x) for x in range(1000, 10_000)]

for i in lista:
    a = i[0:2]
    b = i[2:5]
    c = (int(a) + int(b)) ** 2
    if str(c) == (str(a)+str(b)):
        print(c)

Exercicio 38:
Faça um programa que calcule o terno pitagórico {a, b, c}, para o qual a + b + c = 1000. Um terno pitagórico é um
conjunto de três números naturais, a b c, para a qual, a ** 2 + b ** 2 = c **2

a = 1
b = 1

for a in range(1, 1000):
    for b in range(1, 1000):
        c = ((a ** 2) + (b ** 2)) ** 0.5
        if a + b + c == 1000:
            print(a, b, c)
            break



# Exercicio 39 não vou fazer, apenas calcular area de um triangulo e impedir que seja digitado zero. Para isto basta um
while

# Exercicio 40 é repetição, só muda a condição de parada por um numero negativo

# Exercicio 41 idiota, não vou fazer.

Exercicio 42:
Faça um programa que leia um conjunto não determinado de valores, um de cada vez, e escreva para cada um dos valores
lidos, o quadrado, o cubo e a raiz quadrada. Finalize a entrada de dados com um valor negativo ou zero.



n = int(input('Digite um numero positivo e será retonado seu quadrado, cubo e raiz. Numero: '))
while n => 0:
    print(n ** 2, n ** 3, n ** 0.5)
    n = int(input('Digite mais um numero: '))
print('Numero invalido.')



# Exercicio 43 basico, apenas armazenar em uma lista, usar a função sum para somar a lista e len para dividir


Exercicico 44:
eia um número positivo do usuário, então, calcule e imprima a sequência Fibonacci até o primeiro número superior ao
 número lido. Exemplo: se o usuário informou o número 30, a sequência a ser impressa será 0 1 1 2 3 5 8 13 21 34."

def fibo(n, a=1, b=1, c=0):
    print(a, b, end=' ')
    while n > c:
        c = a + b
        a = b
        b = c
        print(c, end=' ')
    return None

fibo(30)


# Calculando fibonacci com recursiva

def fibo(x):

    if x <= 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)


n = int(input('Digite até qual numero será impresso fibonnaci: '))
for i in range(1, n+1):
    print(fibo(i))


Exercicio 45:
Faça um program que converter km/h para m/s e vice e versa. Você deve criar um menu e crie a opção para finalizasr o
programa

repetir = 'sim'

while repetir == 'sim' or 's':

    menu = input('\n\nDe km/h para m/s digite, digite 1 ou m/s,\nPara [m/s] para [km/h] digite, [2] ou [km/h]: ')
    valor = int(input('Digite o valor a ser convertido:'))

    if menu == '1' or 'm/s':
        print(valor / 3.6)
    elif menu == '2' or 'km/h':
        print(valor / 3.6)
    else:
        while repetir == (1 or 'm/s' or 2 or 'km/h'):
            menu = input('Menu inexistente, digite novamente: ')

    repetir = input('Deseja reptir? Digite "sim" ou "s": ').lower()


Exercicio 46:
Faça um programa que gera um numero aleatório entre 1 a 1000. O programa encerra quando o usuário acerta qual o numero
gerardo. Para ajudar o usuário o programa deve informar se o numero é maior ou menor do que a resposta.


import random
n = random.randint(1, 1000)
r = 0

print('O sistema ira gerar um numero aleatório entre 1 e 1000. Tente acertar!!\n')


while r != n:
    r = int(input('Numero: '))
    if r > n:
        print('\nTente um numero menor')
    elif r < n:
        print('\nTente um numero maior')
print('\nParabens você acertou!!.')


47 repetição de exercico de outro bloco


Resolução Exercicio 48:
Faça um programa que soma os termos de valor par da seuqncia Fibonaccci, cujos valores não ultrapassem 4 milhoes.

def fibo(x):

    if x <= 2:
        return 1
    else:
        return fibo(x-1) + fibo(x-2)


n = 0
soma = 0
while fibo(n) < 4_000_000:
    n += 1

for i in range(1, n+1):
    if fibo(i) % 2 == 0:
        soma += fibo(i)
print(soma)

Exercicio 49:
O funcionário chamado Carlos tem um colega chamado João que recebe um salário que equivale a um terço do seu salário.
Carlos gosta de fazer aplicações na caderneta de poupança e vai aplicar seu salário integralmente nela, pois está
rendendo 2% ao mês. João aplicará seu salário integralmente no fundo de renda fixa, que está rendendo 5% ao mês.

Construa um programa que deverá calcular e mostrar a quantidade de meses necessários para que o valor pertencente a
João iguale ou ultrapasse o valor pertencente a Carlos.

t = 1  # Meses

sc = float(input('Defina o salário de Carlos. Salário: '))

src = (0.02 * sc)  # Rendimento
srj = (sc/3) * 0.05

while src > srj:
    src *= t
    srj *= t
    t += 1

print(f'O montante de joao será maior em: {t} meses. {round(src, 2)}  {round(srj, 2)}. ')

Exercicio 50:
Chico tem 1.50 e cresce 2 centimetros por ano, enquanto Zé tem 1.10 metros e cresce 3 centimetros por ano
Escreva um programa que calcule e imprima quantos anos serão necessários para que Zé seja maior que Chico


al_chico = 1.50
al_ze = 1.10
anos = 0

while al_chico > al_ze:
    anos += 1
    al_chico += 0.02
    al_ze += 0.03

print(f'Irá levar: {anos}')


Exercicio 51:
Um funcionário recebe aumento anual. Em 1995 foi contratado por 2000. Em 1996 recebeu aumento de 1.5%. A partir de
1997, os aumentos sempre correspondem ao dobro do ano anterior. Faça um programa que determine o salário anual


salario_i = 2000
anos = int(input('Digite a quantidade de anos que esta trabalhando na empresa: '))

if anos <= 1:
    print(salario_i)
else:
    salario_f = salario_i * (1 + (0.015 * (2 ** (anos-1))))
    print(salario_f)


Exercicio 52:
Escreva um programa que receba como entrada o valor do saque realizado pelo cliente de um bando e retorne
quantas notas de cada valor serão necessárias para atender ao saque com a menor quantidade de notas possível. Serão
utilizadas notas de 100, 50, 20, 10, 5, 2 e 1 real.

notas = [100, 50, 20, 10, 5, 2, 1]

saque = int(input('Digite o valor a ser sacado e será devolvido a menor quantidade de notas para este saque.\n'
                  'Saque: '))

print('Será sacado: ')

for i in notas:
    nota = (saque // i)
    if nota > 0:
        print(f'{int(nota)} nota de {round(i, 0)}', end=", ")
        saque -= nota * i


Exercicio 53:
Escreva um programa que leia um numero inteiro positivo n e em seguida imprima n linhas do chamado Triangulo
de Floyd.


def flody(n):
    quant = 1
    numero = 1
    for i in range(1, n+1):
        quant += 1
        for b in range(1, quant):
            print(str(numero).zfill(2), end='  ')
            numero += 1
        print()

    return None

flody(10)


#tive de procurar no curso do colega sobre transformar em str e usar a função zfill() não sei direito para oque é
# Após curso, a função zfill enche um numero com zeros a esquerda e recebe como parametro a quantidade de zeros e a
variável

numero = int(input('Digite um inteiro positivo para que seja impresso "n" linhas de Floyd. Numero: '))

while numero < 0:
    numero = int(input('Digite um numero valido: '))

    print(flody(numero, 1, 2))
    print('1')

Exercicio 54:
Faça um programa que receba um numero interio mairo do que 1, e verifique se o numero fornecido é primo ou não

numero = int(input('Digite um numero e será retornado se ele é primo. Numero: '))
primo = 0

for i in range(1, numero+1):
    if numero % i == 0:
        primo += 1
    elif primo > 2:
        break

if primo == 2:
    print(f'O numero {numero} é primo.')
elif numero == 1:
    print('Numero 1 é primo')
else:
    print('Não é primo')



Exercicio 55:
Escreva um programa que leia um inteiro não negativo n e imprima a soma dos n primeiros numeros primos

intervalo_f = int(input('Digite um numero inteiro positivo, para ser calculado a soma de seus numeros primos dentro'
                        'de seu intervalo. Numero: '))
n_primos = [1]
cont = [0, 0]

for i in range(1, intervalo_f+1):
    for b in range(1, i+1):
        if i % b == 0:
            cont[0] += 1
            cont[1] = i
    if cont[0] == 2:
        n_primos.append(cont[1])
    cont[0] = 0

print(f'Os numero primos são {n_primos} e sua soma é: {sum(n_primos)}')


# após terminar curso, otimizando


def seq_primo(numero):
    primos = []

    for dividendo in range(1, numero+1): # loop p percorrer cada numero

        if len(primos) < 2:
            primos.append(dividendo)
        else:
            cont = True
            for i in primos[1:]:
                if (dividendo % i) == 0:
                    cont = False
                    break

            if cont is True:
                primos.append(dividendo)

    return print(primos)

seq_primo(10_000)

Exercicio 56:
Faça um programa que calcule a soma de todos os numeros primos abaixo de dois milhoes

n_primos = [1]
cont = [0, 0]    # cont 0 é para ser o contador se é primo, pois tem de atender 2 cond e cont 1 é para colocar na lista

for i in range(1, 2_000_000):
    for b in range(1, i+1):
        if i % b == 0:
            cont[0] += 1
            cont[1] = i
    if cont[0] == 2:
        print(n_primos)
        n_primos.append(cont[1])
    cont[0] = 0

print(f'Os numero primos são {n_primos} e sua soma é: {sum(n_primos)}')


# após curso

def seq_primo(numero):
    primos = []

    for dividendo in range(1, numero+1): # loop p percorrer cada numero

        if len(primos) < 2:
            primos.append(dividendo)
        else:
            cont = True
            for i in primos[1:]:
                if (dividendo % i) == 0:
                    cont = False
                    break
                else:
                    pass

            if cont is True:
                primos.append(dividendo)
            else:
                pass

    return print(primos)


seq_primo(2_000_000)

Exercicio 57 não vou fazer, mesma coisa só muda um parametro
Exercicio 58 não vou fazer, mesma coisa só muda um parametro

Exercicio 59 falta terminar. Faltas apenas o maior, menor e media. Usei a função random para facilicar os testes.


import random

consumo = []
codigo = []
entrada = 0

habitantes = int(input('Digite o numero de habitantes: '))
kwh = int(input('Digite o valor do Kw/h: '))


for i in range(1, habitantes+1):
    for a in range(0, 2):
        # entrada = int(input(f'Informe o consumo em kwh do {i}º consumidor: '))
        entrada = random.randint(1, 1000)
        consumo.append(entrada)

        # entrada = int(input(f'Informe o código do {i}º consumidor. Sendo [1] Residencail, [2] Comercial e '
        #                    f'[3] Industrial: '))
        entrada = random.randint(1, 3)
        codigo.append(entrada)

consumo.index(max(consumo))


Exercicio 60 não vou fazer, é junção de tres exercicios anteriores
Exercicio 61 e 62, é interessante se sobrar tempo..

"""
