# ordenamiento_radix.py

def _ordenamiento_conteo_para_radix(lista, exponente, clave):
    """Función auxiliar para Radix Sort (privada)."""
    n = len(lista)
    salida = [0] * n
    conteo = [0] * 10

    for i in range(n):
        indice = (clave(lista[i]) // exponente)
        conteo[indice % 10] += 1

    for i in range(1, 10):
        conteo[i] += conteo[i - 1]

    i = n - 1
    while i >= 0:
        indice = (clave(lista[i]) // exponente)
        salida[conteo[indice % 10] - 1] = lista[i]
        conteo[indice % 10] -= 1
        i -= 1

    for i in range(n):
        lista[i] = salida[i]

def ordenar(lista, clave):
    """
    Ordena una lista de objetos usando Radix Sort basándose en una clave numérica.
    """
    if not lista:
        return lista
    
    valor_maximo = max(lista, key=clave)
    numero_maximo = clave(valor_maximo)

    exponente = 1
    while numero_maximo // exponente > 0:
        _ordenamiento_conteo_para_radix(lista, exponente, clave)
        exponente *= 10
    return lista