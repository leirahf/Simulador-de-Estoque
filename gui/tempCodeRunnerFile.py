import tkinter as tk
from tkinter import messagebox
import sqlite3

# Função para abrir o menu
def abrir_menu():
    menu_window = tk.Tk()
    menu_window.title("Menu Principal")
    menu_window.geometry("300x250")

    label_menu = tk.Label(menu_window, text="Bem-vindo ao Menu!", font=("Arial", 16))
    label_menu.pack(pady=20)

    # Funções para as opções do menu
    def gerenciar_ingredientes():
        print("Abrindo gerenciamento de ingredientes...")

    def gerenciar_pratos():
        print("Abrindo gerenciamento de pratos...")

    # Botões do menu
    btn_ingredientes = tk.Button(menu_window, text="Gerenciar Ingredientes", command=gerenciar_ingredientes)
    btn_ingredientes.pack(pady=10)

    btn_pratos = tk.Button(menu_window, text="Gerenciar Pratos", command=gerenciar_pratos)
    btn_pratos.pack(pady=10)

    btn_sair = tk.Button(menu_window, text="Sair", command=menu_window.quit)
    btn_sair.pack(pady=10)

    menu_window.mainloop()

# Função para fazer login
def login():
    def autenticar():
        username = entry_username.get()
        password = entry_password.get()
        if not username or not password:
            messagebox.showwarning("Aviso", "Por favor, preencha ambos os campos.")
            return

        try:
            cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (username, password))
            usuario = cursor.fetchone()
            if usuario:
                messagebox.showinfo("Sucesso", "Login bem-sucedido!")
                root.destroy()
                abrir_menu()  # Aqui abre o menu principal
            else:
                messagebox.showerror("Erro", "Nome de usuário ou senha incorretos.")
        except sqlite3.Error as e:
            messagebox.showerror("Erro", f"Erro ao verificar o usuário: {e}")

    def registrar():
        # Função de registrar novo usuário
        def criar_usuario():
            novo_username = entry_new_username.get()
            nova_senha = entry_new_password.get()
            if not novo_username or not nova_senha:
                messagebox.showwarning("Aviso", "Por favor, preencha ambos os campos.")
                return

            try:
                cursor.execute("INSERT INTO usuarios (username, password) VALUES (?, ?)", (novo_username, nova_senha))
                conn.commit()
                messagebox.showinfo("Sucesso", "Usuário registrado com sucesso!")
                registrar_window.destroy()
            except sqlite3.Error as e:
                messagebox.showerror("Erro", f"Erro ao registrar usuário: {e}")

        # Criar uma nova janela para registro
        registrar_window = tk.Toplevel()
        registrar_window.title("Registrar Novo Usuário")
        registrar_window.geometry("300x200")

        label_new_username = tk.Label(registrar_window, text="Novo Nome de Usuário:")
        label_new_username.pack(pady=5)
        entry_new_username = tk.Entry(registrar_window)
        entry_new_username.pack(pady=5)

        label_new_password = tk.Label(registrar_window, text="Nova Senha:")
        label_new_password.pack(pady=5)
        entry_new_password = tk.Entry(registrar_window, show="*")
        entry_new_password.pack(pady=5)

        btn_criar_usuario = tk.Button(registrar_window, text="Registrar", command=criar_usuario)
        btn_criar_usuario.pack(pady=10)

    # Janela de login
    root = tk.Tk()
    root.title("Login")
    root.geometry("300x250")

    # Campos de login
    label_username = tk.Label(root, text="Nome de Usuário:")
    label_username.pack(pady=5)
    entry_username = tk.Entry(root)
    entry_username.pack(pady=5)

    label_password = tk.Label(root, text="Senha:")
    label_password.pack(pady=5)
    entry_password = tk.Entry(root, show="*")
    entry_password.pack(pady=5)

    # Botão de login
    btn_login = tk.Button(root, text="Login", command=autenticar)
    btn_login.pack(pady=10)

    # Botão de registrar novo usuário
    btn_registrar = tk.Button(root, text="Registrar Novo Usuário", command=registrar)
    btn_registrar.pack(pady=10)

    # Conexão com o banco de dados
    conn = sqlite3.connect("banco/estoque.db")  # Ajuste o caminho do banco de dados conforme necessário
    cursor = conn.cursor()

    root.mainloop()

# Iniciar o aplicativo de login
if __name__ == "__main__":
    login()
