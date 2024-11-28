import tkinter as tk
from tkinter import messagebox
import sqlite3

# Conectar ao banco de dados
conn = sqlite3.connect('banco/estoque.db')
cursor = conn.cursor()

# Função para gerenciar pratos
def gerenciar_pratos(voltar_callback):
    def criar_prato():
        prato_nome = entry_prato.get()
        ingredientes_str = entry_ingredientes.get()
        
        if prato_nome == "" or ingredientes_str == "":
            messagebox.showwarning("Aviso", "Por favor, insira o nome do prato e os ingredientes.")
            return

        # Inserir o prato na tabela de pratos com os ingredientes como uma string
        cursor.execute("INSERT INTO pratos (nome, ingredientes) VALUES (?, ?)", (prato_nome, ingredientes_str))
        conn.commit()

        messagebox.showinfo("Sucesso", f"Prato {prato_nome} criado com sucesso!")
        entry_prato.delete(0, tk.END)
        entry_ingredientes.delete(0, tk.END)

    # Janela de gerenciamento de pratos
    pratos_window = tk.Tk()
    pratos_window.title("Gerenciar Pratos")
    pratos_window.geometry("400x400")

    label = tk.Label(pratos_window, text="Gerenciar Pratos", font=("Arial", 16))
    label.pack(pady=20)

    # Campo para nome do prato
    label_prato = tk.Label(pratos_window, text="Nome do Prato:")
    label_prato.pack(pady=5)
    entry_prato = tk.Entry(pratos_window)
    entry_prato.pack(pady=5)

    # Campo para ingredientes (separados por vírgula)
    label_ingredientes = tk.Label(pratos_window, text="Ingredientes (separados por vírgula):")
    label_ingredientes.pack(pady=5)
    entry_ingredientes = tk.Entry(pratos_window)
    entry_ingredientes.pack(pady=5)

    # Botão de criar prato
    btn_criar = tk.Button(pratos_window, text="Criar Prato", command=criar_prato)
    btn_criar.pack(pady=10)

    # Botão de voltar
    btn_voltar = tk.Button(pratos_window, text="Voltar ao Menu", command=lambda: [pratos_window.destroy(), voltar_callback()])
    btn_voltar.pack(pady=10)

    pratos_window.mainloop()

