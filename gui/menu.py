import tkinter as tk
from ingredientes import gerenciar_ingredientes
from pratos import gerenciar_pratos
from pedir_pratos import pedir_pratos

def abrir_menu():
    def voltar_para_menu():
        abrir_menu()  # Recarrega o menu principal

    menu_window = tk.Tk()
    menu_window.title("Menu Principal")
    menu_window.geometry("300x250")

    label_menu = tk.Label(menu_window, text="Bem-vindo ao Menu!", font=("Arial", 16))
    label_menu.pack(pady=20)

    btn_ingredientes = tk.Button(
        menu_window,
        text="Gerenciar Ingredientes",
        command=lambda: [menu_window.destroy(), gerenciar_ingredientes(voltar_para_menu)],
    )
    btn_ingredientes.pack(pady=10)

    btn_pratos = tk.Button(
        menu_window,
        text="Gerenciar Pratos",
        command=lambda: [menu_window.destroy(), gerenciar_pratos(voltar_para_menu)],
    )
    btn_pratos.pack(pady=10)

    btn_pedir_pratos = tk.Button(
        menu_window,
        text="Pedir Pratos",
        command=lambda: [menu_window.destroy(), pedir_pratos(voltar_para_menu)],
    )
    btn_pedir_pratos.pack(pady=10)

    btn_sair = tk.Button(menu_window, text="Sair", command=menu_window.quit)
    btn_sair.pack(pady=10)

    menu_window.mainloop()
