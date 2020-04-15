# coding: utf-8

import os
import sys

with open(sys.argv[1]) as fr:
    for line in fr.readlines():
        if line.startswith('![Figure') or line.startswith('![Table'):
            start = line.find('(')
            end = line.find(')')
            image_url = line[start+1:end]
            start = line.find('[')
            end = line.find(']')
            save_name = line[start+1:end]
            os.system('wget ' + image_url + ' -O ' + save_name + '.png')