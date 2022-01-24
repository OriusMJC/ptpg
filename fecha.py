def pide_fecha(ano,sem):
    """Recibe parámetros (año, sem). Pide que se ingrese el mes(mes) y el día(dia) de la denuncia,
    mientras el mes y día no sean correctos según el año y el semestre, pide el reingreso de ambos datos. 
    Devuelve mes y día, verificados."""
    mes = int(input("Ingrese el mes de la denuncia: "))
    if sem == 1:
        while mes < 1 or mes > 6:  
            print ('mes no valido')
            mes = int(input('Ingrese el mes:  '))
    else:                           
        while mes < 7 or mes > 12:    
            print ('mes no valido')
            mes = int(input('Ingrese el mes:  '))
    dia = int(input("Ingrese el dia de la denuncia: "))
    if mes == 2:
        if ano % 4 == 0:
            while dia < 1 or dia > 29:
                print ('dia no valido')
                dia = int(input('Ingrese el dia:  '))
        else:
            while dia < 1 or dia > 28:
                print ('dia no valido')
                dia = int(input('Ingrese el dia:  '))
    elif mes == 1 or mes == 3 or mes == 5 or mes == 7 or\
        mes == 8 or mes == 10 or mes == 12:
        while dia < 1 or dia > 31:
            print ('dia no valido')
            dia = int(input('Ingrese el dia:  '))
    else:                           
        while dia < 1 or dia > 30:
            print ('dia no valido')
            dia = int(input('Ingrese el dia:  '))
       
    return mes, dia