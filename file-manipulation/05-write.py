# 'r+' va a leer y escribir
with open('text.txt', 'r+', encoding='utf-8') as file:
    for line in file:
        print(line)
    file.write('nueva linia insertada\n')
    file.write('nueva 2 linia insertada\n')
    file.write('nueva 3 linia insertada\n')

'''
# 'w+' va a sobreescribir, lo remplaza
with open('text.txt', 'w+', encoding='utf-8') as file:
    for line in file:
        print(line)
    file.write('nueva linia insertada\n')
    file.write('nueva 2 linia insertada\n')
    file.write('nueva 3 linia insertada\n')
'''