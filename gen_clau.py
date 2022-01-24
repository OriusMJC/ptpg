def genero():
    """Pide el género (genero) y mientras este sea diferente de “m”, “v” y “x”
    pide su reingreso. Devuelve género validado"""
    genero = input("Ingrese el género: v:varon, m:mujer, x:otre : ")
    gen = ('m','v','x')
    while genero not in gen:
        print("Género no válido, ingreselo nuevamente y en MINÚSCULAS.")
        genero = input("Ingrese su genero: v:varon, m:mujer, x:otre : ")
    if genero == "m":
        return "Mujer"
    elif genero == "v":
        return "Varón"
    else:
        return "Otre"
        

def claustro():
    """Pide el claustro (claustro) y mientras sea diferente de “e”, “d”, “nd” y “g”
    pide su reingreso. Devuelve claustro validado."""
    claustro = input("Ingrese su claustro: e:estudiante, d:docente, nd:no docente, g: graduade : ")
    clau = ('e','d','nd','g')
    while claustro not in clau:
        print("Claustro no válido, ingreselo nuevamente y en MINÚSCULAS.")
        claustro = input("Ingrese su claustro: e:estudiante, d:docente, nd:no docente, g: graduade : ")
    if claustro == "e":
        return "Estudiante"
    elif claustro == "d":
        return "Docente"
    elif claustro == "nd":
        return "No Docente"
    else:
        return "Graduade"