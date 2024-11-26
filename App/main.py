from tkinter import *
from tkinter import ttk

from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter ,A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import SimpleDocTemplate, Image

import webbrowser

import sqlite3

from os import path, mkdir, rename, remove


root = Tk()


class Relatorios():
  def printClient(self):
    if not path.exists("./Relatorios"):
      mkdir("Relatorios")
    
    # realizar busca por nomes identicos de arquivos e substituir o antigo pelo novo
    try:
      rename(
        f"cliente_{'_'.join(self.rel_nome.title().split())}.pdf",
        f"Relatorios/cliente_{'_'.join(self.rel_nome.title().split())}.pdf"
      )
      print("\narquivo movido")
      
    except:
      remove(
        f"Relatorios/cliente_{'_'.join(self.rel_nome.title().split())}.pdf"
        )
      print('\narquivo removido')
      
      rename(
        f"cliente_{'_'.join(self.rel_nome.title().split())}.pdf",
        f"Relatorios/cliente_{'_'.join(self.rel_nome.title().split())}.pdf"
      )
      
    finally:
      webbrowser.open(
        f"D:/17phr/Documents/PROGRAMACAO!/GitHub/GUI_tkinter/Relatorios/cliente_{'_'.join(self.rel_nome.title().split())}.pdf"
      )
      
      print("final\n")    
  
  def geraRelatorioCliente(self):
    self.rel_codigo = self.entry_codigo.get()
    self.rel_nome = self.entry_nome.get()
    self.rel_telefone = self.entry_telefone.get()
    self.rel_cidade = self.entry_cidade.get()
    
    # Se todos os dados do cliente não estiverem preenchidos, o relatório não irá ser criado.
    rel_dados = [self.rel_codigo, self.rel_nome, self.rel_telefone, self.rel_cidade]
    
    if rel_dados:
      # Cria o aruqivo PDF com o prefixo "clente_" mais o nome do cliente e a extensão ".pdf" no tamanho de página "A4".
      self.c = canvas.Canvas(f"cliente_{'_'.join(self.rel_nome.title().split())}.pdf",pagesize=A4)
      
      # Define a fonte como "Helvetica-Bold" com o tamanho 24 e escreve o titulo da página na posição desejada. 
      self.c.setFont("Helvetica-Bold",24)
      self.c.drawString(200, 790, "Ficha de Cliente")
      
      self.c.setFont("Helvetica-Bold",18)
      self.c.drawString(50,720,"Código: ")
      self.c.drawString(50,690,"Nome: ")
      self.c.drawString(50,660,"Telefone: ")
      self.c.drawString(50,630,"Cidade: ")
      
      # Define a fonte como "Helvetica-Bold" com o tamanho 18 e escreve o as informações do usuário ao lado da escrita anterior.
      self.c.setFont("Helvetica",18)
      self.c.drawString(150,720, self.rel_codigo)
      self.c.drawString(150,690, self.rel_nome)
      self.c.drawString(150,660, self.rel_telefone)
      self.c.drawString(150,630, self.rel_cidade)
      
      # Cria uma linha que começa na possição x=20 com 555px de largura, no y=600 com 2px de altura e com preenchimento atívo.
      self.c.rect(20, 600, 555, 2, fill=True)
      
      self.c.showPage()
      self.c.save()
      
      # mover o arquivo do cliente para o diretório Relatorios.
      self.printClient()
    
    else: print("não foi possivel criar um relatório, pois o nome do cliente não existe!")
    
class Funcs: # Inicio da aula 07
  def limpa_tela(self):
    self.entry_codigo.delete(0,END)
    self.entry_nome.delete(0,END)
    self.entry_telefone.delete(0,END)
    self.entry_cidade.delete(0,END)
  
  def connect_db(self): # Inicio da aula 08
    self.conn = sqlite3.connect("App/clientes.sqlite3")
    self.cursor = self.conn.cursor()
    print("conectando ao banco de dados")
  
  def disconnect_db(self):
    self.conn.close()
    print("Banco de dados desconectado")
  
  def create_table(self):
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
  
  def variaveis(self):
    self.codigo = self.entry_codigo.get()
    self.nome_cliente = self.entry_nome.get()
    self.telefone = self.entry_telefone.get()
    self.cidade = self.entry_cidade.get()
  
  def add_client(self): # Inicio da aula 09
    self.variaveis()
    
    self.connect_db()
    self.cursor.execute("""
      INSERT INTO clientes(nome_cliente, telefone,cidade)
          VALUES (?,?,?);
      """, (self.nome_cliente, self.telefone, self.cidade))
    self.conn.commit()
    self.disconnect_db()
    
    self.select_lista()
    self.limpa_tela()
  
  def select_lista(self):
    self.lista_clientes.delete(*self.lista_clientes.get_children())
    
    self.connect_db()
    lista = self.cursor.execute("""
          SELECT cod, nome_cliente, telefone, cidade FROM clientes
          ORDER BY nome_cliente ASC;
      """)
    
    for i in lista:
      self.lista_clientes.insert("", END, values=i)
    
    self.disconnect_db()
  
  def OnDoubleClik(self,event): # Inicio da aula 10
    self.limpa_tela()
    self.lista_clientes.selection()
    
    for n in self.lista_clientes.selection():
      col1, col2, col3, col4 = self.lista_clientes.item(n, 'values')
      
      self.entry_codigo.insert(END,col1)
      self.entry_nome.insert(END,col2)
      self.entry_telefone.insert(END,col3)
      self.entry_cidade.insert(END,col4)
  
  def del_client (self):
    self.variaveis()
    self.connect_db()
    
    self.cursor.execute("""
          DELETE FROM clientes WHERE cod = ?
      """, (self.codigo))
    self.conn.commit()
    
    self.disconnect_db()
    self.limpa_tela()
    self.select_lista()
  
  def change_client(self): # Inicio da aula 11
    self.variaveis()
    self.connect_db()
    self.cursor.execute("""
      UPDATE
          clientes
      SET
          nome_cliente = ?,
          telefone = ?,
          cidade = ?
      WHERE
          cod = ?;
      """,(
      self.nome_cliente,
      self.telefone,
      self.cidade,
      self.codigo
    ))
    self.conn.commit()
    self.disconnect_db()
    self.select_lista()
    self.limpa_tela()
  
  def search_client(self):
    ...
  
  
class App(Funcs,Relatorios):# Inicio da aula 01
  def __init__(self) -> None:
    self.root = root
    self.tela()
    self.frames_tela()
    self.widgets_frame1()
    self.lista_frame2()
    self.create_table()
    self.select_lista()
    self.menus()
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
                            bd=2, fg='white', font=('verdana',8,'bold'),
                            command=self.search_client)
    self.bt_buscar.place(relx=0.32, rely=0.1, relwidth=0.1, relheight=0.169)
    
    # Botão Novo.
    self.bt_novo = Button(self.frame_1, text='Novo', bg='#2fabe9',
                            bd=2, fg='white', font=('verdana',8,'bold'),
                                command=self.add_client)
    self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.169)
    
    # Botão de Alterar.
    self.bt_alterar = Button(self.frame_1, text='Alterar', bg='#2fabe9',
                                bd=2, fg='white', font=('verdana',8,'bold'),
                                command=self.change_client)
    self.bt_alterar.place(relx=0.71, rely=0.1, relwidth=0.1, relheight=0.169)
    
    # Botão de Apagar.
    self.bt_apagar = Button(self.frame_1, text='Apagar', bg='#2fabe9',
                            bd=2, fg='white', font=('verdana',8,'bold'),
                            command=self.del_client)
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
    
    self.entry_nome = Entry(self.frame_1)
    self.entry_nome.place(relx=0.063,rely=0.45, relwidth=0.86)
    
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
    
    self.lista_clientes.bind("<Double-1>", self.OnDoubleClik)
  
  def menus(self): # Inicio da aula 12
    menubar = Menu(self.root)
    self.root.config(menu=menubar)
    
    menu_opcoes = Menu(menubar)
    menu_relatorios= Menu(menubar)
    
    def Quit():
        self.root.destroy()
    
    menubar.add_cascade(label='Opções', menu=menu_opcoes)
    menubar.add_cascade(label='Relatorios', menu=menu_relatorios)
    
    menu_opcoes.add_command(label='Sair', command=Quit)
    menu_opcoes.add_command(label='Limpar tela', command=self.limpa_tela)
    
    menu_relatorios.add_command(label='Ficha do cliente',
                                command=self.geraRelatorioCliente)




App()
