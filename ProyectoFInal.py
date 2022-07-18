# from ctypes import resize
# from distutils.cmd import Command
# from email.mime import image
from cProfile import label
from email.mime import image
from tkinter import *
#from turtle import clear, width
from PIL import Image, ImageTk
import subprocess

tareas = []
x = ""
a = 0

root = Tk()
root.title('Blossom Time')
root.config(bg='Lightgreen')
root.config(bd=10)
root.config(relief="groove")
root.config(cursor='pirate')
root.iconbitmap('calendario.ico')



#funciones
def Intask():                 #Abre la pantalla para agregar tareas
    global e
    global top1
    top1 = Toplevel()
    top1.minsize(width=500, height=300)
    e = Entry(top1, width=70)
    Label(top1, text='Escribe la tarea que deseas agregar a la lista.').pack()
    e.pack()
    #Button(top1, text="Agregar tarea", command=ListTask(e.get())).pack()
    Button(top1, text="Agregar tarea",command=lambda: ListTaks(e.get()), ).pack()
    Button(top1, text="Cerrar", command= top1.destroy).pack()
    
    #ListTaks(x)

def ListTaks(palabra):          #Agrega la tarea en la lista "tareas"
    e.delete(0, END)
    tareas.append(palabra)
    Label(top1, text="Se agrego tu tarea").pack()




def PrintTask():                 # se imprimen tareas
    global top2
    global a
    top2 = Toplevel()
    top2.minsize(width=500, height=300)
    Label(top2, text="Tareas pendientes").pack()  
    r = IntVar()
    cont=0
    for i in tareas:
        Radiobutton(top2, text=i, variable=r,value=cont).pack()
        cont+=1
    a+=1    


    Button(top2, text="Seleccionar", command=tiempo).pack() 
    Button(top2, text="Completar",command=lambda: eliminar(r.get(),a) ).pack()   
    Button(top2, text="Cerrar", command=top2.destroy).pack()
    
    

def tiempo(): #ventana tiempo

    subprocess.call("cronometro.py", shell=True)

#completar y subir nivel
def eliminar(posicion,b):
    tareas.pop(posicion)
    top2.after(20, top2.destroy)
    
    # top3 = Toplevel()
    # top3.config(bg='Black')
    #top3.minsize(width=500, height=614)
    # img2 = Image.open('Homero.png')
    # resized2= ImageTk.PhotoImage(img2.resize((500, 500), Image.LANCZOS))   
    # newimg2=Label(root, image = resized2)
    # newimg2.pack()
    imagenes[b].grid(row=1, column=0, rowspan=4 )
    root.after(200, PrintTask)

    





    


    

    

    




#pic in root
Label(text='Bienvenido a Blossom time',font=('Chiller', 25), bg='Lightgreen', fg='white').grid(row=0, column=0)
img1 = Image.open('1.png')
resized = ImageTk.PhotoImage(img1.resize((409, 614), Image.ANTIALIAS))   
newimg1=Label(root, image = resized)

img2 = Image.open('2.png')
resized2 = ImageTk.PhotoImage(img2.resize((409, 614), Image.ANTIALIAS))   
newimg2=Label(root, image = resized2)

img3 = Image.open('3.png')
resized3 = ImageTk.PhotoImage(img3.resize((409, 614), Image.ANTIALIAS))   
newimg3=Label(root, image = resized3)

img4 = Image.open('4.png')
resized4 = ImageTk.PhotoImage(img4.resize((409, 614), Image.ANTIALIAS))   
newimg4=Label(root, image = resized4)

img5 = Image.open('5.png')
resized5 = ImageTk.PhotoImage(img5.resize((409, 614), Image.ANTIALIAS))   
newimg5=Label(root, image = resized5)

img6 = Image.open('6.png')
resized6 = ImageTk.PhotoImage(img6.resize((409, 614), Image.ANTIALIAS))   
newimg6=Label(root, image = resized6)

img7 = Image.open('7.png')
resized7 = ImageTk.PhotoImage(img7.resize((409, 614), Image.ANTIALIAS))   
newimg7=Label(root, image = resized7)

img8 = Image.open('8.png')
resized8 = ImageTk.PhotoImage(img8.resize((409, 614), Image.ANTIALIAS))   
newimg8=Label(root, image = resized8)

img9 = Image.open('Homero.png')
resized9 = ImageTk.PhotoImage(img9.resize((409, 614), Image.ANTIALIAS))   
newimg9=Label(root, image = resized9)


imagenes=[newimg1,newimg2,newimg3,newimg4,newimg5,newimg6,newimg7,newimg8,newimg9]


#buttons in root
b1 = Button(root, text='Agrega tu tarea', padx=20, pady=30, command=Intask)
bExit = Button(root, text='Salir', command=quit, padx=40, pady=30)
bList = Button(root, text='lista de Tareas', padx=20, pady=30, command=PrintTask)
bTamaguchi = Button(root, text='Tamaguchi', padx=40, pady=30)


#posititions widgets in root
newimg1.grid(row=1, column=0, rowspan=4 )
b1.grid(row=1, column=1)
bExit.grid(row=4, column=1)
bList.grid(row=2, column=1)
#bTamaguchi.grid(row=3, column=1)


root.mainloop()


