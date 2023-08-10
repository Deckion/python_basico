
try:
    txt = open ("aula09/dados.txt","r")    # abre o arquivo e tem q especificar o caminho (USANDO o w+ limpa)
    print('Arquivo encontrado!')
    txt.seek(0)                           #posiciona o cursor na primeira linha do txt para ler de cima pra baixo
    print (txt.read())
except:
    print ("problema ao abrir o arquivo, talvez caminho errado..")






