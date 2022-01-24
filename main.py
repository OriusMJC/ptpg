import porc_tsv as tsv
import fecha
import vali_año_sem as ano_sem
import porcentaje as porcent
from gen_clau import genero,claustro

    
def main():
    cant_denu = 0
    exp_max = 0
    cant_m = 0
    cant_v = 0
    cant_o = 0
    cant_estu = 0
    cant_docen = 0
    cant_nodocen = 0
    cant_gradu = 0
    calif_mas_tsv = 0
    cant_pares = 0
    ano_inf, seme_inf = ano_sem.vali_ano_sem()
    continuar = input('Presione ENTER para continuar')
    # PIDE DATOS DE CADA DENUNCIA
    while continuar != "n" and continuar != 'N':
        cant_denu = cant_denu + 1
        num_exp = int(input('Numero de expediente:  '))
        if num_exp > exp_max:
            exp_max = num_exp
        mes, dia = fecha.pide_fecha(ano_inf, seme_inf)
        print("Datos del denunciante:")
        gen_dente = genero()
        if gen_dente == "Varón":
            cant_v = cant_v + 1
        elif gen_dente == "Mujer":
            cant_m = cant_m + 1
        else:
            cant_o = cant_o + 1
        clau_dente = claustro()
        if clau_dente == "Estudiante":
            cant_estu = cant_estu + 1
        elif clau_dente == "Docente":
            cant_docen = cant_docen + 1
        elif clau_dente == "No Docente":
            cant_nodocen = cant_nodocen + 1
        else:
            cant_gradu = cant_gradu + 1 
        vio_sex,aco_sex,con_sex,com_acc_sex,calif_mas_tsv = tsv.porc_tsv(calif_mas_tsv)
        print("Datos del denunciado:")
        gen_dendo = genero()
        clau_dendo = claustro()
        if clau_dendo == clau_dente:
            cant_pares = cant_pares + 1
        #MUESTRA DATOS DE LA DENUNCIA    
        print("--------------Datos de la Denuncia----------------")
        print("Número de expediente:",num_exp)
        print("Fecha de la denuncia:", ano_inf,"-",mes,"-",dia)
        print("Género del denunciante:", gen_dente)
        print("Claustro del denunciante:", clau_dente)
        print("--Tipos de situaciones vivenciadas--")
        if vio_sex == True:
            print(" - Hechos de violencia sexual")
        if aco_sex == True:
            print(" - Hechos de acoso sexual")
        if con_sex == True:
            print(" - Hechos con connotación sexista")
        if com_acc_sex == True:
            print(" - Comportamientos y acciones de violencias")
        print("Género de la persona denunciada:", gen_dendo)
        print("Claustro de la persona denunciada:", clau_dendo)
        print("     ------------------------------")
        continuar = input('¿Continuar? S/N:  ')
    #MUESTRA DATOS DEL SEMESTRE 
    porcentaje = porcent.cal_porcent(cant_denu,calif_mas_tsv)
    print("\nAño del informe:", ano_inf)
    print("Semestre del informe:", seme_inf)
    print("Cantidad de denuncias: ", cant_denu)
    print(f"Porcentaje de denuncias en más de un tipo de situación vivenciada: {porcentaje:.2f} %")
    print("Cantidad de denuncias entre pares del mismo claustro: ", cant_pares)
    print("Mayor número de expediente: ", exp_max)
    print("Cantidad de denunciantes varones: ", cant_v)
    print("Cantidad de denunciantes mujeres: ", cant_m)
    print("Cantidad de denunciantes otres: ", cant_o)
    print("Cantidad de denunciantes del claustro de estudiantes: ", cant_estu)
    print("Cantidad de denunciantes del claustro de docentes: ", cant_docen)
    print("Cantidad de denunciantes del claustro de no-docentes: ", cant_nodocen)
    print("Cantidad de denunciantes del claustro de graduades: ", cant_gradu)
    print("Eso es todo")
    input("Enter para salir")
    
main()



