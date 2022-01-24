def cal_porcent(denu_total,cant_tsv):
    """Recibe 2 parámetros (cant_denu, calif_mas_tsv). Calcula el porcentaje (porcentaje)
    de todas las denuncias que cumplan con más de dos TSV (cien divido la cantidad de 
    denuncias totales, multiplicado por cantidad de denuncias calificadas en más de un TSV)."""
    if denu_total != 0:
        porcent = (100/denu_total)*cant_tsv
        return porcent
    else:
        return 0