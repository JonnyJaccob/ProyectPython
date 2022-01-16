import tkinter as tk 
#Realizado en Python 3.8.5

ventana = tk.Tk()
ventana.title("Calculadora")

i=0

#Entrada
e_texto = tk.Entry(ventana, font = ("Calibri 20"))
e_texto.grid(row=0,column = 0, columnspan=4, padx = 50, pady=5)

#Funciones
def click_boton(valor):
    global i
    e_texto.insert(i ,valor)
    i += 1
    
def borrar():
    e_texto.delete(0, "end")
    i = 0
    
def hacer_operaciones():
    ecuacion = e_texto.get()
    resultado = eval(ecuacion)
    borrar()
    e_texto.insert(0,resultado)
    i = 0

#Botones
boton1 = tk.Button(ventana,text = "1",width=5,height=2, command = lambda: click_boton(1))
boton2 = tk.Button(ventana,text = "2",width=5,height=2, command = lambda: click_boton(2))
boton3 = tk.Button(ventana,text = "3",width=5,height=2, command = lambda: click_boton(3))
boton4 = tk.Button(ventana,text = "4",width=5,height=2, command = lambda: click_boton(4))
boton5 = tk.Button(ventana,text = "5",width=5,height=2, command = lambda: click_boton(5))
boton6 = tk.Button(ventana,text = "6",width=5,height=2, command = lambda: click_boton(6))
boton7 = tk.Button(ventana,text = "7",width=5,height=2, command = lambda: click_boton(7))
boton8 = tk.Button(ventana,text = "8",width=5,height=2, command = lambda: click_boton(8))
boton9 = tk.Button(ventana,text = "9",width=5,height=2, command = lambda: click_boton(9))
boton0 = tk.Button(ventana,text = "0",width=13,height=2, command = lambda: click_boton(0))

boton_borrar = tk.Button(ventana,text = "AC",width=5,height=2, command = lambda: click_boton())
boton_parentesis1 = tk.Button(ventana,text = "(",width=5,height=2, command = lambda: click_boton("("))
boton_parentesis2 = tk.Button(ventana,text = ")",width=5,height=2, command = lambda: click_boton(")"))
boton_punto = tk.Button(ventana,text = ".",width=5,height=2, command = lambda: click_boton("."))

boton_div = tk.Button(ventana,text = "/",width=5,height=2, command = lambda: click_boton("/"))
boton_mult = tk.Button(ventana,text = "x",width=5,height=2, command = lambda: click_boton("*"))
boton_sum = tk.Button(ventana,text = "+",width=5,height=2, command = lambda: click_boton("+"))
boton_rest = tk.Button(ventana,text = "-",width=5,height=2, command = lambda: click_boton("-"))
boton_igual = tk.Button(ventana,text = "=",width=5,height=2, command = lambda: hacer_operaciones())

#Agregar botones en pantalla
boton_borrar.grid(row = 1, column = 0, padx =5 , pady=5)
boton_parentesis1.grid(row = 1, column = 1, padx =5 , pady=5)
boton_parentesis2.grid(row = 1, column = 2, padx =5 , pady=5)
boton_punto.grid(row = 1, column = 3, padx =5 , pady=5)

boton7.grid(row = 2, column = 0, padx =5 , pady=5)
boton8.grid(row = 2, column = 1, padx =5 , pady=5)
boton9.grid(row = 2, column = 2, padx =5 , pady=5)
boton_mult.grid(row = 2, column = 3, padx =5 , pady=5)

boton4.grid(row = 3, column = 0, padx =5 , pady=5)
boton5.grid(row = 3, column = 1, padx =5 , pady=5)
boton6.grid(row = 3, column = 2, padx =5 , pady=5)
boton_sum.grid(row = 3, column = 3, padx =5 , pady=5)

boton1.grid(row = 4, column = 0, padx =5 , pady=5)
boton2.grid(row = 4, column = 1, padx =5 , pady=5)
boton3.grid(row = 4, column = 2, padx =5 , pady=5)
boton_rest.grid(row = 4, column = 3, padx =5 , pady=5)

boton0.grid(row = 5, column = 0,columnspan = 2 ,padx =5 , pady=5)
boton_punto.grid(row = 5, column = 1, padx =5 , pady=5)
boton_igual.grid(row = 5, column = 2, padx =5 , pady=5)

ventana.mainloop()