# abre o arquivo em modo de escrita
arquivo = open("exemplo.txt", "w")

# escreve informações no arquivo
arquivo.write("Este é um exemplo de arquivo em Python.\n")
arquivo.write("Podemos escrever informações nele com a função write().\n")

# fecha o arquivo
arquivo.close()




# abre o arquivo em modo de leitura
arquivo = open("exemplo.txt", "r")

# lê todas as linhas do arquivo
linhas = arquivo.readlines()

# imprime as linhas do arquivo
for linha in linhas:
    print(linha)

# fecha o arquivo
arquivo.close()


# abre o arquivo original em modo de leitura
arquivo_origem = open("exemplo.txt", "r")

# abre o arquivo de destino em modo de escrita
arquivo_destino = open("copia.txt", "w")

# copia as informações do arquivo original para o arquivo de destino
for linha in arquivo_origem:
    arquivo_destino.write(linha)

# fecha os arquivos
arquivo_origem.close()
arquivo_destino.close()



import os

# move o arquivo para a pasta de destino
pasta_destino = "/home/usuario/documentos/"
arquivo_origem = "exemplo.txt"
arquivo_destino = os.path.join(pasta_destino, arquivo_origem)
os.rename(arquivo_origem, arquivo_destino)






# remove o arquivo
arquivo = "exemplo.txt"
os.remove(arquivo)
