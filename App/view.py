"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________
small= "taxi-trips-wrvz-psew-subset-small.csv"
medium="taxi-trips-wrvz-psew-subset-medium.csv"
large="taxi-trips-wrvz-psew-subset-large.csv"

# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________
d_1={}
d_2={}





# ___________________________________________________
#  Menu principal
# ___________________________________________________
def printMenu():
    print("Bienvenido")
    print("1- Inicializar Catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Número total de taxis en los servicios reportados")
    print("4- Número total de compañías que tienen al menos un taxi inscrito.")
    print("5- Top M de compañías ordenada por la cantidad de taxis afiliados.")
    print("6- Top N de compañías que más servicios prestaron,")
    print("0- Salir")


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        cont = controller.initCatalog()
    if int(inputs[0]) == 2:
        
        print("Elija el tamaño del archivo")
        print("1- Archivo Small")
        print("2- Archivo Medium")
        print("3- Archivo Large")
        tamano= input("Seleccione una opción para continuar\n")
        if int(tamano)==1:
            print("Cargando información de los archivos ....")
            controller.loadDetails(cont, small, d_1, d_2)
            print('Número de  viajes cargados: ' + str(controller.detailsSize(cont)))
        elif int(tamano)==2:
            print("Cargando información de los archivos ....")
            controller.loadDetails(cont, medium, d_1, d_2)
            print('Número de  viajes cargados: ' + str(controller.detailsSize(cont)))
        elif int(tamano)==3:
            print("Cargando información de los archivos ....")
            controller.loadDetails(cont, large, d_1, d_2)
            print('Número de  viajes cargados: ' + str(controller.detailsSize(cont)))
        
    if int(inputs[0]) == 3:
        print("El numero total de taxis en los servicios reportados es: " + str(controller.detailsSizeTaxis(cont)))
    if int(inputs[0]) == 4:
        print("El numero total de compañías que tienen al menos un taxi inscrito es: " + str(controller.detailsSizeCompanias(cont)))
    if int(inputs[0]) == 5:
        i=0
        companias=controller.Punto5(d_1)
        m = int(input("Ingrese el numero M top de compañias: "))
        while i!=m:
            print(str(i+1) + ". "+ str(companias[i][0]) + ": " + str(companias[i][1]))
            i+=1

    if int(inputs[0]) == 6:
        i=0
        companias=controller.Punto6(d_2)
        n = int(input("Ingrese el numero N top de compañias: "))
        while i!=n:
            print(str(i+1) + ". "+ str(companias[i][0]) + ": " + str(companias[i][1]))
            i+=1
    if int(inputs[0]) == 0:
        sys.exit(0)
sys.exit(0)
