# # criar uma lista de notas
# notas = [6.25,2,10,9,8.8]
# # valor maximo de uma nota 
# print ('Maior valor:',max (notas))
# # valor minimo de uma nota da lista
# print ('Menor valor:',min(notas))
# # Quantidade de itens na lista de notas
# print ('Quantidade de notas:',len(notas))
# # Soma total das notas da lista
# print ('Soma das notas:',sum(notas))
# #mostrar media das notas da lista
# print (f"Media aritmetica: {sum(notas)/len(notas):.2f}")

# # operador in
# print (10 in notas) #ele (in) esta diretamente ligados a listas, ele verifica se o determinado numero esta ligado a lista

# # loop for com listas
# print (notas)
# for i in notas: # a letra i e o indice ele acessa cada item da lista
#     print (i, end=' ')

# leia 5 notas utilizando lista e estruturas de repetiçao

# notas = []

# for i in range(0,5): # no range o 0 foi o start e o 5 foi stop
#      num = float(input("Digite uma nota: "))
#      notas.append (num) 
# print ("as notas sao:", notas)
# print ("a soma das notas :", sum (notas)) 

# leia uma quantidade de notas determinadas pelo usuario e faça a soma dos valores 

# notas = []
# qnt_notas = int(input("Digite a quantidade de notas: "))
# for i in range(qnt_notas): 
#      num = float(input("Digite uma nota: "))
#      notas.append (num) 
# print ("A soma das notas :", sum (notas)) 

#Adicionar somente valores de zero ate 10

qnt_notas = int(input("Digite a quantidade de notas: "))
cont = 1
notas = []
while cont <=qnt_notas:
    num = float(input("Digite uma nota: "))
    if num>=0 or notas<=10:
        notas.append (num)
    else:
        continue
    cont +=1  
print ("A soma das notas :", sum (notas)) 