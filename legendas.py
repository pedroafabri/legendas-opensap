import re
from googletrans import Translator
import csv

with open("legendas.txt", "r") as file:

    content = file.read().replace('\n', '')
    matches = re.findall('(([0-9])([0-9]):([0-9])([0-9]):([0-9])([0-9]))', content)
    print('Alinhando legendas...')
    for match in matches:
        newString = '\n' + match[0] + ';'
        content = content.replace(match[0], newString)

print("Traduzindo as linhas... por favor, aguarde. Isso pode demorar um pouco")
splitted = content.split('\n')

#Arrumar array
counter = 0
toTranslate = []
for splitString in splitted:
    lineSplitted = splitString.split(';')
    if len(lineSplitted) == 2:
        splitted[counter] = lineSplitted
        toTranslate.append(splitted[counter][1])
        counter = counter + 1

translator = Translator()
translations = translator.translate(toTranslate, dest='pt')
counter = 0
newContent = ''
for translation in translations:
    print('Traduzindo linha {}'.format((counter + 1)))
    newContent += splitted[counter][0] + ';' + translation.text + '\n'
    counter = counter + 1

with open("legendas.csv", 'w') as file:
    file.write(newContent)
    print('Arquivo "legendas.csv" gerado!')
