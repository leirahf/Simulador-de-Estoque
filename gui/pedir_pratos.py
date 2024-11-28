import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para pedir um prato
def pedir_pratos(voltar_callback):
    def confirmar_pedido():
        prato_selecionado = combo_pratos.get()

        if prato_selecionado == "":
            messagebox.showwarning("Aviso", "Por favor, selecione um prato.")
            return

        # Obter os ingredientes do prato
        cursor.execute("SELECT ingredientes FROM pratos WHERE nome = ?", (prato_selecionado,))
        prato = cursor.fetchone()

        if prato:
            ingredientes_necessarios = prato[0].split(",")  # Ingredientes separados por vírgula
            ingredientes_faltando = []
            
            # Verificar se há quantidade suficiente de cada ingrediente
            for ingrediente in ingredientes_necessarios:
                ingrediente = ingrediente.strip()  # Remover espaços extras
                cursor.execute("SELECT quantidade FROM ingredientes WHERE nome = ?", (ingrediente,))
                ingrediente_info = cursor.fetchone()

                if ingrediente_info:
                    quantidade_estoque = ingrediente_info[0]
                    if quantidade_estoque <= 0:
                        ingredientes_faltando.append(ingrediente)
                    else:
                        # Subtrair 1 unidade do ingrediente no estoque
                        nova_quantidade = quantidade_estoque - 1
                        cursor.execute(
                            "UPDATE ingredientes SET quantidade = ? WHERE nome = ?",
                            (nova_quantidade, ingrediente),
                        )
                        conn.commit()
                else:
                    ingredientes_faltando.append(ingrediente)

            if ingredientes_faltando:
                messagebox.showerror("Erro", f"Faltam ingredientes: {', '.join(ingredientes_faltando)}")
            else:
                messagebox.showinfo("Sucesso", f"Pedido de {prato_selecionado} realizado com sucesso!")
                voltar_callback()  # Voltar para o menu ou outra tela desejada
        else:
            messagebox.showerror("Erro", "Prato não encontrado.")

    # Criar a janela para pedir pratos
    pedir_window = tk.Tk()
    pedir_window.title("Pedir Prato")
    pedir_window.geometry("300x200")

    # Obter lista de pratos
    cursor.execute("SELECT nome FROM pratos")
    pratos = cursor.fetchall()

    lista_pratos = [prato[0] for prato in pratos]  # Converter de lista de tuplas para lista de nomes de pratos

    label_pratos = tk.Label(pedir_window, text="Selecione um prato:")
    label_pratos.pack(pady=10)

    combo_pratos = tk.StringVar(pedir_window)
    combo_pratos.set("")  # Valor padrão
    menu_pratos = tk.OptionMenu(pedir_window, combo_pratos, *lista_pratos)
    menu_pratos.pack(pady=10)

    btn_confirmar = tk.Button(pedir_window, text="Confirmar Pedido", command=confirmar_pedido)
    btn_confirmar.pack(pady=10)

    btn_voltar = tk.Button(pedir_window, text="Voltar", command=pedir_window.destroy)
    btn_voltar.pack(pady=10)

    pedir_window.mainloop()

# Conexão com o banco de dados
conn = sqlite3.connect('banco/estoque.db')  # Ajuste o caminho do banco de dados
cursor = conn.cursor()
