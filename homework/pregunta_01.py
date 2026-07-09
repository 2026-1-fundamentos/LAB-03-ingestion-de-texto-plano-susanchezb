"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel

import pandas as pd

def pregunta_01():
    """
    Construya y retorne un dataframe de Pandas a partir del archivo
    'files/input/clusters_report.txt'. Los requierimientos son los siguientes:

    - El dataframe tiene la misma estructura que el archivo original.
    - Los nombres de las columnas deben ser en minusculas, reemplazando los
      espacios por guiones bajos.
    - Las palabras clave deben estar separadas por coma y con un solo
      espacio entre palabra y palabra.


    """
  

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lineas = file.readlines()

    data = []
    cluster = 0
    cantidad_palabras = 0
    porcentaje_palabras = 0
    palabras_clave = " "

    for linea in lineas[4:]:
        limpiar_linea = linea.strip().split()

        if len(limpiar_linea) > 0:
            if limpiar_linea[0].isdigit():
                
                cluster = int(limpiar_linea[0])
                cantidad_palabras = int(limpiar_linea[1])
                porcentaje_palabras = float(limpiar_linea[2].replace(",", "."))
                palabras_clave = palabras_clave.join(limpiar_linea[4:])

            else:
                palabras_clave += " " + " ".join(limpiar_linea).strip(".")
        else:
            data.append({"cluster": cluster, "cantidad_de_palabras_clave": cantidad_palabras, "porcentaje_de_palabras_clave" : porcentaje_palabras, "principales_palabras_clave" : palabras_clave})
            palabras_clave = " "

    df1 = pd.DataFrame(data, columns = ["cluster", "cantidad_de_palabras_clave", "porcentaje_de_palabras_clave", "principales_palabras_clave"])

    return df1