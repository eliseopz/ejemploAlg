import Funciones as fun

fun.agregarAsig("Español", 20)
fun.agregarAsig("Matemáticas", 90)

fun.agregarEstudiante(1, "Juan", "Lopez", "ISI", fun.notas)

for est in fun.listEst:
    print(est.Nombres)
    print(est.Apellidos)
    print(est.Carrera)
    for nota in est.Notas:
        print(nota.Materia)
        print(nota.Calificacion)