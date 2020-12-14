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

import config as cf
from App import model
import csv
from time import process_time 

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta. Esta responsabilidad
recae sobre el controlador.
"""

# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def initCatalog():
    catalog = model.newCatalog()
    return catalog



# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadDetails(catalog, details, d_1, d_2):
    t1_start = process_time()
    details = cf.data_dir + details
    with open(details, encoding="utf-8-sig") as csvfile:
        reader = csv.DictReader(csvfile, delimiter=',')
        for row in reader:
            model.addviaje(catalog,row)
            model.addTaxi(catalog,row)
            model.addCompania(catalog,row, d_1, d_2)
            
                
                     
    t1_stop = process_time()
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
  
def Punto5(d_1):
    return model.Punto5(d_1)

def Punto6(d_2):
    return model.Punto6(d_2) 

def getviajesbyGenre(catalog, genrename):
    genreinfo = model.getviajesbyGenre(catalog, genrename)
    return genreinfo

def detailsSize(catalog):
    return model.detailsSize(catalog)

def detailsSizeTaxis(catalog):
    return model.detailsSizeTaxis(catalog)

def detailsSizeCompanias(catalog):
    return model.detailsSizeCompanias(catalog)