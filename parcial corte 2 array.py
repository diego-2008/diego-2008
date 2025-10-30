def invertir_array(array):
    return array [::-1]
cantidad = int(input("ingrese la cantidad de elemnetos del array: "))
array = []
for i in range (cantidad):
    elemento = input(f"ingrese el elemento {i + 1}:")
    array.append(elemento)
    print("array original:", array)
    array_invertido = invertir_array (array)
    print("array invertido:", array_invertido)
    
    