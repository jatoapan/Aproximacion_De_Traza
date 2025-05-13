import os
import math as mt
import customtkinter as ctkt
from PIL import Image
import sys

if getattr(sys, 'frozen', False):
    directory = os.path.dirname(sys.executable)
else:
    directory = os.path.dirname(__file__)

images_path = os.path.join(directory, '../images')
traza_path = os.path.join(images_path, 'traza.png')
area_path = os.path.join(images_path, 'area.png')

def calculoDeLongitudArco(a, n, resultado):
    resultado.delete(0, 'end')
    radio = a.get().strip()
    validador1 = False
    intervalos = n.get().strip()
    validador2 = False

    if radio.count('.') == 0 or radio.count('.') == 1:
        radioCopy = radio.replace('.', '')
        if radioCopy.isdigit() and radioCopy != '0':
            radio = float(radio)
            validador1 = True

    if intervalos.isdigit() and intervalos != '0':
        validador2 = True
        intervalos = int(intervalos)

    if validador1 and validador2:
        i = 1
        sumatoria = 0
        while i <= intervalos:
            funcionSumando = mt.sqrt(5 - mt.sin(((4 * mt.pi) / intervalos) * i))
            sumatoria += funcionSumando
            i += 1
        longitudDeArco = ((radio * mt.pi) / intervalos) * sumatoria
        msj = f'Longitud de Arco: {round(longitudDeArco, 6)} (cm)'
    else:
        msj = 'Ingreso Inválido'
    
    a.delete(0, 'end')
    n.delete(0, 'end')
    resultado.insert(0, msj)

def funcionBoton():
    ventana.destroy()

    nuevaVentana = ctkt.CTk()
    nuevaVentana.title('AproximaciónDeTraza')
    nuevaVentana.after(0, lambda: nuevaVentana.state('zoomed'))

    imagen1 = ctkt.CTkImage(Image.open(traza_path), size=(ancho1 * 0.66, alto1))
    etiqueta1 = ctkt.CTkLabel(master=nuevaVentana, image=imagen1, text='')
    etiqueta1.pack(side='right')

    frame1 = ctkt.CTkFrame(master=nuevaVentana, width=int(ancho1 * 0.33), height=alto1, fg_color='orange')
    frame1.pack(side='left', fill='both', expand=True)

    frame2 = ctkt.CTkFrame(master=frame1, width=400, height=110, fg_color='white')
    frame2.place(x=90, y=100)

    etiqueta2 = ctkt.CTkLabel(master=frame2, text='Parámetros', font=('Torus Notched Bold', 40), text_color='orange')
    etiqueta2.place(x=90, y=25)
    
    etiqueta3 = ctkt.CTkLabel(master=frame1, text="Ingrese el valor del radio 'a' (cm):", font=('Torus Notched Bold', 20), text_color='white')
    etiqueta3.place(x=140, y=275)

    entrada1 = ctkt.CTkEntry(master=frame1, width=400, height=50, fg_color='white', text_color='black', font=('Torus Notched Bold', 20), justify='center')
    entrada1.place(x=90, y=375)

    etiqueta4 = ctkt.CTkLabel(master=frame1, text="Ingrese la cantidad de sub-intervalos:", font=('Torus Notched Bold', 20), text_color='white')
    etiqueta4.place(x=120, y=475)

    entrada2 = ctkt.CTkEntry(master=frame1, width=400, height=50, fg_color='white', text_color='black', font=('Torus Notched Bold', 20), justify='center')
    entrada2.place(x=90, y=575)

    entrada3 = ctkt.CTkEntry(master=frame1, width=400, height=50, fg_color='white', text_color='black', font=('Torus Notched Bold', 20), placeholder_text_color='black', justify='center')
    entrada3.place(x=90, y=875)

    boton1 = ctkt.CTkButton(master=frame1, width=400, height=110, text='Ingresar Datos', text_color='white', font=('Torus Notched Bold', 30), fg_color='red', border_color='red', hover_color='lightyellow', command=lambda: calculoDeLongitudArco(entrada1, entrada2, entrada3))
    boton1.place(x=90, y=700)

    nuevaVentana.mainloop()

ventana = ctkt.CTk()
ventana.title('AproximaciónDeTraza')
ventana.after(0, lambda: ventana.state('zoomed'))
ctkt.set_appearance_mode('white')

ancho1 = ventana.winfo_screenwidth()
alto1 = ventana.winfo_screenheight()

imagen1 = ctkt.CTkImage(Image.open(traza_path), size=(ancho1 * 0.66, alto1))
etiqueta1 = ctkt.CTkLabel(master=ventana, image=imagen1, text='')
etiqueta1.pack(side='left')

frame1 = ctkt.CTkFrame(master=ventana, width=ancho1 * 0.33, height=alto1, fg_color='orange')
frame1.pack(side='right', fill='both', expand=True)

frame2 = ctkt.CTkFrame(master=frame1, width=400, height=110, fg_color='white')
frame2.place(x=90, y=100)

etiqueta2 = ctkt.CTkLabel(master=frame2, text='Bienvenido', font=('Torus Notched Bold', 40), text_color='orange')
etiqueta2.place(x=100, y=25)

etiqueta3 = ctkt.CTkLabel(master=frame1, text='El objetivo de este programa es aproximar', font=('Torus Notched Bold', 20), text_color='white')
etiqueta3.place(x=90, y=300)
etiqueta4 = ctkt.CTkLabel(master=frame1, text='la longitud de la traza entre el cilindro', font=('Torus Notched Bold', 20), text_color='white')
etiqueta4.place(x=110, y=350)
etiqueta5 = ctkt.CTkLabel(master=frame1, text='x^2 + y^2 = a^2, a > 0, y el plano x + y + 2z = 8', font=('Torus Notched Bold', 20), text_color='white')
etiqueta5.place(x=80, y=400)
etiqueta6 = ctkt.CTkLabel(master=frame1, text='mediante una Suma de Riemman', font=('Torus Notched Bold', 20), text_color='white')
etiqueta6.place(x=140, y=450)

imagen2 = ctkt.CTkImage(Image.open(area_path), size=(400, 175))
etiqueta7 = ctkt.CTkLabel(master=frame1, image=imagen2, text='')
etiqueta7.place(x=90, y=550)

boton1 = ctkt.CTkButton(master=frame1, width=400, height=110, text='Empezar', text_color='white', font=('Torus Notched Bold', 30), fg_color='red', border_color='red', hover_color='lightyellow', command=funcionBoton)
boton1.place(x=90, y=800)

ventana.mainloop()

# Programado por: José Andrés Toapanta Domínguez