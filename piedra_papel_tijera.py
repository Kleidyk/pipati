from tkinter import *
import tkinter as tk
from tkinter import ttk,font
import random
from tkinter.messagebox import showinfo

class App():

    # valores = ["Piedra","Papel","Tijera"]  #turquoise

    def __init__(self):
        self.__pp = tk.Tk()
        self.__frame = Frame(self.__pp)  
        self.__piedra = PhotoImage(file='clase022\\piedra.png')
        self.__papel = PhotoImage(file='clase022\\papel.png')
        self.__tijera = PhotoImage(file='clase022\\tijera.png')
        self.__titulo = tk.Label(self.__pp,text="Piedra, Papel o Tijera",bg="pink",fg="Purple",font=("Comic Sans MS",20,"bold")) #bold=negrita
        self.__etiqueta1 = tk.Label(self.__pp,text="Ingrese una Opcion: ",bg="pink",fg="Purple",font=("Comic Sans MS",12,'bold'))
        self.__img_piedra = tk.Label(self.__pp, image=self.__piedra)
        self.__boton1 = tk.Button(self.__pp,image=self.__piedra, command=lambda:self.operar(0))
        self.__img_papel = tk.Label(self.__pp, image=self.__papel)
        self.__boton2 = tk.Button(self.__pp,image=self.__papel, command=lambda:self.operar(1))
        self.__img_tijera = tk.Label(self.__pp,image=self.__tijera)
        self.__boton3 = tk.Button(self.__pp,image=self.__tijera, command=lambda:self.operar(2))
        self.__etiqueta3 = tk.Label(self.__pp,text="VS",bg="pink",fg="Purple",font=("Comic Sans MS",50,"bold"))
        self.__salir = tk.Button(self.__pp,text="Salir",command=quit)

        self.__frame.pack() 
        self.__titulo.place(x=110, y=40)
        self.__etiqueta1.place(x=30,y=85)
        self.__img_piedra.place(x=100,y=120)
        self.__boton1.place(x=100,y=120)
        self.__img_papel.place(x=215,y=120)
        self.__boton2.place(x=215,y=120)
        self.__img_tijera.place(x=330,y=120)
        self.__boton3.place(x=330,y=120)
        self.__etiqueta3.place(x=210,y=280)
        self.__salir.place(x=350,y=450)

        self.configurar()

    def operar(self,value):
        self.__valores = ['piedra','papel','tijera']
        self.__aleatorio = random.choice(self.__valores)
        self.__cpu = self.__aleatorio
        self.__usuario = value

        if self.__usuario == 0:
            self.__dusuario10 = tk.Label(self.__pp,text='Elegiste Piedra',bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            self.__imagen1 = PhotoImage(file='clase022\\piedra.png')
            self.__lblusuario = tk.Label(self.__pp,image=self.__imagen1)
            self.__dcpu11 = tk.Label(self.__pp,text="La CPU eligio: "+str(self.__cpu),bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            if self.__cpu == "piedra":
                self.__imagen2 = PhotoImage(file='clase022\\piedra.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text="Empate!!!",bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold")) 
            elif self.__cpu == "papel":
                self.__imagen2 = PhotoImage(file='clase022\\papel.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text="Perdiste!!!",bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            elif self.__cpu == "tijera":
                self.__imagen2 = PhotoImage(file='clase022\\tijera.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text="Ganaste!!!",bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))           
        if self.__usuario == 1:
            self.__dusuario10 = tk.Label(self.__pp,text='Elegiste Papel',bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            self.__imagen1 = PhotoImage(file='clase022\\papel.png')
            self.__lblusuario = tk.Label(self.__pp,image=self.__imagen1)
            self.__dcpu11= tk.Label(self.__pp,text="La CPU eligio: "+str(self.__cpu),bg="pink",fg="Purple",font=("Comic Sans MS",12,"bold"))
            if self.__cpu == "piedra":
                self.__imagen2 = PhotoImage(file='clase022\\piedra.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text="Ganaste!!!",bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            elif self.__cpu == "papel":
                self.__imagen2 = PhotoImage(file='clase022\\papel.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text='Empate!!!',bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            elif self.__cpu == "tijera": 
                self.__imagen2 = PhotoImage(file='clase022\\tijera.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text="Perdiste!!!",bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
        if self.__usuario == 2:
            self.__dusuario10 = tk.Label(self.__pp,text='Elegiste Tijera',bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            self.__imagen1 = PhotoImage(file='clase022\\tijera.png')
            self.__lblusuario = tk.Label(self.__pp,image=self.__imagen1)
            self.__dcpu11 = tk.Label(self.__pp,text="La CPU eligio: "+str(self.__cpu),bg="pink",fg="Purple",font=("Comic Sans MS",12,"bold"))
            if self.__cpu == "piedra":
                self.__imagen2 = PhotoImage(file='clase022\\piedra.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text="Perdiste!!!",bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            elif self.__cpu == "papel":
                self.__imagen2 = PhotoImage(file='clase022\\papel.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text="Ganaste!!!",bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))
            elif self.__cpu == "tijera": 
                self.__imagen2 = PhotoImage(file='clase022\\tijera.png')
                self.__lblcpu = tk.Label(self.__pp,image=self.__imagen2)
                self.__label = tk.Label(self.__pp,text='Empate!!!',bg='pink',fg='Purple',font=("Comic Sans MS",12,"bold"))        
       
        # Margenes #0
        self.__dusuario10.place(x=30,y=230) 
        self.__lblusuario.place(x=100,y=290)
        self.__dcpu11.place(x=300,y=230)   
        self.__lblcpu.place(x=340,y=300)
        self.__lblcpu.place(x=340,y=290)
        self.__lblcpu.place(x=340,y=290)
        self.__label.place(x=90,y=400)


        # Margenes #1
        self.__dusuario10.place(x=30,y=230) 
        self.__lblusuario.place(x=100,y=290)
        self.__dcpu11.place(x=300,y=230)   
        self.__lblcpu.place(x=340,y=300)
        self.__lblcpu.place(x=340,y=290)
        self.__lblcpu.place(x=340,y=290)

        # # Margenes #2
        self.__dusuario10.place(x=30,y=230) 
        self.__lblusuario.place(x=100,y=290)
        self.__dcpu11.place(x=300,y=230)   
        self.__lblcpu.place(x=340,y=300)
        self.__lblcpu.place(x=340,y=290)
        self.__lblcpu.place(x=340,y=290)
      

    def configurar(self):
        self.__pp.title("Piedra, Papel o Tijera")
        self.__pp.configure(background="pink")
        self.__pp.resizable(0,0)
        self.__pp.config(bg="pink")          # color de fondo, background
        self.__pp.config(cursor="heart")    # tipo de cursor (arrow defecto)
        self.__pp.config(relief="sunken")  
        self.__frame.config(bg="pink")     
        self.__frame.config(width=500,height=500) 
        self.__frame.config(cursor="")         
        self.__frame.config(relief="sunken")  
        self.__frame.config(bd=25)  
        

    def inicio(self):
        self.__pp.mainloop()

def main():

    App().inicio()

main()


