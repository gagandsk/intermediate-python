set_countries = {'col', 'mex', 'bol'}

#len() : Devuelve el tamaño del 
size = len(set_countries)
print (size)

print('col' in set_countries)
print('peru' in set_countries)

# add(): Añade un elemento al conjunto.
set_countries.add('pe')
print(set_countries)
set_countries.add('pe')
print(set_countries)


# update(): Añade cualquier tipo de 
set_countries.update({'ar', 'es', 'ecua', 'pe'})
print(set_countries)

# remove(): Elimina un elemento y si este no existe lanza el error “keyError”
set_countries.remove('col')
print(set_countries)
set_countries.remove('ar')
print(set_countries)


# discard(): Elimina un elemento y si ya existe no lanza ningún error
set_countries.discard('arg')
print(set_countries)

set_countries.add('arg')
print(set_countries)

# pop(): Nos devuelve un elemento aleatorio y lo elimina y si el conjunto está vacío lanza el error “key error”.
print(set_countries.pop())
print(set_countries)

# clear(): Elimina todo el contenido del conjunto
set_countries.clear()
print(set_countries)

print(len(set_countries))