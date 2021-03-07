global1 = 34

def cambiar_global(val):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    global global1
    global1=val
    pass


def anio_bisiesto(year):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    es_bisiesto=lambda year: False if not year % 4 == 0 else (True if not year % 100 == 0 else (False if not year % 400 == 0 else True))
    return es_bisiesto(year)

    pass

def contar_valles(l):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    nvalle=0
    for a in l:
      if a==0:
        nvalle+=1
    return nvalle
    pass

def saltando_rocas():
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    pass

def pares_medias():
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    pass

# Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'

class ListaComa:
    def __init__(self,l1):
      self.l1=l1
        

    def __str__(self):
      cadena=''
      for i in self.l1:
        if self.l1[len(self.l1)-1]==i:
          cadena+=str(i)
        else:
          cadena+=str(i)+","
      return cadena


# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'

class Persona:
    def __init__(self,nombres,apellidos):
        self.nombres=nombres
        self.apellidos=apellidos

    def nombre_completo(self):
      cadena=''
      cad_nom=''
      cad_ape=''
      for i in self.nombres:
        if self.nombres[len(self.nombres)-1]==i:
          cad_nom+=str(i).capitalize()
        else:
          cad_nom+=str(i).capitalize()+" "
      for i in self.apellidos:
        if self.apellidos[len(self.apellidos)-1]==i:
          cad_ape+=str(i).capitalize()
        else:
          cad_ape+=str(i).capitalize()+" "
      cadena=cad_nom+' '+cad_ape
      return cadena




# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35.
from datetime import date
class Persona1(Persona):
  def __init__(self, nombres, apellidos, fecha_nacimiento):
    Persona.__init__(self, nombres, apellidos)
    self.fecha_nacimiento = fecha_nacimiento

  def edad(self):
    hoy=date.today()
    return (hoy.year - self.fecha_nacimiento.year) - (1 if hoy < date(hoy.year,self.fecha_nacimiento.month, self.fecha_nacimiento.day) else 0)