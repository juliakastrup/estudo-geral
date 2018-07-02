# baseado em https://gist.github.com/davidbauer/11055010

#!/usr/bin/env python

# assume que há um arquivo csv 
# cuja primeira coluna contém o nome a ser utilizado na imagem
# e a segunda coluna contém o nome do arquivo de imagem
# assume que o caminho para o arquivo é o mesmo

import urllib
import csv
from slugify import slugify

filename = "nomedocsvorigem"

with open("{0}.csv".format(filename), 'r') as csvfile:
    # iterate on all lines
    i = 0
    csvfile = csv.reader(csvfile)
    for line in csvfile:
        # protege o nome do arquivo, que será usado nos arquivos de log e na mensagem 
        nameimage = line[0]
        # transforma cada linha da primeira coluna em 'slugs' para evitar problemas de encoding:
        line[0] = slugify(line[0])

        # transforma cada '/' da primeira coluna em '-':
        if line[0].find('/'):
            line[0] = line[0].replace('/','-')

        # verifica se há url válida para cada linha da primeira coluna:
        if line[1]:
            # monta a url, utilizando o caminho para o arquivo de imagem  + nome do arquivo de imagem
            # exemplo:  
            # urllib.urlretrieve("https://d1pkzhm5uq4mnt.cloudfront.net/imagens/capas/" + line[1], line[0] + ".jpg")
            sucesso = open("imagem-salva.txt","a")
            urllib.urlretrieve("https://www.caminho.para/imagem/" + line[1], line[0] + ".jpg")
            print "Image saved for {0}".format(nameimage)
            sucesso.write("Image saved for {0}\n".format(nameimage))
            i += 1
        else:
            erro = open("nao-encontrada.txt","a")
            print "No result for {0}".format(nameimage)
            erro.write("No result for {0}\n".format(nameimage))