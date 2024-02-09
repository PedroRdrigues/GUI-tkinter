from tkinter import * # Inicio da aula 01

root = Tk()

class App():
    def __init__(self) -> None:
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_frame1()
        root.mainloop()
    
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=500, height=300)
    
    
    def frames_tela(self): # Inicio da aula 02
        self.frame_1 = Frame(
            self.root, bd=4, bg='#dfe3ee',
            highlightbackground='#759de6', highlightthickness=1.8
        )
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)
        
        
        self.frame_2 = Frame(
            self.root, bd=4, bg='#dfe3ee',
            highlightbackground='#759de6', highlightthickness=1.8
        )
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)
    
    
    def widgets_frame1(self): # Inicio da aula 03
        # Botão de limpar.
        self.bt_limpar = Button(self.frame_1, text='Limpar', bg='#2fabe9')
        self.bt_limpar.place(relx=0.21, rely=0.1, relwidth=0.1, relheight=0.169)
        # Botão de Busca.
        self.bt_buscar = Button(self.frame_1, text='Buscar', bg='#2fabe9')
        self.bt_buscar.place(relx=0.32, rely=0.1, relwidth=0.1, relheight=0.169)
        # Botão Novo.
        self.bt_novo = Button(self.frame_1, text='Novo', bg='#2fabe9')
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.169)
        # Botão de Alterar.
        self.bt_alterar = Button(self.frame_1, text='Alterar', bg='#2fabe9')
        self.bt_alterar.place(relx=0.71, rely=0.1, relwidth=0.1, relheight=0.169)
        # Botão de Apagar.
        self.bt_apagar = Button(self.frame_1, text='Apagar', bg='#2fabe9')
        self.bt_apagar.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.169)
        
        # Inicio da aula 03
        # Criação da label e entry do código
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee')
        self.lb_codigo.place(relx=0.01,rely=0.01)
        
        self.entry_codigo = Entry(self.frame_1)
        self.entry_codigo.place(relx=0.013,rely=0.15, relwidth=0.09)
        
        # Criação da label e entry do nome do cliente
        self.lb_nomeCliente = Label(self.frame_1, text='Nome', bg='#dfe3ee')
        self.lb_nomeCliente.place(relx=0.01,rely=0.3)
        
        self.entry_nomeCliente = Entry(self.frame_1)
        self.entry_nomeCliente.place(relx=0.013,rely=0.45, relwidth=0.91)
        
        # Criação da label e entry do telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee')
        self.lb_telefone.place(relx=0.01,rely=0.6)
        
        self.entry_telefone = Entry(self.frame_1)
        self.entry_telefone.place(relx=0.013,rely=0.75, relwidth=0.42)
        
        # Criação da label e entry do cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee')
        self.lb_cidade.place(relx=0.5,rely=0.6)
        
        self.entry_cidade = Entry(self.frame_1)
        self.entry_cidade.place(relx=0.5,rely=0.75, relwidth=0.42)
        


App()