import sqlite3
from tkinter import Tk, Label, Button, Entry, Listbox, StringVar, messagebox


class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Gerenciamento de Estoque")

        # Campo para adicionar ingredientes
        Label(root, text="Nome do Ingrediente:").grid(row=0, column=0, padx=10, pady=10)
        self.ingrediente_nome = StringVar()
        Entry(root, textvariable=self.ingrediente_nome).grid(row=0, column=1, padx=10)

        Label(root, text="Quantidade:").grid(row=1, column=0, padx=10)
        self.ingrediente_quantidade = StringVar()
        Entry(root, textvariable=self.ingrediente_quantidade).grid(row=1, column=1, padx=10)

        Button(root, text="Adicionar Ingrediente", command=self.adicionar_ingrediente).grid(row=2, column=0, columnspan=2, pady=10)

        # Lista de ingredientes
        self.lista_ingredientes = Listbox(root, width=50, height=10)
        self.lista_ingredientes.grid(row=3, column=0, columnspan=2, pady=10)
        self.carregar_ingredientes()

    def adicionar_ingrediente(self):
        nome = self.ingrediente_nome.get()
        quantidade = self.ingrediente_quantidade.get()

        if not nome or not quantidade.isdigit():
            messagebox.showerror("Erro", "Insira um nome válido e uma quantidade numérica.")
            return

        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()

        try:
            cursor.execute("INSERT INTO ingredientes (nome, quantidade) VALUES (?, ?)", (nome, int(quantidade)))
            conn.commit()
            messagebox.showinfo("Sucesso", f"Ingrediente '{nome}' adicionado!")
        except sqlite3.IntegrityError:
            messagebox.showerror("Erro", f"O ingrediente '{nome}' já existe.")
        finally:
            conn.close()

        self.carregar_ingredientes()

    def carregar_ingredientes(self):
        self.lista_ingredientes.delete(0, 'end')

        conn = sqlite3.connect('estoque.db')
        cursor = conn.cursor()

        cursor.execute("SELECT nome, quantidade FROM ingredientes")
        for ingrediente in cursor.fetchall():
            self.lista_ingredientes.insert('end', f"{ingrediente[0]}: {ingrediente[1]} unidades")

        conn.close()


if __name__ == "__main__":
    root = Tk()
    app = App(root)
    root.mainloop()

