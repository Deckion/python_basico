

# Tupla ----NAO PODE SER ALTERADA----

cidades = ('Manaus','Coari','Parintins','Manacapuru','Anori')
print (type(cidades))

# mostrar o ultimo item da tupla
print (cidades[-1])
# mostrar o primeiro item da tupla
print (cidades[0])
# Mostrar itens ordenados 
print (sorted (cidades))
print (cidades.count('Manaus')) #conta quantas vezes aparece palavra Manaus

# Leia 3 numeros positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e menor valor informado.
lista=[]

for i in range(3): 
     num = int(input("Digite um numero: "))
     lista.append(num)
     
print ("ordem crescente :", sorted(lista)) 
print ('Maior valor',max (lista))
print ('Menor valor',min (lista))









