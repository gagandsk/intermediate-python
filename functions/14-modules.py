import sys
import re
import time
import collections #util para manejar listas

print(sys.path)
text = 'MI NUMERO DE TELEFONO ES 123 123 123, el codigo del pais es 34, mi numero de la suerte es 10'

result = re.findall('[0-9]+', text)
print('all numbers coincidence =>', result)

timestamp = time.time()
localTime = time.localtime()
result = time.asctime(localTime)
print(timestamp)
print('local time =>', result)

numbers = [1,2,3,4,5,6,7,8,9,1,2,3,4,5]
counter = collections.Counter(numbers)
print(counter)
