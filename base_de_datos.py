# base_de_datos.py

import random

def obtener_registros_estudiantes():
    """
    Genera y devuelve una lista FIJA con 5000 registros de estudiantes simulados.
    Usa una semilla para que la base de datos sea la misma en cada ejecución.
    """
    random.seed(2025) # La semilla asegura que los 5000 registros sean siempre los mismos

    registros = []
    cifs_usados = set()
    
    # -> CAMBIA ESTE NÚMERO
    while len(registros) < 5000:
        anio = random.randint(2018, 2024)
        numero = random.randint(1, 9999)
        letra = random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        
        cif = f"{anio}-{numero:04d}{letra}"
        
        if cif in cifs_usados:
            continue
        
        cifs_usados.add(cif)
        
        edad = random.randint(17, 25)
        calificacion = random.randint(40, 100)
        
        registros.append({'cif': cif, 'edad': edad, 'calificacion': calificacion})
        
    return registros