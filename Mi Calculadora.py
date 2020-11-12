import tkinter as tk
from tkinter import ttk
from tkinter import Menu
from tkinter import messagebox


def crear_ventana():
    ventana = tk.Tk()
    ventana.title('Mi primera aplicación')
    ventana.geometry('400x300')

    label = tk.Label(ventana, text='Calculadora', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    numero1 = tk.Entry(ventana, width=10)
    numero2 = tk.Entry(ventana, width=10)

    numero1.grid(column=1, row=1)
    numero2.grid(column=1, row=2)

    label_numero1 = tk.Label(ventana, text='Ingrese primer numero', font=('Arial bold', 10))
    label_numero1.grid(column=0, row=1)

    label_numero2 = tk.Label(ventana, text='Ingrese segundo numero', font=('Arial bold', 10))
    label_numero2.grid(column=0, row=2)

    operadores = ttk.Combobox(ventana)
    operadores['values'] = ['+', '-', '*', '/', 'pow']
    operadores.current(0)
    operadores.grid(column=1, row=3)

    label_operadores = tk.Label(ventana, text='Seleccione operador', font=('Arial bold', 10))
    label_operadores.grid(column=0, row=3)

    boton_calcular = tk.Button(ventana, command=lambda: Click_calcular(label_resultado, numero1.get(), numero2.get(),
                                                                       operadores.get()), text='Calcular', bg='blue',
                               fg='white')
    boton_calcular.grid(column=1, row=4)

    label_resultado = tk.Label(ventana, text='Resultado: ', font=('Arial bold', 15))
    label_resultado.grid(column=0, row=5)

    menu = Menu(ventana)
    menu.add_command(label='Expandir Binomio', command=lambda: Binomio(ventana))
    menu.add_command(label='Numeros Cuadrados', command=lambda: Cuadrados(ventana))

    ventana.config(menu=menu)
    ventana.mainloop()

def Binomio(ventana):
    Expandir_binomios = tk.Toplevel(ventana)
    Expandir_binomios.title('Mi primera aplicación')
    Expandir_binomios.geometry('400x300')
    label = tk.Label(Expandir_binomios, text='Expandir Binomio X + Y', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    numero = tk.Entry(Expandir_binomios, width=10)
    numero.grid(column=1, row=1)

    label_numero = tk.Label(Expandir_binomios, text='Potencia a elevar: ', font=('Arial bold', 10))
    label_numero.grid(column=0, row=1)

    label_resultado = tk.Label(Expandir_binomios, text='Binomio expandido:', font=('Arial bold', 15))
    label_resultado.grid(column=0, row=5)
    boton_calcular = tk.Button(Expandir_binomios, command=lambda: Click_binomios(label_resultado, numero.get()), text='Expandir', bg='blue',fg='white')
    boton_calcular.grid(column=1, row=4)

def Cuadrados(ventana):
    Cuadrados= tk.Toplevel(ventana)
    Cuadrados.title('Mi primera aplicación')
    Cuadrados.geometry('400x300')
    label = tk.Label(Cuadrados, text='Numeros Cuadrados', font=('Arial bold', 15))
    label.grid(column=0, row=0)

    label = tk.Label(Cuadrados, text='(Comprueba si un numero es cudrado)', font=('Arial bold', 10))
    label.grid(column=0, row=1)

    numero = tk.Entry(Cuadrados, width=10)
    numero.grid(column=1, row=2)

    label_numero = tk.Label(Cuadrados, text='Numero que desea comprobar: ', font=('Arial bold', 10))
    label_numero.grid(column=0, row=2)

    label_resultado = tk.Label(Cuadrados, text='El numero es cuadrado: ', font=('Arial bold', 15))
    label_resultado.grid(column=0, row=5)

    boton_calcular = tk.Button(Cuadrados, command=lambda: Click_cuadrados(label_resultado, numero.get()), text='Comprobar', bg='blue',fg='white')
    boton_calcular.grid(column=1, row=4)

def Calcular(Num1, Num2, Operador):
    if Operador == '+':
        Resultado = Num1 + Num2
    elif Operador == '-':
        Resultado = Num1 - Num2
    elif Operador == '*':
        Resultado = Num1 * Num2
    elif Operador == '/':
        Resultado = Num1 / Num2
    else:
        Resultado = Num1 ** Num2
    return Resultado

def Click_calcular(label, Num1, Num2, Operador):
    try:
        Valor1 = float(Num1)
        Valor2 = float(Num2)

    except ValueError:
        messagebox.showinfo('Reingresar valores', 'Los valores ingresados no son numericos')

    resultado = Calcular(Valor1, Valor2, Operador)
    label.configure(text='Resultado= ' + str(resultado))

def FACTORIAL(A):
    FT = 1
    for F in range(1,A+1):
        FT = FT * F
    return FT

def COEFICIENTE_BINOMIAL(A,B):
    CB = (FACTORIAL(A))/((FACTORIAL(B))*(FACTORIAL(A-B)))
    return str(int(CB))

def VARIABLE_ELEVADA(X,Y,A,B):
    PX = A-B
    PY = A-PX
    VEX = X + '**' + str(PX)
    VEY = '*' + Y + '**' + str(PY)
    if PX == 0:
        VEX = ''
        VEY = Y + '**' + str(PY)
    elif PY == 0:
        VEY = ''
    elif PX == 1:
        VEX = X
    elif PY == 1:
        VEY = '*' + Y
    VE = VEX + VEY
    return VE

def EXPANSION_BINOMIO(A,B,X,Y):
    if COEFICIENTE_BINOMIAL(A,B) == '1':
        EB = VARIABLE_ELEVADA(X,Y,A,B)
    else:
        EB = (COEFICIENTE_BINOMIAL(A,B)) + '*' + (VARIABLE_ELEVADA(X,Y,A,B))
    return EB

def main_Binomios(A):
    X = 'x'
    Y = 'y'
    EBT = ''
    if A == 1:
        return "x+y"
    else:
        for B in range(A + 1):
            if B == 0:
                EBT = EBT + EXPANSION_BINOMIO(A, B, X, Y)
            else:
                EBT = EBT + '+' + EXPANSION_BINOMIO(A, B, X, Y)
        return EBT

def Click_binomios(label, Num1):
    try:
        Valor1 = int(Num1)

    except ValueError:
        messagebox.showinfo('Reingresar valores', 'El valor ingresado no es numerico')

    resultado = main_Binomios(Valor1)
    label.configure(text='Binomio expandido= ' + str(resultado))

def NUMERO_CUADRADO(X):
    if (X**(1/2)%1) == 0:
        return True
    else:
        return False

def Numeros_cuadrados(X):
    A = int(X ** (1 / 2))
    if NUMERO_CUADRADO(X) is True:
        return 'El numero que ingreso si es cuadrado'
    else:
        return "El numero ingresado no es cuadrado"


def Click_cuadrados(label, Num1):
    try:
        Valor1 = int(Num1)

    except ValueError:
        messagebox.showinfo('Reingresar valores', 'El valor ingresado no es numerico')

    resultado = Numeros_cuadrados(Valor1)
    label.configure(text='El numero es cuadrado: ' + str(resultado))

def main():
    crear_ventana()

main()