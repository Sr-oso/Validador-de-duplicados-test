def interseccion_anidada(A, B):
    interseccion = []

    for elemento_a in A:
        for elemento_b in B:
            if elemento_a == elemento_b:
                interseccion.append(elemento_a)
                break

    return interseccion


def busqueda_binaria(arr, objetivo):
    izquierda = 0
    derecha = len(arr) - 1

    while izquierda <= derecha:
        medio = (izquierda + derecha) // 2

        if arr[medio] == objetivo:
            return True
        elif arr[medio] < objetivo:
            izquierda = medio + 1
        else:
            derecha = medio - 1

    return False


def interseccion_busqueda_binaria(A, B):
    B_ordenado = sorted(B)

    interseccion = []

    for elemento in A:
        if busqueda_binaria(B_ordenado, elemento):
            interseccion.append(elemento)

    return interseccion


def interseccion_hash(A, B):
    conjunto_B = set(B)

    interseccion = []

    for elemento in A:
        if elemento in conjunto_B:
            interseccion.append(elemento)

    return interseccion