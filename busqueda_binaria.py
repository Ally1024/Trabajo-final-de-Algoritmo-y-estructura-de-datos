# busqueda_binaria.py

def buscar(lista, objetivo, clave):
    """
    Realiza una búsqueda binaria en una 'lista' ordenada para encontrar un 'objetivo'.
    Devuelve el objeto completo si lo encuentra, de lo contrario devuelve None.
    """
    bajo = 0
    alto = len(lista) - 1

    while bajo <= alto:
        medio = (alto + bajo) // 2
        valor_medio = clave(lista[medio])

        if valor_medio < objetivo:
            bajo = medio + 1
        elif valor_medio > objetivo:
            alto = medio - 1
        else:
            return lista[medio]
            
    return None