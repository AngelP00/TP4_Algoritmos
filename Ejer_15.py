from lista import Lista
from random import randint, choice

class Entrenador:
    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
        self.nombre = nombre
        self.torneos_ganados = torneos_ganados
        self.batallas_ganadas = batallas_ganadas
        self.batallas_perdidas = batallas_perdidas
    
    def __str__(self):
        #return self.nombre
        return f'Entrenador: {self.nombre} , torneos ganados: {self.torneos_ganados} , batallas ganadas: {self.batallas_ganadas} , batallas perdidas: {self.batallas_perdidas}'

class Pokemon:

    def __init__(self, nombre, nivel, tipo, subtipo):
        self.nombre = nombre
        self.nivel = nivel
        self.tipo = tipo
        self.subtipo = subtipo

    def __str__(self):
        return f"pokemon nombre: {self.nombre} - nivel: {self.nivel} - tipo: {self.tipo} - subtipo: {self.subtipo}"

lista_entrenadores = Lista()

enternadores = [
    {'name': 'uno', 'tg': 15, 'bg': 45,  'bp': 11},
    {'name': 'dos', 'tg': 3, 'bg': 12,  'bp': 35},
    {'name': 'tres', 'tg': 0, 'bg': 50,  'bp': 50},
    {'name': 'cuatro', 'tg': 1, 'bg': 10,  'bp': 1},
    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
]

pokemons = [
    {'name': 'pok1', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
    {'name': 'pok2', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
    {'name': 'pok3', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
    {'name': 'pok4', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
    {'name': 'pok5', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
    {'name': 'pok6', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
    {'name': 'Tyrantrum', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
    {'name': 'Terrakion', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
    {'name': 'Wingull', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},
]


for entrenador in enternadores:
    lista_entrenadores.insertar(Entrenador(entrenador['name'],
                                           entrenador['tg'],
                                           entrenador['bp'],
                                           entrenador['bg']), 'nombre')

for entrenador in enternadores:
    for i in range(randint(1, 5)):
        pokemon = choice(pokemons)
        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
        pos.sublista.insertar(Pokemon(pokemon['name'],
                                      pokemon['nivel'],
                                      pokemon['tipo'],
                                      pokemon['subtipo']), 'nombre')

lista_entrenadores.barrido_lista_lista()

print()   
print('a. obtener la cantidad de Pokémons de un determinado entrenador;')
#! punto a cantidad de pok de un entrenador

entrenador = input('ingrese nombre del entrenador: ')
nodo_entrenador = lista_entrenadores.busqueda(entrenador, 'nombre')
if(nodo_entrenador):
    print(f"el entrenador tiene {nodo_entrenador.sublista.tamanio()} pokemons")
else:
    print('el entrenador no esta en la lista')


print()
print('b. listar los entrenadores que hayan ganado más de tres torneos;')
def barrido_entrenador_mas_tres_torneos_ganados(lista):
        pos_entrenador = 0
        entrenador = lista.obtener_elemento(0)
        while(entrenador is not None):
            if(entrenador.torneos_ganados > 3):
                print(entrenador)
            pos_entrenador += 1
            entrenador = lista.obtener_elemento(pos_entrenador)

#! entrenadores con mas de tres torneos
barrido_entrenador_mas_tres_torneos_ganados(lista_entrenadores)


print()
print('c. Listar el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;')
#! c
nodo_mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
print('Entrenador con mas torneos ganados:',nodo_mayor.info.nombre,', su poquemon de mayor nivel es:', nodo_mayor.sublista.mayor_de_lista('nivel').info)


print()
print('d. mostrar todos los datos de un entrenador y sus Pokemos;')
#! d
nombre_entrenador = input('ingrese nombre del entrenador: ')
nodo_entrenador = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')
if(nodo_entrenador):
    print(f"el entrenador tiene: {nodo_entrenador.info}")
    print('sus pokemones son: ')
    nodo_entrenador.sublista.barrido()
else:
    print('el entrenador no esta en la lista')
print()

print('e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %')
def mostrar_los_entrenadores_cuyo_porcentaje_de_victorias_sea_mayor_a_x(lista, porcentaje):
    cant_entrenadores = lista.tamanio()
    for i in range(cant_entrenadores):
        nodo_entrenador = lista.obtener_nodo(i)

        total = nodo_entrenador.info.batallas_ganadas + nodo_entrenador.info.batallas_perdidas
        if (nodo_entrenador.info.batallas_ganadas / total) > (porcentaje/100):
            print(nodo_entrenador.info)

mostrar_los_entrenadores_cuyo_porcentaje_de_victorias_sea_mayor_a_x(lista_entrenadores, 79)

print()
print('f. mostrar los entrenadores que tengan Pokemons de tipo fuego y planta o agua/volador (tipo y subtipo);')
def mostrar_entrenadores_que_tienen_a_x_tipo_de_pokemon(lista, tipos):
    resultado = 0
    cant_entrenadores = lista.tamanio()
    for i in range(cant_entrenadores):
        nodo_entrenador = lista.obtener_nodo(i)

        cant_pokemones = nodo_entrenador.sublista.tamanio()
        for j in range(cant_pokemones):
            pokemon = nodo_entrenador.sublista.obtener_nodo(j).info
            if (pokemon.tipo in tipos) or (pokemon.subtipo in tipos):
                print('El entrenador',nodo_entrenador.info.nombre,'tiene por lo menos un pokemon de uno de los siguientes tipos: ', tipos)
                break

mostrar_entrenadores_que_tienen_a_x_tipo_de_pokemon(lista_entrenadores, ('fuego','planta','agua','volador'))

print()
print('g. el promedio de nivel de los Pokémons de un determinado entrenador')
def promedio_de_nivel_de_los_pokemones_de_x_entrenador(nodo_entrenador):
    acum = 0
    cant_pokemones = nodo_entrenador.sublista.tamanio()
    for i in range(cant_pokemones):
        pokemon = nodo_entrenador.sublista.obtener_elemento(i)
        acum+= pokemon.nivel

    return acum/cant_pokemones

nombre_entrenador = input('ingrese el nombre del entrenador: ')
nodo_entrenador = lista_entrenadores.busqueda(nombre_entrenador, 'nombre')
if(nodo_entrenador):
    print("Promedio de nivel de los pokemones del entrenador 'uno':",promedio_de_nivel_de_los_pokemones_de_x_entrenador(nodo_entrenador))
else:
    print('el entrenador no esta en la lista')


print()
print('h. determinar cuántos entrenadores tienen a un determinado Pokémon')
def cuantos_entrenadores_tienen_a_un_x_Pokemon(lista, nombre_pokemon):
    resultado = 0
    cant_entrenadores = lista.tamanio()
    for i in range(cant_entrenadores):
        nodo_entrenador = lista.obtener_nodo(i)
        
        pokemon = nodo_entrenador.sublista.busqueda(nombre_pokemon,'nombre')
        if(pokemon is not None):#el poquemon esta en la sublista
            resultado+=1

    return resultado

nombre_pokemon = input('ingrese el nombre del pokemon: ')
print(cuantos_entrenadores_tienen_a_un_x_Pokemon(lista_entrenadores,nombre_pokemon))

print()
print('i. mostrar los entrenadores que tienen Pokemones repetidos')
def mostrar_los_entrenadores_que_tienen_pokemones_repetidos(lista):
    se_repiten_pokemones = False
    cant_entrenadores = lista.tamanio()
    for i in range(cant_entrenadores):
        nodo_entrenador = lista.obtener_nodo(i)
        #print('entrenador:',nodo_entrenador.info.nombre)

        cant_pokemones = nodo_entrenador.sublista.tamanio()
        for j in range(cant_pokemones):
            pokemon = nodo_entrenador.sublista.obtener_nodo(j).info
            nodo_entrenador.sublista.eliminar(pokemon.nombre, 'nombre')#se elimina el pokemon
            pokemon_buscado = nodo_entrenador.sublista.busqueda(pokemon.nombre,'nombre')#se busca al pokemon
            if pokemon_buscado is not None:
                print('El entrenador',nodo_entrenador.info.nombre,'tiene pokemones repetidos')
                break
            nodo_entrenador.sublista.insertar(pokemon, 'nombre')#se velueve a insertar

mostrar_los_entrenadores_que_tienen_pokemones_repetidos(lista_entrenadores)

print()
print('j. determinar los entrenadores que tengan uno de los siguientes Pokémons: Tyrantrum, Terrakion o Wingull')
def mostrar_entrenadores_que_tienen_a_x_pokemon(lista, nombre_pokemones):
    resultado = 0
    cant_entrenadores = lista.tamanio()
    for i in range(cant_entrenadores):
        nodo_entrenador = lista.obtener_nodo(i)
        #print('entrenador:',)
        for nombre_pokemon in nombre_pokemones:
            pokemon = nodo_entrenador.sublista.busqueda(nombre_pokemon,'nombre')
            if(pokemon is not None):#el poquemon esta en la sublista
                print('El entrenador',nodo_entrenador.info.nombre,'tiene el pokemon', nombre_pokemon)

mostrar_entrenadores_que_tienen_a_x_pokemon(lista_entrenadores, ('Tyrantrum', 'Terrakion', 'Wingull'))

print()
print('k. determinar si un entrenador “X” tiene al Pokémon “Y”')
print(', tanto el nombre del entrenador como del Pokémon deben ser ingresados')
print('; además si el entrenador tiene al Pokémon se deberán mostrar los datos de ambos')

def determinar_si_un_entrenador_x_tiene_al_Pokémon_y(lista, nombre_entrenador, nombre_pokemon):
    nodo_entrenador = lista.busqueda(nombre_entrenador,'nombre')
    if(nodo_entrenador is not None):#el entrenador esta en la lista
        nodo_pokemon = nodo_entrenador.sublista.busqueda(nombre_pokemon,'nombre')
        if(nodo_pokemon is not None):#el poquemon esta en la sublista
            print('El entrenador',nombre_entrenador,'tiene el pokemon', nombre_pokemon)
            print(nodo_entrenador.info)
            print(nodo_pokemon.info)
        else:
            print('El entrenador',nombre_entrenador,'no tiene el pokemon', nombre_pokemon)
    else:
        print('El entrenador no se encuentra en la lista')

nombre_entrenador = input('ingrese el nombre del entrenador: ')
nombre_pokemon = input('ingrese el nombre del pokemon: ')
determinar_si_un_entrenador_x_tiene_al_Pokémon_y(lista_entrenadores,nombre_entrenador, nombre_pokemon)