# baseado em https://gist.github.com/davidbauer/11055010

# https://github.com/django/django/blob/master/django/utils/text.py#L403

#!/usr/bin/env python

# assuming a csv file with a name in column 0 and the image url in column 1

import urllib
import csv
import unicodedata
import re
import os
from urllib.request import urlretrieve
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
arquivo = logging.FileHandler('_download.log')
arquivo.setLevel(logging.INFO)
formatter = logging.Formatter('%(levelname)s: %(message)s')
arquivo.setFormatter(formatter)
console = logging.StreamHandler()
console.setFormatter(formatter)
console.setLevel(logging.INFO)
logger.addHandler(arquivo)
logger.addHandler(console)

def slugify(value, allow_unicode=False):
    """
    Convert to ASCII if 'allow_unicode' is False. Convert spaces to hyphens.
    Remove characters that aren't alphanumerics, underscores, or hyphens.
    Convert to lowercase. Also strip leading and trailing whitespace.
    """
    value = str(value)
    if allow_unicode:
        value = unicodedata.normalize('NFKC', value)
    else:
        value = unicodedata.normalize('NFKD', value).encode('ascii', 'ignore').decode('ascii')
    value = re.sub(r'[^\w\s-]', '', value).strip().lower()
    return(value)

filename = "capas-sebolinha"

def main():
    with open("{0}.csv".format(filename), 'r') as csvfile:

        pasta = os.path.join(os.path.dirname(__file__), 'capas')
        if not os.path.exists(pasta):
            os.mkdir(pasta)

        csvfile = csv.reader(csvfile)
        for line in csvfile:
            image_name = line[0]
            image_slug = slugify(line[0])
            image_file = line[1]

            # check if we have an image URL
            if image_file:
                urlretrieve(
                    "https://d1pkzhm5uq4mnt.cloudfront.net/imagens/capas/{0}".format(image_file),
                    'capas/{0}.jpg'.format(image_slug)
                )
                logger.info('Image saved for %s', image_name)
            else:
                logger.error('No result for %s', image_name)

if __name__ == '__main__':
    main()