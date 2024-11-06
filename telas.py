from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from req import *
from tela_repositor import *
from tela_gerente import *
from tela_usuario import *

co0 = "#6A5ACD"
co1 = "#87CEEB"
co2 = "#FFFAFA"
co3 = "#E6E6FA"
co4 = "#FA8072"
co5 = "#708090" #Gray

# Janela/Widget Window
window = Tk()
window.title("Gerenciamento")
window.geometry('590x300')
window.configure(background=co3)
window.resizable(width=FALSE, height=FALSE)
style = Style(window)
style.theme_use("clam")


            #container
frameCima=Frame(window, width=790, height=50, bg=co1, relief="flat")
frameCima.grid(row=0,column=0, columnspan=2, sticky=NSEW)
app_ = Label(frameCima, text="Login de Usuario", compound=LEFT, padx=5, pady=10, anchor=NW, font=('Verdana 15 bold'), fg=co4)
app_.place(x=50, y=7)
app_linha = Label(frameCima,width=770, height=1, compound=LEFT, padx=5, pady=10, anchor=NW, font=('Verdana 1'), bg=co0 ,fg=co4)
app_linha.place(x=0, y=47)


def btn_login():
    login = i_login_usuario.get()
    password = i_pw_usuario.get()

    print (login, password)
    data = get_usuarios()
    usuarios = list()
    for usuario in data:
        usuarios.append({
            'id_usuario': usuario[0],
            'id_categoria': usuario[1],
            'nome_usuario': usuario[2],
            'senha_usuario': usuario[3]
        })
    
    cont = 0
    for usuario in usuarios:
        cont += 1

        if login == usuario['nome_usuario'] and password == usuario['senha_usuario'] and 1 == usuario['id_categoria']:
            print ('sucesso')
            cod_user =  (usuario['id_usuario'])
            tela_repositor(cod_user)
            return cod_user
        
        if login == usuario['nome_usuario'] and password == usuario['senha_usuario'] and 2 == usuario['id_categoria']:
            print ('sucesso')
            cod_user =  (usuario['id_usuario'])
            tela_usuario(cod_user)
            return cod_user
        
        if login == usuario['nome_usuario'] and password == usuario['senha_usuario'] and 3 == usuario['id_categoria']:
            print ('sucesso')
            cod_user =  (usuario['id_usuario'])
            tela_gerente(cod_user)
            return cod_user

            
        if cont >= len(usuarios):
            print("Usuario nao encontrado")

            #Login
login_usuario = Label(window, anchor=CENTER,text="Login", font=('Ivy 12'), bg=co3, fg=co5)
login_usuario.grid(row=2, column=0, padx=50,pady=10, sticky=NSEW)
           
            # Input 
i_login_usuario = Entry(window, width=25,justify='center', relief='solid')
i_login_usuario.grid(row=3, column=0,padx=5,pady=10, sticky=NSEW)
            
            #Senha
w_pw_usuario = Label(window, justify='center',text="Senha", font=('Ivy 12'), bg=co3, fg=co5)
w_pw_usuario.grid(row=4, column=0, padx=5,pady=10, sticky=NSEW)
            
            # Input 
i_pw_usuario = Entry(window, width=25,justify='center', relief='solid')
i_pw_usuario.grid(row=5, column=0, padx=5,pady=10, sticky=NSEW)
        

b_login = Button(window, command=btn_login, compound=LEFT, width=15, anchor=NW, text=" Login", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
b_login.grid(row=6, column=0, sticky=NSEW,padx=5, pady=5)
        





window.mainloop()