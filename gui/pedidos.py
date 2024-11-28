import tkinter as tk
from tkinter import messagebox
import sqlite3

def realizar_pedido():
    prato_selecionado = listbox_pratos.get(tk.ACTIVE)

    conn = sqlite3.connect('../estoque.db')
    cursor = conn.cursor()

    # Obter os ingredientes do prato selecionado
    cursor.execute("""
        SELECT i.nome, pi.quantidade, i.quantidade 
        FROM prato_ingrediente pi
        JOIN ingredientes i ON pi.ingrediente_id = i.id
        JOIN pratos p ON pi.prato_id = p.id
        WHERE p.nome = ?
    """, (prato_selecionado,))
    ingredientes = cursor.fetchall()

    # Verificar disponibilidade dos ingredientes
    for ingrediente in ingredientes:
        if ingrediente[1] > ingrediente[2]:  # quantidade necessária > quantidade no estoque
            messagebox.showerror("Erro", f"Ingrediente insuficiente: {ingrediente[0]}")
            conn.close()
            return

    # Atualizar estoque
    for ingrediente in ingredientes:
        cursor.execute("UPDATE ingredientes SET quantidade = quantidade - ? WHERE nome = ?", 
                       (ingrediente[1], ingrediente[0]))

    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", f"Pedido do prato '{prato_selecionado}' realizado com sucesso!")

def listar_pratos():
    conn = sqlite3.connect('../estoque.db')
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM pratos")
    pratos = cursor.fetchall()
   
