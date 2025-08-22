### Algoritmo K-NN ###

### Importamos las bibliotecas necesarias
import pandas as pd
import Animal_Class

# Leemos los datos del dataset base
df_base = pd.read_excel("animals.xlsx", engine="openpyxl") # type: ignore
# Creamos la lista de animales
"""
# Esta es la forma larga
lista_animals = [Animal_Class.Animal(row["nombre_animal"], row["pelo"], row["plumas"], row["tomaLeche"], row["esqueleto"],
                                     row["acuático"], row["predador"], row["dientes"], row["columnaVertebral"],
                                     row["respira"], row["venenoso"], row["piernas"], row["cola"], row["domestico"],
                                     row["tamañoMedio"],) for index, row in df.iterrows()]
"""
# Creación de la lista de forma dinámica
lista_animals = [Animal_Class.Animal(**row.to_dict()) for index, row in df_base.iterrows()] # type: ignore
# print(lista_animals)
# Leemos los datos a clasificar
df_nuevo: pd.DataFrame = pd.read_excel("animals_clasificar.xlsx") # type: ignore
# Dado que tenemos la columna de clase vacia, aparecera NaN
# Definimos que el no tener clase aparezca 0 en lugar de NaN
df_nuevo["clase"] = df_nuevo["clase"].fillna(0).astype(int) # type: ignore
# Generamos nuestra lista de animales sin clasificar
lista_animals_clasificar = [Animal_Class.Animal(**row.to_dict()) for index, row in df_nuevo.iterrows()] # type: ignore
print(lista_animals_clasificar)

### FIN DEL PROGRAMA ###