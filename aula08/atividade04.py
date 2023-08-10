# '''1 - Crie uma função em Python para retornar a área de um retângulo, considere a seguinte fórmula: A=b.h'''

# def area(b,h):
#     a = b*h
#     return a


# '''2 -Crie uma função em Python para mostrar a área de um círculo, considere a seguinte fórmula: A= pi.r² '''
# def area_circ(r):
#     a = (3.14 * (r**2))
#     return a

# '''3 - Crie uma função em Python para mostrar o produto da multiplicação entre n valores.'''
# def mult_valor (*valor1):
#     produto =1
#     for valor in valor1:
#         produto *= valor
#     return produto

'''4 - Crie uma função em Python para mostrar apenas as chaves de um dicionário. '''

def chaves (dic):
  for chave in dic:
    print(chave)

dicionario = {"c": 1, "o": 2, "x": 3, "i": 4, "n": 5, "h": 6, "a": 7}
chaves(dicionario)

'''5 - Crie uma função em Python para mostrar apenas os valores de um dicionário. '''

def valores (dic):
    for valor in dic.values():
        print(valor)

dicionario = {"c": 1, "o": 2, "x": 3, "i": 4, "n": 5, "h": 6, "a": 7}
valores(dicionario)

'''6 - Crie uma função em Python para mostrar as chaves e os valores de um dicionário.'''

def chave_e_valor(dic):
  for chave, valor in dic.items():
    print(chave, valor)

dicionario = {"c": 1, "o": 2, "x": 3, "i": 4, "n": 5, "h": 6, "a": 7}
chave_e_valor (dicionario)

'''7 - Crie uma função em Python para retornar a quantidade de itens existentes em um dicionário.'''