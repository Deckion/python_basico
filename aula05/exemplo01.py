# # exemplos da funçao range () uma funçao q define intervalos sequenciados
# print (list (range(2,15)))
# print (list (range(10)))
# print (range (10))
# print (list (range (10,100,5 ))) # a terceira casa dentro do parenteses e pra acrescentar ou diminuir os valores da frente no caso ai 15,20,25 etc
# print ('-'*50)

# # loop for - 
# for i in range (10):
#     print (i, end=' ')
# print ('\nvalor final do contador: ', i)
# print ('-'*50)

# # contagem de 20 ate 30 usando laço for

# for i in range (20,31):
#     print (i, end=' ')

# # contagem 10 ate zero usando o laço for

# for i in range (10,-1, -1):
#     print (i, end=' ')

#  LEIA 5 numeros inteiros e mostre uma msg qnd o numero for  par

# for i in range (5):
#     num = int (input(" informe o valor: "))
#     if num %2==0: # a porcentagem indica o resto da divisao por 2 para achar o par
#         print ('o valor informado é par! ')
#     else:
#         print ('o valor informado é impar!')

#  LEIA 5 numeros e some somente os valores impares e mostre a quantidade de impares 
cont = 0
soma = 0
media = 0
print ("soma dos numeros impares informe valor abaixo: ")
for i in range (5):
    num = int (input(" informe o valor: "))
    if num%2!=0: # para achar o impar
        soma+=num
        cont+=1
    else:
       print ('o valor informado é par, digite impar!')     
print ('\na soma dos impares é:', soma)        
print ('\na quantidade de impares é: ', cont)  
# mostre a media aritimetica dos impares
print (f'a media de impares é {soma/cont:.2f}')
# pode ser assim tb
media = soma/cont 
print ('resultado: ', media)        





