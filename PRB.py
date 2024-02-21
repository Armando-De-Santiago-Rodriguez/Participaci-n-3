import tkinter as tk
from tkinter import filedialog
import pandas as pd

# Definir algoritmo para sustituir la letra en la posición deseada
def algoritmo_modificar(Posicion, Referencia, Alteracion, Cadena):
    Lista_Lista_regresar = []  # Lista para almacenar las cadenas modificadas
    Lista_Lista_regresar.append(Cadena)
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
                Lista_L.append(Alteracion[Posicion.index(j)])  # Agregar la Alteración que se realizó a la lista
        if Cadena_G != cadena_actual:
            Lista_L.insert(0, ''.join(Cadena_G))  # Convertir la lista de caracteres en una cadena y agregarla a la lista
        x += 5
        y += 5
        if Lista_L:  # Verificar si la lista no está vacía antes de agregarla a Lista_Lista_regresar
            Lista_Lista_regresar.append(Lista_L)
    return Lista_Lista_regresar

def procesar_archivo_csv(ruta_archivo, texto_resultado):
    # Leer el archivo CSV
    datos = pd.read_csv(ruta_archivo)

    # Asignar su respectiva variable a cada columna
    Posicion = datos['posicion'].tolist()
    Referencia = datos['referencia'].tolist()
    Alteracion = datos['alteracion'].tolist()
    String = datos['string_a_modificar']

    # Variable únicamente para guardar la cadena que deseo
    String_2 = String[0]

    # Llamar a la función algoritmo_modificar
    Cadena_Guardada = algoritmo_modificar(Posicion, Referencia, Alteracion, String_2)

    # Crear un DataFrame con las cadenas modificadas
    df = pd.DataFrame({'Cadena_Modificada': Cadena_Guardada})

    # Guardar el DataFrame en un archivo CSV
    df.to_csv('cadenas_modificadas.csv', index=False)

    # Leer el archivo resultante y mostrar su contenido en la interfaz gráfica
    with open('cadenas_modificadas.csv', 'r') as archivo:
        contenido = archivo.readlines()
        texto_resultado.config(state=tk.NORMAL)
        texto_resultado.delete('1.0', tk.END)
        for i, linea in enumerate(contenido[1:], start=1):  # Omitir la primera línea (encabezado del DataFrame)
            texto_resultado.insert(tk.END, f"{i}. {linea}")
        texto_resultado.config(state=tk.DISABLED)

def fusionar_cadenas(cadena1_idx, cadena2_idx, texto_resultado, resultado_label):
    idx1 = int(cadena1_idx) - 1
    idx2 = int(cadena2_idx) - 1
    with open('cadenas_modificadas.csv', 'r') as archivo:
        contenido = archivo.readlines()
        cadena1 = contenido[idx1 + 1].strip()
        cadena2 = contenido[idx2 + 1].strip()
        original = contenido[1].strip()  

    mod1 = cadena1.split(',')[0::2]
    mod2 = cadena2.split(',')[0::2]

    cadena1_original = cadena1.split(',')[0]
    cadena2_original = cadena2.split(',')[0]
    Original_Original = original.split(',')[0]

    mod_fusionadas = list(Original_Original)

    for l in range(len(Original_Original)):
        if Original_Original[l] != cadena1_original[l]:
            mod_fusionadas[l] = cadena1_original[l]
        elif Original_Original[l] != cadena2_original[l]:
            mod_fusionadas[l] = cadena2_original[l]

    cadena_fusionada = ''.join(mod_fusionadas)

    resultado = f"Cadena fusionada: {cadena_fusionada}"

    resultado_label.config(text=resultado)


def seleccionar_archivo(texto_resultado):
    ruta_archivo = filedialog.askopenfilename(title="Seleccionar archivo CSV")
    if ruta_archivo:
        procesar_archivo_csv(ruta_archivo, texto_resultado)

def main():
    # Crear la ventana principal
    ventana = tk.Tk()
    ventana.title("Edicion de cadenas de caracteres")
    ventana.geometry("800x600")

    etiqueta = tk.Label(ventana, text="¡¡¡¡¡Bienvenido!!!!!!", bg="blue")
    etiqueta.pack(fill=tk.X)  # Ajustar el padding (espaciado)

    boton1 = tk.Button(ventana, text="Seleccionar archivo CSV", command=lambda: seleccionar_archivo(texto_resultado))
    boton1.pack(pady=10)

    texto_resultado = tk.Text(ventana, wrap=tk.WORD, height=20, width=80)
    texto_resultado.pack(pady=10)

    etiqueta_fusion = tk.Label(ventana, text="Fusionar Cadenas", bg="yellow")
    etiqueta_fusion.pack(fill=tk.X)  # Ajustar el padding (espaciado)

    frame_fusion = tk.Frame(ventana)
    frame_fusion.pack(pady=10)

    etiqueta_cadena1 = tk.Label(frame_fusion, text="Índice de la cadena 1:")
    etiqueta_cadena1.grid(row=0, column=0)

    entrada_cadena1 = tk.Entry(frame_fusion)
    entrada_cadena1.grid(row=0, column=1)

    etiqueta_cadena2 = tk.Label(frame_fusion, text="Índice de la cadena 2:")
    etiqueta_cadena2.grid(row=1, column=0)

    entrada_cadena2 = tk.Entry(frame_fusion)
    entrada_cadena2.grid(row=1, column=1)

    boton_fusion = tk.Button(frame_fusion, text="Fusionar", command=lambda: fusionar_cadenas(entrada_cadena1.get(), entrada_cadena2.get(), texto_resultado, resultado_label))
    boton_fusion.grid(row=2, column=0, columnspan=2, pady=10)

    frame_resultado = tk.Frame(ventana, bd=2, relief=tk.GROOVE)
    frame_resultado.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

    resultado_label = tk.Label(frame_resultado, text="", wraplength=600)
    resultado_label.pack(pady=10)

    etiqueta = tk.Label(ventana, text="¡Adios mundo cruel!")
    etiqueta.pack(padx=20, pady=10)  # Ajustar el padding (espaciado)

    # Ejecutar el bucle principal de la ventana
    ventana.mainloop()

if __name__ == "__main__":
    main()
