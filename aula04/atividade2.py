'''1.	Crie um script em Python para receber dois números informados pelo usuário e mostrar todos números entre eles em ordem decrescente.'''


# num1 = int(input("Digite o primeiro número: "))
# num2 = int(input("Digite o segundo número: "))

   
# if num1 > num2:
#         inicio = num1
#         fim = num2
# else:
#         inicio = num2
#         fim = num1
# print("Números entre", inicio, "e", fim, "em ordem decrescente:")
# for numero in range(inicio, fim - 1, -1):
#         print(numero)
# print ('fim')


'''2.	Faça um script que mostre uma contagem iniciando em 10, finalizando em 500 com incremento de 5 em 5.'''
# a = 10
# b =500
# num =0

# while a<=b:
#     print (a, end=" ")
#     a+=5
# print ('\nfim')

'''3.	Faça um script que mostre os números pares em um intervalo definido pelo usuário.'''


# inicio = int(input("Digite o número de início: "))
# fim = int(input("Digite o número de fim: "))


# if inicio > fim:                 # Garantir que o início seja menor ou igual ao fim
#     inicio, fim = fim, inicio
# print("Números pares entre", inicio, "e", fim, "são:")
# for numero in range(inicio, fim + 1):
#     if numero % 2 == 0:
#         print(numero)


'''4.	Faça um script que leia dois valores positivos e mostre a soma dos números ímpares entre eles.'''


# soma = 0
# cont = 0
# num = 0
# while cont<=num:
#     num = int (input ('Insira numero: '))
#     if num%2!=0:
#         soma +=num
#         cont +=1
# print ('\na soma dos impares é:', soma) 





'''5.	Faça um script que mostre uma sequência numérica iniciando em 63, terminado em 129, calcule e mostre a soma destes valores.'''

# for i in range(63, 130):
#     print(i)

# soma = 0

# for i in range(63, 130):
#     soma += i
# print("A soma é", soma)    


'''6.	Faça um script em Python para receber dois números informados pelo usuário, mostre o valor da soma de todos os números entre eles e a média dos valores.'''

# pnum = int(input("Digite o primeiro número: "))
# snum = int(input("Digite o segundo número: "))
# inicio = min(pnum,snum) 
# fim = max(pnum, snum)
# soma =0
# for i in range(inicio, fim+ 1):
#     soma += i

# media = soma / fim # <--- media 

# print("A soma dos números entre", pnum, "e", snum, "é", soma)
# print("A média dos números entre", pnum, "e", snum, "é", media)

'''7.	Faça um script em Python mostre a tabuada de multiplicação do 8, iniciando do 0 até o 10.'''

'''8.	Crie um script em Python que leia dez números e mostre a média dos valores informados.'''

'''9.	Crie um script em Python que leia 5 números e mostre o maior valor informado.'''

# cont = 1
# num =0
# while cont<=5:
#     num1 = int (input ('Insira numero: '))
#     if num1>num:
#        num=num1
#     cont+=1

# print ("maior:", num)    



'''10.	Crie um script em Python que leia 5 números e mostre o maior valor e o menor valor informado.'''

# maior = 0
# menor = float("inf")

# for i in range(1,5):
#     numero = float(input("Digite um número: "))

#     if numero > maior:
#         maior = numero

#     if numero < menor:
#         menor = numero

# print("O maior número é:", maior, 'o menor numero é:', menor)

    
'''11. Faça um script em Python que leia 10 valores positivos e mostre, no final, a soma dos números pares e a soma dos números ímpares'''


# for i in range(1,10):
#     numero = float(input("Digite um número: "))