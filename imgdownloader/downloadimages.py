# baseado em https://gist.github.com/davidbauer/11055010

#!/usr/bin/env python

# assuming a csv file with a name in column 0 and the image url in column 1

import urllib
import csv
from slugify import slugify

filename = "capas-sebolinha"

with open("{0}.csv".format(filename), 'r') as csvfile:
    # iterate on all lines
    i = 0
    csvfile = csv.reader(csvfile)
    for line in csvfile:
        nameimage = line[0]
        line[0] = slugify(line[0])

        if line[0].find('/'):
            line[0] = line[0].replace('/','-')
        # check if we have an image URL
        if line[1]:
            sucesso = open("capas-salvas.txt","a")
            urllib.urlretrieve("https://d1pkzhm5uq4mnt.cloudfront.net/imagens/capas/" + line[1], line[0] + ".jpg")
            print "Image saved for {0}".format(nameimage)
            sucesso.write("Image saved for {0}\n".format(nameimage))
            i += 1
        else:
            erro = open("sem-capas.txt","a")
            print "No result for {0}".format(nameimage)
            erro.write("No result for {0}\n".format(nameimage))