'''
El programa debe mostrar un Menú con las siguientes opciones:
1) Solicitar al usuario una materia y listar los estudiantes con sus nombres y calificaciones correspondientes en esa materia.
2) Mostrar el estudiante con la calificación más alta y más baja considerando todas las materias.
3) Mostrar los estudiantes ordenados por su promedio de calificaciones de menor a mayor.
'''

from funciones import *

flag_correr = True
while flag_correr:
    opciones = int(input('''
    1) listar estudiantes.
    2) Mostrar estudiantes con calificación más alta y más baja.
    3) Mostrar estudiantes ordenados por su promedio de calificaciones de manera ascendente (menor a mayor)
    4) Salir
    Que deseas realizar: '''))

    match opciones:
        case 1:
            limpiar_pantalla()
            listar_estudiantes(estudiantes, calificaciones)
        case 2:
            limpiar_pantalla()
            mostrar_estudiantes_con_calificacion_alta(estudiantes, calificaciones)
        case 3:
            limpiar_pantalla()
            mostrar_estudiantes_por_promedio(estudiantes, calificaciones)
        case 4:
            limpiar_pantalla()
            print("Saliendo del programa!!")
            flag_correr = False
        case _:
            limpiar_pantalla()
            print("error ingrese una opcion valida!!")
