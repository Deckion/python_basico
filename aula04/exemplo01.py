# # estruturas de repetição WHILE (continuação)
# # Leia 5 números e mostre a soma de todos os valores informados

# cont = 1
# soma = 0 # acumulador ( ele vai guardar o produto da soma, no caso)

# while cont <= 5:
#     num = float (input('informe um valor:') )
#     soma = soma+num  # mesmo que += num (no caso) 
#     cont +=1
# print ('Resultado da soma:', soma)

# # calcular a soma dos valores do intervalo (fechado) das variaveis "a" e "b" (280)
# a = 10
# b = 25
# num=0

# while a<=b:
#     print (a, end=" ")
#     num = num+a   
#     a+=1 
# print ('\nResultado:', num)

# # leia dois valores(inteiros) e mostre a soma do intervalo entre eles
# v1 = int (input ('Valor 1:'))
# v2 = int (input ('Valor 2:'))
# num = 0
# if v1<v2:
#     while v1<=v2:
#         num +=v1
#         v1+=1
#     print ('Resultado:', num)    
# elif v2<v1:
#     while v2<=v1:
#         num +=v2
#         v2 +=1
#     print ('Resultado:', num)  
# else:
#     print ('Infelizmente valores sao iguais')

#Soma 5 valores positivos informados pelo usuário
 
# cont = 1
# pos = 0 # acumulador 

# while cont <= 5:
#     num = float (input('informe um valor positivo:') )
#     if num<0:
#         continue # continua o programa e ignora a informação 
#     pos = pos+num 
#     cont +=1   
# print ('Resultado da soma:', pos)

#Soma 5 valores negativos informados pelo usuário

cont = 1
pos = 0 # acumulador 

while cont <= 5:
    num = float (input('informe um valor negativo:') )
    if num>=0:
        print('Voce digitou numero positivo!')
        break # para o programa e ignora a informação 
    pos = pos+num 
    cont +=1   
print ('Resultado da soma:', pos)

# Leia 3 notas e mostre a media, caso seja digitado um valor negativo OU acima de 10 sera solicitado um novo valor

# cont = 1
# nota = 0 # acumulador 

# while cont <= 3:
#     num = float (input('informe uma nota: ') ) #vai ser onde insere as notas
#     if num<0 or num>10:
#         print ('digite outra nota! ')
#         continue 
#     nota = nota+num
#     cont +=1   
# print ('Resultado da media:', nota/3)





