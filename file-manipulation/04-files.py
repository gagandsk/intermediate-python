# Dentro de tu archivo 04-files.py

try:
    with open('text.txt', 'r', encoding='utf-8') as file:
        contenido = file.read()
        # contenido = file.readline()
        print(contenido)
        # for line in file:
            # print(line)
        file.close()
except FileNotFoundError:
    print("El archivo text.txt no fue encontrado en la ubicación especificada.")
except Exception as e:
    print(f"Ocurrió un error: {e}")