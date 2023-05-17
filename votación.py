import tkinter as tk

# Función para registrar un voto
def registrar_voto(voto):
    global voto1, voto2, voto3, voto4, voto5

    # Incrementar el contador correspondiente según el voto ingresado
    if voto == 1:
        voto1 += 1
    elif voto == 2:
        voto2 += 1
    elif voto == 3:
        voto3 += 1
    elif voto == 4:
        voto4 += 1
    elif voto == 5:
        voto5 += 1

    # Actualizar la etiqueta de resultados
    actualizar_resultados()

# Función para actualizar la etiqueta de resultados
def actualizar_resultados():
    global voto1, voto2, voto3, voto4, voto5, total_de_votos, resultados_label

    # Calcular el total de votos
    total_de_votos = voto1 + voto2 + voto3 + voto4 + voto5

    # Crear una lista de candidatos para iterar sobre ella
    candidatos = [voto1, voto2, voto3, voto4, voto5]

    # Actualizar la etiqueta de resultados con los datos actualizados
    resultados_text = "Resultados:\n\n"
    contador = 0
    for i in candidatos:
        contador += 1
        porcentaje = int((i / total_de_votos) * 100)
        resultados_text += f"Candidato {contador}: {i} votos ({porcentaje}%)\n"
    resultados_text += f"\nTotal de votos: {total_de_votos}"
    resultados_label.config(text=resultados_text)

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Contador de Votos")
ventana.geometry("300x400")

# Variables para almacenar los votos
voto1 = 0
voto2 = 0
voto3 = 0
voto4 = 0
voto5 = 0
total_de_votos = 0

# Etiqueta de instrucciones
instrucciones_label = tk.Label(ventana, text="Seleccione el número del candidato al que desea votar:")
instrucciones_label.pack(pady=10)

# Funciones para registrar los votos
def votar_candidato1():
    registrar_voto(1)

def votar_candidato2():
    registrar_voto(2)

def votar_candidato3():
    registrar_voto(3)

def votar_candidato4():
    registrar_voto(4)

def votar_candidato5():
    registrar_voto(5)

# Botones de votación
boton_candidato1 = tk.Button(ventana, text="Candidato 1", command=votar_candidato1)
boton_candidato1.pack()

boton_candidato2 = tk.Button(ventana, text="Candidato 2", command=votar_candidato2)
boton_candidato2.pack()

boton_candidato3 = tk.Button(ventana, text="Candidato 3", command=votar_candidato3)
boton_candidato3.pack()

boton_candidato4 = tk.Button(ventana, text="Candidato 4", command=votar_candidato4)
boton_candidato4.pack()

boton_candidato5 = tk.Button(ventana, text="Candidato 5", command=votar_candidato5)
boton_candidato5.pack()

# Etiqueta de resultados
resultados_label = tk.Label(ventana, text="Resultados:")
resultados_label.pack(pady=20)

# Ejecutar la interfaz de usuario
ventana.mainloop()
