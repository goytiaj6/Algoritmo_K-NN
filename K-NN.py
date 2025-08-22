### Algoritmo K-NN ###

### Importamos las bibliotecas necesarias
import pandas as pd

# Leemos los datos del dataset base
df = pd.read_excel("animals.xlsx", engine="openpyxl") # type: ignore

# Mostrar las primeras y útimas filas
# print(df)

atributos = df.iloc[:, :-1].values.tolist()
clases = df.iloc[:, -1].tolist()

# Leemos los datos a clasificar
df_nuevo = pd.read_excel("animals_clasificar.xlsx") # type: ignore
atributos_nuevo = df_nuevo.values.tolist()

# Mostrar las primeras y útimas filas
# print(df_nuevo)

### FIN DEL PROGRAMA ###