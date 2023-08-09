'''1.	Crie um dicionário contendo os nomes dos estados abreviados (Chave) e os nomes das capitais (Valor) da região norte e nordeste. Mostre ao final as informações relacionadas ao amazonas e Sergipe.'''



# norte = {'AM':'Manaus', "AC":"Rio Branco", "AP":"Macapá",  "PA":"Belém" , "RO":"Porto Velho", "RR":"Boa Vista","TO": "Palmas"}
# nordeste = { 'MA':'São Luís' , 'PI':'Teresina' , 'CE': 'Fortaleza', "RN":'Natal' , "PB":'João Pessoa', "PE":"Recife" , "AL":"Maceió", "SE":"Aracaju.", "BA":"Salvador"}

# print (norte["AM"], "e", nordeste ["SE"])



'''2.	Crie um script que leia o nome de 5 alunos e mostre os dados informados em ordem alfabética'''

# aluno = []
# cont=1
# while cont <=5:
# 	nome = input("Digite nome dos guri: ")
# 	aluno.append(nome)
# 	cont +=1
# aluno.sort()
# print (aluno)


'''3.	Crie uma lista com os seguintes valores: 
[2,10,30,85,2,6,0,4]
 	- Mostre apenas o terceiro valor
	- Mostre apenas o último valor
    - Mostre o dobro de cada valor'''

# list = [2,10,30,85,2,6,0,4]

# print ('Terceiro valor:', list[2])
# print ('ultimo valor:', list[-1])
 
# list2 = [i*2 for i in list]
# print(list2)

'''4.	Qual a principal diferença entre uma lista e uma tupla em Python?'''

'''5.	Pesquise e responda quais a principais características da Estrutura Set em Python.'''

'''6.	Descreva quatro exemplos de funções/métodos que podem ser aplicados em um dicionário.'''

'''7.	Crie um script que leia dez números positivos e armazene os dados em uma lista, mostre os dados em ordem crescente, o maior valor informado e menor valor informado.'''

num = []

for i in range(10):
        numero = float(input(f"Digite o {i+1}º número positivo: "))
        while numero <= 0:
            numero = float(input("Número inválido. Digite um número positivo: "))
        num.append(numero)

num.sort()
menor_num = num[0]
maior_num = num[-1]

print("\nNúmeros em ordem crescente:", num)
print("Menor valor:", menor_num)
print("Maior valor:", maior_num)