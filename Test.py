#https://github.com/Armando-De-Santiago-Rodriguez/Participaci-n-3.git
import pandas as pd

#Importar el CSV para leerlo
datos = pd.read_csv('dataset.csv')

#Definir algoritmo para sustituir la letra en la pisicion deseada
def algoritmo_modificar(Posicion, Referencia, Alteracion, Cadena):
    Lista_Lista_regresar = []  # Lista para almacenar las cadenas modificadas
    cadena_actual = list(Cadena)  
    x = 0
    y = 9
    while len(cadena_actual) >= y:
        Cadena_G = cadena_actual.copy()  # Copia de la cadena actual para cada iteración
        Lista_L = []
        for j in range(x, y):
            if j in Posicion and Referencia[Posicion.index(j)] == Cadena_G[j]: 
                del Cadena_G[j]
                Cadena_G.insert(j, Alteracion[Posicion.index(j)])  # Usar la posición para obtener la alteración correspondiente
                Lista_L.append(j)  # Agregar la posición a la lista
                Lista_L.append(Alteracion[Posicion.index(j)])
        if Cadena_G != cadena_actual:
            Lista_L.insert(0,''.join(Cadena_G))  # Convertir la lista de caracteres en una cadena y agregarla a la lista
        x += 5
        y += 5
        if Lista_L:  # Verificar si la lista no está vacía antes de agregarla a Lista_Lista_regresar
            Lista_Lista_regresar.append(Lista_L)
    return Lista_Lista_regresar

# Asignar su respectiva variable a cada columna
Posicion = datos['posicion'].tolist()
Referencia = datos['referencia'].tolist()
Alteracion = datos['alteracion'].tolist()
String = datos['string_a_modificar']

# Variable unicamente para guardar la cadena que deso
String_2 = String[0]

# Llamar a la función algoritmo_modificar
Cadena_Guardada = algoritmo_modificar(Posicion, Referencia, Alteracion, String_2)

# Crear un DataFrame con las cadenas modificadas
df = pd.DataFrame({'Cadena_Modificada': Cadena_Guardada})

# Guardar el DataFrame en un archivo CSV
df.to_csv('cadenas_modificadas.csv', index=False)