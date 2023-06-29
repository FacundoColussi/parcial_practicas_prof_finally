"""Escribe un programa que calcule el promedio general de una clase."""

# Ingreso de datos
cantidad_alumnos = int(input("Ingrese la cantidad de alumnos: "))

alumnos = 0
suma_calificaciones = 0

# Se inicia while 
while alumnos < cantidad_alumnos:
    alumnos = alumnos + 1
    print()
    print("Alumno", alumnos)

    calificacion = float(input("Ingrese la calificación: "))
    
    # Se limita la nota entre 0 a 10 para prevenir que ingresen mal.
    if calificacion < 0 :
        print("> ¡Vuelva a intentantarlo! La nota debe ser de 0 a 10.")
        print()
        alumnos = alumnos - 1 
    elif calificacion > 10 :
        print("> ¡vuelva a intentantarlo! La nota debe ser de 0 a 10.")
        alumnos = alumnos - 1 
    else:
        suma_calificaciones = suma_calificaciones + calificacion

        promedio = suma_calificaciones / cantidad_alumnos

print()
print("el promedio de la clase es de:" , promedio)
