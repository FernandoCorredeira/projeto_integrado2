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

def tela_repositor(cod_user):  
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

    def tela_produto():


       
        print(cod_user)
        def btn_add_product(): 

            data_user = cod_user
            data_name = i_name_product.get()
            data_invoice = i_invoice.get()
            data_categories = i_categories.get()
            data_deposits = i_deposits.get()
            data_amount = i_amount.get()
            data_value = i_value.get()

            list_data = [data_user, data_name, data_invoice, data_categories, data_deposits, data_amount, data_value]

            for i in list_data:
                if i == '':
                    messagebox.showerror('Erro','É necessario a inserção de todos os dados')
                    return
                
                create_product(data_user, data_name, data_invoice, data_categories, data_deposits, data_amount, data_value)
                messagebox.showinfo('Sucesso','Produto Cadastrado')

                i_name_product.delete(0,END)
                i_invoice.delete(0,END)
                i_categories.delete(0,END)
                i_deposits.delete(0,END)
                i_amount.delete(0,END)
                i_value.delete(0,END)
                    


        
        app_ = Label(frameDireita, text="Inserir novo Produto", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 17'), bg=co2, fg=co1)
        app_.grid(row=0, column=0, columnspan=4,sticky=NSEW)

        app_linha = Label(frameDireita,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 , fg=co4)
        app_linha.grid(row=1, column=0, columnspan=4, sticky=NSEW)
        


        #Texto cod usuario
        l_cod_user = Label(frameDireita, text="Código do usuário:", font=('Ivy 12'), bg=co3, fg=co5)
        l_cod_user.grid(row=2, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do cod usuario
        l_cod_user = Label(frameDireita, text=f"{cod_user}", font=('Ivy 13'), bg=co3, fg=co4)
        l_cod_user.grid(row=2, column=1, padx=5,pady=10, sticky=NSEW)

        #Texto Nome do produto
        l_name_product = Label(frameDireita, text="Nome do Produto", font=('Ivy 12'), bg=co3, fg=co5)
        l_name_product.grid(row=3, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do produto
        i_name_product = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_name_product.grid(row=3, column=1, padx=5,pady=10, sticky=NSEW)

        #Texto Nota fiscal
        l_invoice = Label(frameDireita, text="Nota Fiscal", font=('Ivy 12'), bg=co3, fg=co5)
        l_invoice.grid(row=4, column=0, padx=5,pady=10, sticky=NSEW)
        # Input NF
        i_invoice = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_invoice.grid(row=4, column=1, padx=5,pady=10, sticky=NSEW)
        
        #Texto de Categorias
        l_categories = Label(frameDireita, text="Categoria", font=('Ivy 12'), bg=co3, fg=co5)
        l_categories.grid(row=5, column=0, padx=5,pady=10, sticky=NSEW)
        # Input da categoria
        i_categories = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_categories.grid(row=5, column=1, padx=5,pady=10, sticky=NSEW)
        
        #Texto Depositos
        l_deposits = Label(frameDireita, text="Deposito", font=('Ivy 12'), bg=co3, fg=co5)
        l_deposits.grid(row=6, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do Deposito
        i_deposits = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_deposits.grid(row=6, column=1, padx=5,pady=10, sticky=NSEW)

        # Texto Quantidade
        l_amount = Label(frameDireita, text="Quantidade", font=('Ivy 12'), bg=co3, fg=co5)
        l_amount.grid(row=7, column=0, padx=5,pady=10, sticky=NSEW)
        # Input da quantidade
        i_amount = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_amount.grid(row=7, column=1, padx=5,pady=10, sticky=NSEW)
        # Texto valor
        l_value = Label(frameDireita, text="Valor", font=('Ivy 12'), bg=co3, fg=co5)
        l_value.grid(row=8, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do valor
        i_value = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_value.grid(row=8, column=1, padx=5,pady=10, sticky=NSEW)

        #btn salvar
        b_car_salvar = Button(frameDireita, command=btn_add_product, compound=LEFT, width=25, anchor=NW, text=" Salvar Produto", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        b_car_salvar.grid(row=9, column=1, sticky=NSEW, pady=5)   

    def tela_att_produto():
        def btn_add_product(): 

            data_user = cod_user
            data_name = i_name_product.get()
            data_invoice = i_invoice.get()
            data_categories = i_categories.get()
            data_deposits = i_deposits.get()
            data_amount = i_amount.get()
            data_value = i_value.get()

            list_data = [data_user, data_name, data_invoice, data_categories, data_deposits, data_amount, data_value]

            for i in list_data:
                if i == '':
                    messagebox.showerror('Erro','É necessario a inserção de todos os dados')
                    return
                
                create_product(data_user, data_name, data_invoice, data_categories, data_deposits, data_amount, data_value)
                messagebox.showinfo('Sucesso','Produto Cadastrado')

                i_name_product.delete(0,END)
                i_invoice.delete(0,END)
                i_categories.delete(0,END)
                i_deposits.delete(0,END)
                i_amount.delete(0,END)
                i_value.delete(0,END)
                    


        
        app_ = Label(frameDireita, text="Atualizar Produtos", width=50, compound=LEFT, padx=5, pady=10, font=('Verdana 17'), bg=co2, fg=co1)
        app_.grid(row=0, column=0, columnspan=4,sticky=NSEW)

        app_linha = Label(frameDireita,width=770, height=1, compound=LEFT, padx=5, anchor=NW, font=('Verdana 1'), bg=co0 , fg=co4)
        app_linha.grid(row=0, column=0, columnspan=4, sticky=NSEW)
        


        #Texto cod usuario
        l_cod_user = Label(frameDireita, text="Código do usuário:", font=('Ivy 12'), bg=co3, fg=co5)
        l_cod_user.grid(row=2, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do cod usuario
        l_cod_user = Label(frameDireita, text=f"{cod_user}", font=('Ivy 13'), bg=co3, fg=co4)
        l_cod_user.grid(row=2, column=1, padx=5,pady=10, sticky=NSEW)

        #Texto Nome do produto
        l_name_product = Label(frameDireita, text="Nome do Produto", font=('Ivy 12'), bg=co3, fg=co5)
        l_name_product.grid(row=3, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do produto
        i_name_product = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_name_product.grid(row=3, column=1, padx=5,pady=10, sticky=NSEW)

        #Texto Nota fiscal
        l_invoice = Label(frameDireita, text="Nota Fiscal", font=('Ivy 12'), bg=co3, fg=co5)
        l_invoice.grid(row=4, column=0, padx=5,pady=10, sticky=NSEW)
        # Input NF
        i_invoice = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_invoice.grid(row=4, column=1, padx=5,pady=10, sticky=NSEW)
        
        #Texto de Categorias
        l_categories = Label(frameDireita, text="Categoria", font=('Ivy 12'), bg=co3, fg=co5)
        l_categories.grid(row=5, column=0, padx=5,pady=10, sticky=NSEW)
        # Input da categoria
        i_categories = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_categories.grid(row=5, column=1, padx=5,pady=10, sticky=NSEW)
        
        #Texto Depositos
        l_deposits = Label(frameDireita, text="Deposito", font=('Ivy 12'), bg=co3, fg=co5)
        l_deposits.grid(row=6, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do Deposito
        i_deposits = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_deposits.grid(row=6, column=1, padx=5,pady=10, sticky=NSEW)

        # Texto Quantidade
        l_amount = Label(frameDireita, text="Quantidade", font=('Ivy 12'), bg=co3, fg=co5)
        l_amount.grid(row=7, column=0, padx=5,pady=10, sticky=NSEW)
        # Input da quantidade
        i_amount = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_amount.grid(row=7, column=1, padx=5,pady=10, sticky=NSEW)
        # Texto valor
        l_value = Label(frameDireita, text="Valor", font=('Ivy 12'), bg=co3, fg=co5)
        l_value.grid(row=8, column=0, padx=5,pady=10, sticky=NSEW)
        # Input do valor
        i_value = Entry(frameDireita, width=25,justify='left', relief='solid')
        i_value.grid(row=8, column=1, padx=5,pady=10, sticky=NSEW)

        #btn salvar
        b_car_salvar = Button(frameDireita, command=btn_add_product, compound=LEFT, width=25, anchor=NW, text=" Salvar Produto", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
        b_car_salvar.grid(row=9, column=1, sticky=NSEW, pady=5)   

    def controlMenuProdutos(i):
        if i == "Registrar Produtos":
            for widget in frameDireita.winfo_children():
                widget.destroy()
            tela_produto()

    def controlMenuAttProdutos(i):
        if i == "Atualizar Produtos":
            for widget in frameDireita.winfo_children():
                widget.destroy()
            tela_att_produto()



#Menu lateral

    b_car = Button(frameEsquerda,command=lambda:controlMenuProdutos('Registrar Produtos'), compound=LEFT, anchor=NW, text="Registrar Produtos", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_car.grid(row=0, column=0, sticky=NSEW, padx=5,pady=6)

    b_car = Button(frameEsquerda,command=lambda:controlMenuAttProdutos('Atualizar Produtos'), compound=LEFT, anchor=NW, text="Atualizar Produtos", bg=co5, fg=co2, font=('Ivy 11'), overrelief=RIDGE, relief=GROOVE)
    b_car.grid(row=1, column=0, sticky=NSEW, padx=5,pady=6)










    windowUser.mainloop()
