import random

def es_camaleon(num):
    suma_digitos = sum(int(d) for d in str(num))
    invertido = int(str(num)[::-1])

    condicion1 = (suma_digitos % 2 == 0)
    condicion2 = (invertido % 3 == 0)

    return condicion1 and condicion2, suma_digitos, invertido

if __name__ == "__main__":
    n = int(input("cantidad de números a validar: "))

    numeros = [random.randint(100, 999) for _ in range(n)]

    print("\nnúmeros generados:", ", ".join(map(str, numeros)))
    print("\nresultados:")

    for num in numeros:
        cumple, suma, invertido = es_camaleon(num)
        if cumple:
            print(f"{num} -> Sí (suma={suma}, invertido={invertido} divisible entre 3 → Sí)")
        else:
            print(f"{num} -> No (suma={suma}, invertido={invertido})")
