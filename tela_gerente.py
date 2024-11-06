from tkinter .ttk import *
from tkinter import *
from tkinter import Tk, ttk
from tkinter import messagebox
from req import *



co0 = "#6A5ACD"
co1 = "#87CEEB"
co2 = "#FFFAFA"
co3 = "#E6E6FA"
co4 = "#FA8072"
co5 = "#708090" #Gray

def tela_gerente(cod_user):  
    windowUser = Tk()
    windowUser.title("Gerenciamento de Estoque")
    windowUser.geometry('790x450')
    windowUser.configure(background=co3)
    windowUser.resizable(width=FALSE, height=FALSE)
    style = Style(windowUser)
    style.theme_use("clam")
    style = Style(windowUser)
    style.theme_use("clam")


    frameCima = Frame(windowUser, width=770, height=50, bg=co1, relief="flat")
    frameCima.grid(row=0,column=0, columnspan=2, sticky=NSEW)
    
    frameEsquerda = Frame(windowUser, width=150, height=790, bg=co4, relief="solid")
    frameEsquerda.grid(row=1,column=0, sticky=NSEW)

    frameDireita = Frame(windowUser, width=600, height=265, bg=co3, relief="raised")
    frameDireita.grid(row=1,column=1, sticky=NSEW)

                # Style Container Header
    app_ = Label(frameCima, text="Gerenciamento de Estoque", compound=LEFT, padx=5, anchor=NW, font=('Verdana 15 bold'), fg=co4)
    app_.place(x=50, y=7)
    app_linha = Label(frameCima,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 ,fg=co4)
    app_linha.place(x=0, y=47)

    def tela_solicitacaoCompras():
       
        print(cod_user)
        
    app_ = Label(frameDireita, text="Solicitações de Compras", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 17'), bg=co2, fg=co1)
    app_.grid(row=0, column=0, columnspan=3,sticky=NSEW)
    app_linha = Label(frameDireita,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 , fg=co4)
    app_linha.grid(row=1, column=0, columnspan=3, sticky=NSEW)
        
    app_ = Label(frameDireita, text="Solicitações de Compras", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 17'), bg=co2, fg=co1)
    app_.grid(row=0, column=0, columnspan=4,sticky=NSEW)

    app_linha = Label(frameDireita,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 , fg=co4)
    app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)

    datas = get_solicitacao()
    print(datas)
    list_header = ['ID Usuario','ID Solicitação','Produto','Quantidade','Valor']

    global tree

    tree = ttk.Treeview(frameDireita, selectmode="extended", columns=list_header, show='headings')

    #Vertical Scrollbar

    vsb = ttk.Scrollbar(frameDireita, orient='vertical',command=tree.yview)

    #Horizontal Scrollbar

    hsb = ttk.Scrollbar(frameDireita, orient='horizontal', command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    frameDireita.grid_rowconfigure(0, weight=12)

    hd=['nw', 'nw', 'nw', 'nw', 'nw', 'nw']
    h=[20, 80, 80, 120, 120, 76, 100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')

        tree.column(col, width=h[n], anchor=hd[n])

        n+=1

        for item in datas:
           tree.insert('', 'end', values=item)



        #btn salvar
        b_car_salvar = Button(frameDireita, compound=LEFT, width=25, anchor=NW, text=" Salvar Compra", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        b_car_salvar.grid(row=11, column=0, sticky='', pady=5)   


    def controlMenu(i):
        if i == "Compras":
            for widget in frameDireita.winfo_children():
                widget.destroy()
                tela_solicitacaoCompras()

#Menu lateral

    b_car = Button(frameEsquerda,command=lambda:controlMenu('Compras'), compound=LEFT, anchor=NW, text="Compras", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_car.grid(row=0, column=0, sticky='', padx=5,pady=6)

    b_car = Button(frameEsquerda,command=lambda:controlMenu('Usuários'), compound=LEFT, anchor=NW, text="Compras", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_car.grid(row=0, column=0, sticky='', padx=5,pady=6)


    windowUser.mainloop()
