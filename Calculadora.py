from tkinter import *
#declarar un objeto de tipo tk
raiz = Tk()
raiz.title("ventana de pruebas")
# metodo de tipo true falce que permite o no agranados o achicar la
#pantalla del programa parametro 1 : alto 2 : ancho
# 0 = false 1 = true
raiz.resizable(1,0)
#introducir un icono 
raiz.iconbitmap("img/calculadora.ico")
#tamaño de pantalla
raiz.geometry("320x480")
#color de panel
raiz.config(bg="#504D8E")
# crear un label 
etiqueta = Label(text="Operacion", font = ("Verdana", 15)).place(x=0, y=15)
# crear una entrada de texto
entrada = StringVar()
campo = Entry(raiz, textvariable=entrada).place(x=150,y=15)
boton= Button(raiz,text="1").place(x=0,y=0)
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")
boton= Button(raiz,text="1")






raiz.mainloop()


