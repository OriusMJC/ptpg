def vali_ano_sem():
    """Pide al usuario año y semestre del informe. Mientras año sea menor que 2021,
    pide su reingreso. Mientras semestre sea distinto de 1 y de 2, pide su reingreso.
    Devuelve el año y semestre verificados"""
    ano_inf = int(input('Año de ingreso:  '))
    while ano_inf < 2021:
        print ('Año no valido')
        ano_inf = int(input('Año de ingreso:  '))
    seme_inf = int(input('Semestre:  '))
    while seme_inf != 1 and seme_inf != 2:
        print ('Semestre no valido')
        seme_inf = int(input('Semestre:  '))
    return ano_inf,seme_inf