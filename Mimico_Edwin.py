import time
import random
import os
import sys
from tkinter import Tk, Label, Entry, Button, Frame
from PIL import Image, ImageTk
import pygame

pygame.init()
pygame.mixer.init()

if hasattr(sys, '_MEIPASS'):
    ruta_base = sys._MEIPASS
else:
    ruta_base = os.path.dirname(os.path.abspath(__file__))

imagen = os.path.join(ruta_base, "Mimico Edwin.png")
sonido = os.path.join(ruta_base, "LUIMIII LUIMIII LUIMIII.mp3")

ejecutando = True

def validar_codigo(entrada_widget, root_ventana):
    texto = entrada_widget.get()
    
    if texto == "1979":
        pygame.mixer.quit()
        root_ventana.destroy()
    else:
        entrada_widget.delete(0, 'end')
        try:
            pygame.mixer.init()
            efecto = pygame.mixer.Sound(sonido)
            efecto.play()
        except:
            pass

while ejecutando:
    tiempo_espera = random.randint(30, 120)
    
    segundos_pasados = 0
    while segundos_pasados < tiempo_espera:
        if not ejecutando:
            break
        time.sleep(1)
        segundos_pasados = segundos_pasados + 1

    if not ejecutando:
        break
    
    try:
        pygame.mixer.init()
        efecto = pygame.mixer.Sound(sonido)
        efecto.play()

        root = Tk()
        root.title("Bloqueo")
        root.attributes("-fullscreen", True) 
        root.attributes("-topmost", True)    
        root.config(bg="black")             
        root.protocol("WM_DELETE_WINDOW", lambda: None) 

        img_original = Image.open(imagen)
        ancho_pantalla = root.winfo_screenwidth()
        alto_pantalla = root.winfo_screenheight()
        img_redimensionada = img_original.resize((ancho_pantalla, alto_pantalla), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img_redimensionada)
        
        lbl_fondo = Label(root, image=img_tk, bg="black")
        lbl_fondo.place(x=0, y=0, relwidth=1, relheight=1)

        cuadro_centro = Frame(root, bg="#f0f0f0", bd=5, relief="groove")
        cuadro_centro.place(relx=0.5, rely=0.5, anchor="center", relwidth=0.25, height=120)

        lbl_texto = Label(cuadro_centro, text="Hay que aser mimicos Luismiii:", bg="#f0f0f0", font=("OCR A Extended", 11, "bold"))
        lbl_texto.pack(pady=5)

        txt_entrada = Entry(cuadro_centro, justify="center", font=("OCR A Extended", 12))
        txt_entrada.pack(pady=5)
        txt_entrada.focus_set() 

        btn = Button(cuadro_centro, text="Desactivar", font=("OCR A Extended", 10), command=lambda: validar_codigo(txt_entrada, root))
        btn.pack(pady=5)

        root.bind('<Return>', lambda event: validar_codigo(txt_entrada, root))

        root.mainloop()
    except:
        pass