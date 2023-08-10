#  abertura de um arquivo chamado dados2.txt
# ler o nome de 10 pessoas e gravar no arquivo



try:
    txt = open ("aula09\dados2.txt", "w+")    # r(read) - apenas le, w(write) cria um aquivo e apaga conteudo se ja existir e o a+(append) cria e nao apaga 
    for i in range (1,11):
        pessoa = (input ("nome da pessoa: ")) 
        txt.write (f"{i} - Nome da pessoa: {pessoa}\n")    # o \n quebra de linha
except: 
    print('O caminho esta incorreto!!')
else:
    txt.seek(0)
    print (txt.read())
    txt.close()
    


