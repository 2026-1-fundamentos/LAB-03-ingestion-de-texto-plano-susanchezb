"""
Escriba el codigo que ejecute la accion solicitada en cada pregunta.
"""

# pylint: disable=import-outside-toplevel


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
    import pandas as pd

def pregunta_01():

    with open("files/input/clusters_report.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()

    data = []

    cluster = None
    cantidad = None
    porcentaje = None
    palabras_clave = []

    for linea in lines[4:]:

        linea = linea.strip()

        # Si la línea está vacía, terminó un cluster
        if linea == "":

            if cluster is not None:

                data.append({
                    "cluster": cluster,
                    "cantidad_de_palabras_clave": cantidad,
                    "porcentaje_de_palabras_clave": porcentaje,
                    "principales_palabras_clave": " ".join(palabras_clave).replace(" ,", ",").replace(" .", ".")
                })

            palabras_clave = []

        else:

            partes = linea.split()

            # Si comienza con un número, empieza un nuevo cluster
            if partes[0].isdigit():

                cluster = int(partes[0])
                cantidad = int(partes[1])
                porcentaje = float(partes[2].replace(",", "."))

                texto = " ".join(partes[4:])
                palabras_clave.append(texto)

            else:

                palabras_clave.append(" ".join(partes))

    # Guardar el último cluster
    if cluster is not None:

        data.append({
            "cluster": cluster,
            "cantidad_de_palabras_clave": cantidad,
            "porcentaje_de_palabras_clave": porcentaje,
            "principales_palabras_clave": " ".join(palabras_clave).replace(" ,", ",").replace(" .", ".")
        })

    return pd.DataFrame(data)
