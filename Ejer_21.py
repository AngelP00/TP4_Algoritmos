'''
21. Se cuenta con una lista de películas de cada una de estas se dispone de los siguientes datos:
nombre, valoración del público –es un valor comprendido entre 0-10–, año de estreno y recaudación.
Desarrolle los algoritmos necesarios para realizar las siguientes tareas:
'''
from lista import Lista
from random import randint, choice

class Pelicula:
    lista_poquemones = Lista()
    def __init__(self, nombre, valoracion, anio_de_estreno, recaudacion):
        self.nombre = nombre
        self.valoracion = valoracion
        self.anio_de_estreno = anio_de_estreno
        self.recaudacion = recaudacion
    
    def __str__(self):
        #return self.nombre
        return f'Pelicula: {self.nombre} , valoracion: {self.valoracion} , anio de estreno: {self.anio_de_estreno} , recaudacion: {self.recaudacion}'


lista_peliculas = Lista()

peliculas = [
    {'name': 'Terminator 1', 'valoracion': 9.5, 'anio de estreno': 1991,  'recaudacion': 40000000},
    {'name': 'Madagascar 3', 'valoracion': 3, 'anio de estreno': 2002,  'recaudacion': 30000000},
    {'name': 'Spider Man 1', 'valoracion': 0, 'anio de estreno': 2003,  'recaudacion': 11000000},
    {'name': 'Thor 1', 'valoracion': 1, 'anio de estreno': 2007,  'recaudacion': 5000000},
    {'name': 'Zorro 1', 'valoracion': 9.5, 'anio de estreno': 2000, 'recaudacion': 4500000},
    {'name': 'Anaconda 1', 'valoracion': 6, 'anio de estreno': 2000, 'recaudacion': 3500000},
]


for pelicula in peliculas:
    lista_peliculas.insertar(Pelicula(pelicula['name'],
                                           pelicula['valoracion'],
                                           pelicula['anio de estreno'],
                                           pelicula['recaudacion']), 'nombre')

lista_peliculas.barrido()



print()
print('a. permitir filtrar las películas por año –es decir mostrar todas las películas de un determinado anio')
def mostrar_las_peliculas_de_x_anio(lista, anio):
    cant_peliculas = lista.tamanio()
    for i in range(cant_peliculas):
        pelicula = lista.obtener_nodo(i).info
        if pelicula.anio_de_estreno == anio:
            print(pelicula)

anio_de_las_peliculas = int(input('ingrese el anio de las peliculas que deseas consultar: '))
mostrar_las_peliculas_de_x_anio(lista_peliculas, anio_de_las_peliculas)

print()
print('b. mostrar los datos de la pelicula que mas recaudo')
def pelicula_que_mas_recaudo(lista):
    pelicula_mayor_recaudacion = Pelicula('', 0, 0, 0)

    cant_peliculas = lista.tamanio()
    for i in range(cant_peliculas):
        pelicula = lista.obtener_nodo(i).info
        if pelicula.recaudacion > pelicula_mayor_recaudacion.recaudacion:
            pelicula_mayor_recaudacion = pelicula

    return pelicula_mayor_recaudacion

print(pelicula_que_mas_recaudo(lista_peliculas))

print()
print('c. indicar las películas con mayor valoración del público, puede ser más de una')
def mostrar_las_peliculas_con_mayor_valoracion(lista):
    mayor_valoracion = 0
    peliculas_con_mayor_valoracion = Lista()

    cant_peliculas = lista.tamanio()
    for i in range(cant_peliculas):
        pelicula = lista.obtener_nodo(i).info
        if pelicula.valoracion > mayor_valoracion:
            mayor_valoracion = pelicula.valoracion
            peliculas_con_mayor_valoracion = Lista()
            peliculas_con_mayor_valoracion.insertar(pelicula,'nombre')
        elif pelicula.valoracion == mayor_valoracion:
            peliculas_con_mayor_valoracion.insertar(pelicula,'nombre')
    
    peliculas_con_mayor_valoracion.barrido()

mostrar_las_peliculas_con_mayor_valoracion(lista_peliculas)


print()
print('d. mostrar el contenido de la lista en los siguientes criterios de orden –solo podrá utilizar una lista auxiliar:')

def mostrar_las_peliculas_por_x_criterio(lista, criterio):
    lista_aux = Lista()

    cant_peliculas = lista.tamanio()
    for i in range(cant_peliculas):
        pelicula = lista.obtener_nodo(i).info
        lista_aux.insertar(pelicula, criterio)
    
    lista_aux.barrido()

print('I. por nombre')
mostrar_las_peliculas_por_x_criterio(lista_peliculas, 'nombre')

print()
print('II. por recaudacion')
mostrar_las_peliculas_por_x_criterio(lista_peliculas, 'recaudacion')

print()
print('III. por anio de estreno')
mostrar_las_peliculas_por_x_criterio(lista_peliculas, 'anio_de_estreno')

print()
print('IV. por valoración del publico')
mostrar_las_peliculas_por_x_criterio(lista_peliculas, 'valoracion')