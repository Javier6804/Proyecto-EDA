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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import listiterator as it
assert config
import operator

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria
"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------
def newCatalog():
    catalogo={
        "viajes":None,
        "viajesId":None,
        "taxisIds":None,
        "companias":None
    } 
    catalogo['viajes'] = lt.newList('SINGLE_LINKED', compareviajesByName)
    catalogo["viajesIds"]=mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareviajesIds)
    catalogo["taxisIds"]=mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareviajesIds)                               
    catalogo["companias"]=mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareviajesIds)
    
    
    return catalogo




def newCompany(name):
    genre = {'name': "", "taxis": None, "num_taxis": None, "viajes": 0}
    genre['name'] = name
    genre['taxis'] = mp.newMap(200,
                                   maptype='CHAINING',
                                   loadfactor=0.4,
                                   comparefunction=compareviajesIds)
    
    return genre

# Funciones para agregar informacion al catalogo
def addviaje(catalog, viaje):
    lt.addLast(catalog['viajes'], viaje)
    mp.put(catalog['viajesIds'], viaje['trip_id'], viaje)

def addTaxi(catalog, viaje):
    mp.put(catalog['taxisIds'], viaje['taxi_id'], None)

def addCompania(catalog, viaje, d_1, d_2):
    companias = catalog['companias']
    existgenre = mp.contains(companias, viaje["company"])
    if existgenre:
        entry = mp.get(companias, viaje["company"])
        dicc = me.getValue(entry)
        

    else:
        dicc = newCompany(viaje["company"])
        mp.put(companias, viaje["company"], dicc)
        
    mp.put(dicc["taxis"], viaje["taxi_id"], None)
    dicc["num_taxis"]=mp.size(dicc["taxis"])
    dicc["viajes"]+=1
    if viaje["company"]=="":
        viaje["company"]="Independent Owner"
    d_1[viaje["company"]]= dicc["num_taxis"]
    d_2[viaje["company"]]= dicc["viajes"]



def Punto5(companias):
    return sorted(companias.items(), key=operator.itemgetter(1), reverse=True)
            
    
def Punto6(companias):
    return sorted(companias.items(), key=operator.itemgetter(1), reverse=True)
            
    

# ==============================
# Funciones de consulta
# ==============================

def getviajesbyGenre(catalog, genero):
    genre = mp.get(catalog['generos'], genero)
    if genre:
        return me.getValue(genre)
    return None

def detailsSize(catalog):
    return lt.size(catalog['viajes'])

def detailsSizeTaxis(catalog):
    return mp.size(catalog['taxisIds'])
    
def detailsSizeCompanias(catalog):
    return mp.size(catalog['companias'])
# ==============================
# Funciones de Comparacion
# ==============================
def compareviajesIds(id, entry):
    identry = me.getKey(entry)
    if (id == identry):
        return 0
    elif (id > identry):
        return 1
    else:
        return -1


def compareviajesByName(keyname, viaje):
    
    authentry = me.getKey(viaje)
    if (keyname == authentry):
        return 0
    elif (keyname > authentry):
        return 1
    else:
        return -1


