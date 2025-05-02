def find_volume(length=1, width=1, depth=1):
    #return length * width * depth
    return length * width * depth, width, 'hola' # devuelve una tupla

result = find_volume(width=10)
result, width, text = find_volume(width=10)

print(result)
print(width)
print(text)