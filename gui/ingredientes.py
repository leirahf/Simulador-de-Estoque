import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('banco/estoque.db')
cursor = conn.cursor()

# Função para gerenciar ingredientes
def gerenciar_ingredientes(voltar_callback):
    def adicionar_ingrediente():
        ingrediente = entry_ingrediente.get()
        quantidade = entry_quantidade.get()

        if not ingrediente or not quantidade.isdigit():
            messagebox.showwarning("Aviso", "Por favor, insira o ingrediente e a quantidade corretamente.")
            return

        quantidade = int(quantidade)

        cursor.execute("INSERT OR IGNORE INTO ingredientes_estoque (ingrediente, quantidade) VALUES (?, ?)", (ingrediente, quantidade))
        conn.commit()

        messagebox.showinfo("Sucesso", f"Ingrediente {ingrediente} adicionado ao estoque com {quantidade} unidades.")
        entry_ingrediente.delete(0, tk.END)
        entry_quantidade.delete(0, tk.END)

        atualizar_lista_ingredientes()

    def atualizar_lista_ingredientes():
        listbox_ingredientes.delete(0, tk.END)
        cursor.execute("SELECT ingrediente, quantidade FROM ingredientes_estoque")
        ingredientes = cursor.fetchall()
        for ingrediente, quantidade in ingredientes:
            listbox_ingredientes.insert(tk.END, f"{ingrediente}: {quantidade} unidades")

    # Janela de gerenciamento de ingredientes
    ingredientes_window = tk.Tk()
    ingredientes_window.title("Gerenciar Ingredientes")
    ingredientes_window.geometry("400x400")

    label = tk.Label(ingredientes_window, text="Gerenciar Ingredientes", font=("Arial", 16))
    label.pack(pady=20)

    # Campo para adicionar ingrediente
    label_ingrediente = tk.Label(ingredientes_window, text="Nome do Ingrediente:")
    label_ingrediente.pack(pady=5)
    entry_ingrediente = tk.Entry(ingredientes_window)
    entry_ingrediente.pack(pady=5)

    label_quantidade = tk.Label(ingredientes_window, text="Quantidade:")
    label_quantidade.pack(pady=5)
    entry_quantidade = tk.Entry(ingredientes_window)
    entry_quantidade.pack(pady=5)

    # Botão de adicionar ingrediente
    btn_adicionar = tk.Button(ingredientes_window, text="Adicionar Ingrediente", command=adicionar_ingrediente)
    btn_adicionar.pack(pady=10)

    # Lista de ingredientes
    listbox_ingredientes = tk.Listbox(ingredientes_window, width=40, height=10)
    listbox_ingredientes.pack(pady=10)
    atualizar_lista_ingredientes()

    # Botão de voltar
    btn_voltar = tk.Button(ingredientes_window, text="Voltar ao Menu", command=lambda: [ingredientes_window.destroy(), voltar_callback()])
    btn_voltar.pack(pady=10)

    ingredientes_window.mainloop()
