# aula de listas

lista  = [2,8,19,4,55,'coxinha',34,'maionese',33]
print (type(lista))
print ('primeiro item da lista:', lista[0])
print ('ultimo item da lista:', lista[8])
print ('ultimo item da lista:', lista[-1]) # <-sempre vai mostrar o ultimo item da lista 
print ('penultimo item da lista:', lista[-2]) # <- sempre vai mostrar o penultimo item da lista
print ('quantidade de item da lista:', len(lista)) #mostra quantidade de itens da lista

# print ('lista ordenada:',sorted(lista))
pc = ['mouse','monitor', 'HD','memoria ram', 'Camera']

# mostrar lista em ordem conforme os itens
print (sorted (pc)) #mostra a lista em ordem alfabetica, ele da prioridade a letras maiusculas
lista2 =[6,8,4,11,55,0,3] #organiza a lista do menor pro maior
print (sorted (lista2))

# mostrar intervalos da lista
print(lista2 [2:5]) #intervalos
print (lista2 [3:]) #intervalo aberto ele vai ate o final nesse exemplo
print(lista2 [:4])

# adicionar item ao final da lista
lista2.append(1000) #adiciona um item na lista sempre no final
print (lista2)

# inserir item em posiçao determinada da lista
lista2.insert (2,5000) #adiciona na posiçao 2 o numero 5000
print (lista2)

# unir duas listas
lista2.extend (lista) #o lista2 chamou o lista, entao ele agregou os elementos da "lista"
print (lista2)

# remover o ultimo item da lista ou o indice informado
lista2.pop() #caso eu informe a posição, ele vai remover o informado
print (lista2)

# remover item especifico da lista
lista2.remove ('coxinha')
print (lista2)

# copiar referencia
lista3 = pc # no caso lista3 recebeu os dados da lista pc (mesmo espaço de memoria)
#copiar objeto
pc2 = pc.copy() #duplica a lista
print ('lista 3', lista3)
print ('lista 4', pc2)
pc.append('SSS')
pc.append('Teclado')
print (lista3)
lista3.append('Placa de Video') 
print (pc2)
print (pc)
