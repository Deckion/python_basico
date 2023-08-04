#Primeiro script em Python
print("Hello, World!!!!")
print('Curso programando com python')
print('-'*30)
print('Carga Horária: 40h \n10 dias')
# padrão snake case (variaveis)
nome_pessoa='Giuliano Prado'
nome_curso='Programando com Python'
idade=40
valor_curso=250.99
# mostrar tipos(type) de dados variaveis
print(type(nome_pessoa))
print(type(idade))
print(type(valor_curso))
#concatenar dados
print('Seja bem-vindo(a)',nome_pessoa)
print("Seja bem-vindo(a)",nome_pessoa,"ao curso", nome_curso)
# o curso <nome_curso> custa <valor>
print("Seja bem-vindo(a)","o curso",nome_curso,"custa R$",valor_curso) 
# f-strings (identifica a variavel) no python 
print(f"Seja bem-vindo {nome_pessoa}") 
print(f'O valor do curso {nome_curso} é R$ {valor_curso}')
print(f"Seja bem-vindo {nome_pessoa} \n\nO curso {nome_curso} custa R${valor_curso}")