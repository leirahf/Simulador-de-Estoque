import sqlite3
import os

# Caminho para o banco de dados
db_path = 'banco/estoque.db'

# Cria a pasta 'banco' se não existir
if not os.path.exists('banco'):
    os.makedirs('banco')

# Conecta ao banco de dados (a pasta já está criada)
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Criação da tabela de ingredientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS ingredientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    quantidade INTEGER NOT NULL
)
''')

# Criação da tabela de pratos
cursor.execute('''
CREATE TABLE IF NOT EXISTS pratos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE NOT NULL,
    ingredientes TEXT NOT NULL
)
''')

# Criação da tabela de usuários
cursor.execute('''
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
''')

conn.commit()
conn.close()

print("Banco de dados e tabelas criados com sucesso!")
