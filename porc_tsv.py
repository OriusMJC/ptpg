def porc_tsv(cantidad):
    '''Recibe un parámetro (cantidad). Pide al usuario que confirme el tipo/s
    de situación/es vivenciada/s. Si hay más de un tsv le suma uno a (cantidad)
    Devuelve el/los tipo/s de situación/es vivenciada/s y la cantidad de denuncias 
    que tengan más de un TSV.'''
    vio_sex = False
    aco_sex = False
    con_sex = False
    com_acc_sex = False
    cant = 0
    error = True
    while error != False:
        situ = input("Hecho de violencia sexual S/N: ")
        if situ == 'S' or situ == 's':
            vio_sex = True
            cant += 1
        situ = input("Hecho de acoso sexual S/N:")
        if situ == 'S' or situ == 's':
            aco_sex = True
            cant += 1
        situ = input("Hecho con connotación sexista S/N:")
        if situ == 'S' or situ == 's':
            con_sex = True
            cant += 1
        situ = input("Comportamientos y acciones de violencia S/N:")
        if situ == 'S' or situ == 's':
            com_acc_sex = True
            cant += 1
        if cant > 0:
            error = False
        else:
            print("Debe seleccionar al menos una opción: ")
    if cant > 1:
        cantidad += 1
    return vio_sex,aco_sex,con_sex,com_acc_sex,cantidad