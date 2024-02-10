from tkinter import * # Inicio da aula 01
from tkinter import ttk
import sqlite3

root = Tk()

class Funcs(): # Inicio da aula 07
    def limpa_tela(self):
        self.entry_codigo.delete(0,END)
        self.entry_nomeCliente.delete(0,END)
        self.entry_telefone.delete(0,END)
        self.entry_cidade.delete(0,END)
    
    def connect_db(self): # Inicio da aula 08
        self.conn = sqlite3.connect("clientes.db")
        self.cursor = self.conn.cursor()
        print("conectando ao banco de dados")
    
    def disconnect_db(self):
        self.conn.close()
        print("Banco de dados desconectado")
    
    def montar_Tabela(self):
        self.connect_db()
        # Criação da tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                cod INTEGER PRIMARY KEY,
                nome_cliente CHAR(40) NOT NULL,
                telefone INTEGER(20),
                cidade CHAR(40)
                );
            """)
        self.conn.commit(); print("Banco de dados criado")
        self.disconnect_db()
    
class App(Funcs):
    def __init__(self) -> None:
        self.root = root
        self.tela()
        self.frames_tela()
        self.widgets_frame1()
        self.lista_frame2()
        self.montar_Tabela()
        root.mainloop()
    
    def tela(self):
        self.root.title("Cadastro de Clientes")
        self.root.configure(background='#1e3743')
        self.root.geometry("700x500")
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=550, height=300)
    
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
    
    def widgets_frame1(self): # Inicio da aula 03 // Inicio da aula 05 (estilização de widgets)
        # Botão de limpar.
        self.bt_limpar = Button(self.frame_1, text='Limpar', bg='#2fabe9',
                                bd=2, fg='white', font=('verdana',8,'bold'),
                                    command=self.limpa_tela)
        self.bt_limpar.place(relx=0.21, rely=0.1, relwidth=0.1, relheight=0.169)
        
        # Botão de Busca.
        self.bt_buscar = Button(self.frame_1, text='Buscar', bg='#2fabe9',
                                bd=2, fg='white', font=('verdana',8,'bold'))
        self.bt_buscar.place(relx=0.32, rely=0.1, relwidth=0.1, relheight=0.169)
        
        # Botão Novo.
        self.bt_novo = Button(self.frame_1, text='Novo', bg='#2fabe9',
                                bd=2, fg='white', font=('verdana',8,'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.169)
        
        # Botão de Alterar.
        self.bt_alterar = Button(self.frame_1, text='Alterar', bg='#2fabe9',
                                    bd=2, fg='white', font=('verdana',8,'bold'))
        self.bt_alterar.place(relx=0.71, rely=0.1, relwidth=0.1, relheight=0.169)
        
        # Botão de Apagar.
        self.bt_apagar = Button(self.frame_1, text='Apagar', bg='#2fabe9',
                                bd=2, fg='white', font=('verdana',8,'bold'))
        self.bt_apagar.place(relx=0.82, rely=0.1, relwidth=0.1, relheight=0.169)
        
        # Inicio da aula 04
        # Criação da label e entry do código
        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee',
                                fg='#2fabe9',font=('verdana',8,'bold'))
        self.lb_codigo.place(relx=0.06,rely=0.01)
        
        self.entry_codigo = Entry(self.frame_1)
        self.entry_codigo.place(relx=0.063,rely=0.15, relwidth=0.09)
        
        # Criação da label e entry do nome do cliente
        self.lb_nomeCliente = Label(self.frame_1, text='Nome', bg='#dfe3ee',
                                    fg='#2fabe9',font=('verdana',8,'bold'))
        self.lb_nomeCliente.place(relx=0.06,rely=0.3)
        
        self.entry_nomeCliente = Entry(self.frame_1)
        self.entry_nomeCliente.place(relx=0.063,rely=0.45, relwidth=0.86)
        
        # Criação da label e entry do telefone
        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee',
                                fg='#2fabe9',font=('verdana',8,'bold'))
        self.lb_telefone.place(relx=0.06,rely=0.6)
        
        self.entry_telefone = Entry(self.frame_1)
        self.entry_telefone.place(relx=0.063,rely=0.75, relwidth=0.42)
        
        # Criação da label e entry do cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee',
                                fg='#2fabe9',font=('verdana',8,'bold'))
        self.lb_cidade.place(relx=0.5,rely=0.6)
        
        self.entry_cidade = Entry(self.frame_1)
        self.entry_cidade.place(relx=0.5,rely=0.75, relwidth=0.42)
    
    def lista_frame2(self): # Inicio da aula 6
        # Criação das colunas
        self.lista_clientes = ttk.Treeview(self.frame_2, height=3,
                                            columns=('col1','col2','col3','col4'))
        
        # Definição do cabeçalho
        self.lista_clientes.heading("#0", text='')
        self.lista_clientes.heading("#1", text='Código')
        self.lista_clientes.heading("#2", text='Nome')
        self.lista_clientes.heading("#3", text='Telefone')
        self.lista_clientes.heading("#4", text='Cidade')
        
        # Tamanho de cada coluna
        self.lista_clientes.column("#0", width=1)
        self.lista_clientes.column("#1", width=50)
        self.lista_clientes.column("#2", width=200)
        self.lista_clientes.column("#3", width=125)
        self.lista_clientes.column("#4", width=125)
        
        # Posição da Treeview
        self.lista_clientes.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.85)
        
        # Adicionando uma Scrolbar
        self.scrol_lista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_clientes.configure(yscroll=self.scrol_lista.set)
        self.scrol_lista.place(relx=0.96, rely=0.05, relwidth=0.03, relheight=0.85)

App()