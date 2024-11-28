import tkinter as tk
from tkinter import messagebox
import sqlite3

def adicionar_ingrediente():
    nome = entry_nome.get()
    quantidade = int(entry_quantidade.get())

    conn = sqlite3.connect('../estoque.db')
    cursor = conn.cursor()
    try:
        cursor.execute("INSERT INTO ingredientes (nome, quantidade) VALUES (?, ?)", (nome, quantidade))
        conn.commit()
        messagebox.showinfo("Sucesso", f"Ingrediente '{nome}' adicionado com sucesso!")
    except sqlite3.IntegrityError:
        messagebox.showerror("Erro", f"O ingrediente '{nome}' já existe.")
    conn.close()

def listar_ingredientes():
    conn = sqlite3.connect('../estoque.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome, quantidade FROM ingredientes")
    ingredientes = cursor.fetchall()
    conn.close()

    listbox.delete(0, tk.END)
    for ingrediente in ingredientes:
        listbox.insert(tk.END, f"{ingrediente[0]}: {ingrediente[1]} unidades")

def gerenciar_estoque():
    global entry_nome, entry_quantidade, listbox

    root = tk.Tk()
    root.title("Gerenciar Estoque")

    tk.Label(root, text="Nome do Ingrediente:").grid(row=0, column=0)
    entry_nome = tk.Entry(root)
    entry_nome.grid(row=0, column=1)

    tk.Label(root, text="Quantidade:").grid(row=1, column=0)
    entry_quantidade = tk.Entry(root)
    entry_quantidade.grid(row=1, column=1)

    btn_adicionar = tk.Button(root, text="Adicionar", command=adicionar_ingrediente)
    btn_adicionar.grid(row=2, column=0, columnspan=2)

    btn_listar = tk.Button(root, text="Listar Estoque", command=listar_ingredientes)
    btn_listar.grid(row=3, column=0, columnspan=2)

    listbox = tk.Listbox(root, width=40)
    listbox.grid(row=4, column=0, columnspan=2)

    root.mainloop()
