from tkinter import *
from tkinter import ttk
import math

#Definiendo 
root = Tk()
#Tamaño
root.geometry('600x300+0+0')
#Evitar maximixar
root.resizable(0, 0)
#Title
root.title("CALCULADORA TIRO PARABOLICO.")

#Funciones
def click():
    #variables
    gravedad = 9.81
    velocidad_cantidad = float(velocidad_input.get())
    angulo_cantidad = float(angulo_input.get())

    
    #tiempo
    tiempo_seno = math.sin(math.radians(angulo_cantidad))
    tiempos = ((2*velocidad_cantidad)*tiempo_seno)/gravedad
    tiempo_resultado.configure(text= '{0:.2f} s.'.format(tiempos))
    
    #altura
    altura = ((velocidad_cantidad ** 2)*(math.sin(math.radians(angulo_cantidad)))*(math.sin(math.radians(angulo_cantidad))))/2*(gravedad)
    altura_resultado.configure(text='{0:.2f} m.'.format(altura))

    #distancia
    cosenos = math.cos(math.radians(angulo_cantidad))
    distancia_multiplicacion= velocidad_cantidad*cosenos*tiempos
    distancia_resultado.configure(text= '{0:.2f} m'.format(distancia_multiplicacion))

    #Ecuacion
    ecuacion_resultado.configure(text='y = {}*sen ({}) *t - 0.5*{}*(t)^2'.format(velocidad_cantidad,angulo_cantidad,gravedad))

   
#APP
#Espacio para fila
titulo = Label(text='')
titulo.grid(row = 0)

#Propiedades de velocidad
velocidad = Label(text='Ingrese la velocidad del objeto en m/s: ',bg = '#FAB812')
velocidad.grid(row=1,column=0)

velocidad_input = Entry(root, width=25)
velocidad_input.grid(row=1,column=1)

#Propiedades de Angulo
angulo = Label(text='Ingrese el angulo del objeto °: ',bg = '#FAB812')
angulo.grid(row=2,column=0)

angulo_input = Entry(root,width=25)
angulo_input.grid(row=2,column=1)

#Propiedades del Boton
btn = Button(root, text='Calcular', command=click).grid(row=3,column=1)

#Espacio 
espacio = Label(text= '').grid(row=4)

#Propiedades de los resultado
altura = Label(text='La altura máxima del objeto es: ')
altura.grid(row=5,column=0)

altura_resultado = Label(text=' ')
altura_resultado.grid(row=5, column=1)

distancia = Label(text='La distancia máxima del objeto es: ')
distancia.grid(row=6,column=0)

distancia_resultado = Label(text=' ')
distancia_resultado.grid(row=6, column=1)

tiempo = Label(text='El tiempo de vuelo recorrido fue: ')
tiempo.grid(row=7, column=0)

tiempo_resultado = Label(text=' ')
tiempo_resultado.grid(row=7,column=1)

ecuacion = Label(text='La ecuacion de la trayectoria es: ')
ecuacion.grid(row=8, column=0)

ecuacion_resultado = Label(text='')
ecuacion_resultado.grid(row=8, column=1)

#Evitar cierre
root.mainloop()