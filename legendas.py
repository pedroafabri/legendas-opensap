import re

with open("legendas.txt", "r") as file:

    content = file.read().replace('\n', '')
    matches = re.findall('(([0-9])([0-9]):([0-9])([0-9]):([0-9])([0-9]))', content)

    for match in matches:
        newString = '\n' + match[0] + ';'
        content = content.replace(match[0], newString)
        print("Alinhada legenda {}".format(match[0]))

with open("legendas.csv", 'w') as file:
    file.write(content)
