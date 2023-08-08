# trabalhar com estrutura de dados dicionario (dict)
# [] # lista
# () # tupla

dados = {} # para iniciar e identificar o dict tem q usar chaves
print (type(dados))
# estrutura chave e valor (dicionario)
alunos = {111: 'Karla Silva', 222:'Hélio Santos', 333: 'Manoel Gomes', 444:'Bruna Surfistinha'}

# mostrar primeiro item do dicionario
print (alunos[111])
# mostrar somente as chaves do dicionario
print (alunos.keys())
# mostrar somente os valores armazenados no dicionario
print (alunos.values())
# mostrar todos os itens do dicionario
print (alunos.items())
# Atualizar dicionário 
alunos.update({555:'Paulo da borracharia'})
print ('alunos')
# outra maneira de adicionar um item ao dicionario
alunos [666] = 'teste'
print (alunos)
alunos [111] = "Carlos Silva" #altera o primeiro item do dicionario
print (alunos)
# Excluir um item do dicionario
alunos.pop(666)
print (alunos)
# Mostrar somente os valores do dicionario
for i in alunos.values():
    print (i)
# Mostrar somente as chaves do dicionario
for i in alunos.keys():
    print (i)
# mostrar todos dos itens de um dicionario
for i in alunos.items():
    print (i)

for i,j in alunos.items():
    print (i, ' - ', j)

for i,j in alunos.items():
    print (i,j,sep=' 👍 ') # separador

# dicionario com lista

dados = {
    'lista_a':[1,2,2,5,8],
    'lista_b':[10,20,30,40],
    'lista_c':[100,200,300,400]    
}
print (dados)
print (type(dados))

# mostrar o ultimo item da lista b

print (dados ["lista_b"][3])



















