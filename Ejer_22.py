from lista import Lista

class Jedi:

    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"'Jedi': {self.nombre} , 'especie': {self.especie} , 'maestro': {self.maestro} , 'sable de luz': {self.sable_luz}"


lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('jedis.txt')
lineas = file.readlines()

lista = []

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';')
    datos.pop(-1)
    # print(datos[4].split('/'))
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),
                        campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         campo='especie')
    lista.append(Jedi(datos[0],
                      datos[2],
                      datos[3].split('/'),
                      datos[4].split('/')))
# !
print('a. listado ordenado por nombre y por especie')
print('Lista por nombre')
lista_jedi.barrido()
print('Fin barrido')

print()
print('Lista por especie')
lista_jedi2.barrido()
print('Fin barrido')

print()
print('b. mostrar toda la información de Ahsoka Tano y Kit Fisto')
def mostrar_x_jedi(lista, nombre_jedi):
    nodo_jedi = lista.busqueda(nombre_jedi, 'nombre')
    if nodo_jedi:
        print('el Jedi',nombre_jedi,'esta en la lista y su informacion es:')
        #print(f'el Jedi {nodo_jedi.info}')
        print(' ',nodo_jedi.info)
    else:
        print('el Jedi',nombre_jedi,'no esta en la lista')

mostrar_x_jedi(lista_jedi, 'Ahsoka Tano')
mostrar_x_jedi(lista_jedi, 'kit fisto')


print()
print('c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices')
def mostrar_todos_los_padawan_de_x_jedi(lista, nombre_jedi):
    cant_jedis = lista.tamanio()
    print('Los padawan de',nombre_jedi,'son:')
    for i in range(cant_jedis):
        nodo_jedi = lista.obtener_nodo(i)

        if(nombre_jedi in nodo_jedi.info.maestro):
            print(nodo_jedi.info)

mostrar_todos_los_padawan_de_x_jedi(lista_jedi, 'yoda')
print()
mostrar_todos_los_padawan_de_x_jedi(lista_jedi, 'luke skywalker')


print()
print("d. mostrar los Jedi de especie humana y twi'lek")
def mostrar_los_jedis_de_x_especie(lista, especie):
    cant_jedis = lista.tamanio()
    print('Los jedis de la especie',especie,'son:')
    for i in range(cant_jedis):
        nodo_jedi = lista.obtener_nodo(i)

        if(nodo_jedi.info.especie == especie):
            print(nodo_jedi.info)

mostrar_los_jedis_de_x_especie(lista_jedi, 'human')
print()
mostrar_los_jedis_de_x_especie(lista_jedi, "twi'lek")

print()
print('e. listar todos los Jedis que comienzan con A')
def mostrar_los_jedis_que_comienzan_con_x_letra(lista, letra):
    cant_jedis = lista.tamanio()
    print(f"Los jedis que comienzan con la letra '{letra.upper()}' son:")
    for i in range(cant_jedis):
        nodo_jedi = lista.obtener_nodo(i)
        
        if(nodo_jedi.info.nombre[0].upper() == letra.upper()):
            print(nodo_jedi.info)

mostrar_los_jedis_que_comienzan_con_x_letra(lista_jedi, "A")

print()
print('f. mostrar los Jedi que usaron sable de luz de mas de un color')
def mostrar_los_jedis_que_usaron_sable_de_luz_de_mas_de_x_color(lista, num_color):
    cant_jedis = lista.tamanio()
    print('Los jedis que usaron sable de luz de mas de',num_color,'color/es son:')
    for i in range(cant_jedis):
        nodo_jedi = lista.obtener_nodo(i)
        
        if len(nodo_jedi.info.sable_luz) > num_color:
            print(nodo_jedi.info.sable_luz)

mostrar_los_jedis_que_usaron_sable_de_luz_de_mas_de_x_color(lista_jedi, 1)

print()
print('g. indicar los Jedi que utilizaron sable de luz amarillo o violeta')
def mostrar_los_jedis_que_usaron_sable_de_luz_de_x_color(lista, color):
    cant_jedis = lista.tamanio()
    print('Los jedis que usaron sable de luz de color',color,'son:')
    for i in range(cant_jedis):
        nodo_jedi = lista.obtener_nodo(i)
        
        if color in nodo_jedi.info.sable_luz:
            print(nodo_jedi.info)

mostrar_los_jedis_que_usaron_sable_de_luz_de_x_color(lista_jedi, 'yellow')
print()
mostrar_los_jedis_que_usaron_sable_de_luz_de_x_color(lista_jedi, 'purple')

print()
print('h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron')
def mostrar_los_nombres_de_todos_los_padawan_de_x_jedi(lista, nombre_jedi):
    cant_jedis = lista.tamanio()
    print('Los padawan de',nombre_jedi,'son:')
    for i in range(cant_jedis):
        nodo_jedi = lista.obtener_nodo(i)

        if(nombre_jedi in nodo_jedi.info.maestro):
            print(nodo_jedi.info.nombre)

mostrar_los_nombres_de_todos_los_padawan_de_x_jedi(lista_jedi, 'qui-gon jin')
print()
mostrar_los_nombres_de_todos_los_padawan_de_x_jedi(lista_jedi, 'mace windu')