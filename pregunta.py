"""
Limpieza de datos usando Pandas
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import pandas as pd

def cambio(x):
  fecha = x.split("/")
  if (len(fecha[0])>3):
    reemplazo = fecha[0]
    fecha[0] = fecha[2]
    fecha[2] = reemplazo
 

  reasignado = "/".join(fecha)

  return reasignado


def clean_data():

    df = pd.read_csv("solicitudes_credito.csv", sep=";")

    #
    # Inserte su código aquí
    #
    #Eliminar primera columna
    del df["Unnamed: 0"]

    #Descartar nulos
    df = df.dropna()

    #Estandarizar valores de las columnas a minúsculas y quitar guiones
    df["sexo"]= df["sexo"].str.lower()
    df["tipo_de_emprendimiento"]= df["tipo_de_emprendimiento"].str.lower()
    df["línea_credito"]= df["línea_credito"].str.lower().str.replace("-"," ").str.replace("_"," ")
    df["barrio"] = df["barrio"].str.lower().str.replace("-"," ").str.replace("_"," ")
    df["idea_negocio"]= df["idea_negocio"].str.lower().str.replace("-"," ").str.replace("_"," ")

    #Se elimina el signo pesos con espacio, las comas de como divisores y el .00
    df["monto_del_credito"]= df['monto_del_credito'].str.replace('\$[\s*]', '').str.replace(',', '').str.replace('\.00', '').astype(int)
    
    #Se estandariza la fecha 
    df['fecha_de_beneficio'] = df["fecha_de_beneficio"].apply(cambio)
    df["fecha_de_beneficio"] = pd.to_datetime(df["fecha_de_beneficio"],format="%d/%m/%Y")

    #Descartar duplicados
    df.drop_duplicates(inplace=True)
    return df
