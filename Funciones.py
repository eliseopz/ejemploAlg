import Estructura

listEst = []
notas = []

def agregarEstudiante(id, nom, ape, car, notas):
    est = Estructura.Estudiante(id, nom, ape, car, notas)
    listEst.append(est)

def agregarAsig(mat, calif): 
    nota = Estructura.Nota(mat, calif)
    notas.append(nota)

def calcPromedio(notas):
    suma = 0
    for nota in notas:
        suma += nota.Calificacion
    promedio = suma / len(notas)
    return promedio

def calcPrimerosLugares():
    i = 0
    while i< len(listEst):
        j = i+1
        while j< len(listEst):
            est1 = listEst[i]
            est2 = listEst[j]
            prom1 = calcPromedio(est1.Notas)
            prom2 = calcPromedio(est2.Notas)
            if(prom2 > prom1):
                aux = listEst[i]
                listEst[i] = listEst[j]
                listEst[j] = aux
            j+=1
        i+=1
    return listEst[0], listEst[1], listEst[2]


