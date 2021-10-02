import sqlite3
from sqlite3.dbapi2 import IntegrityError

usuarios = '''CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        usuario CHARACTER(20) UNIQUE, senha CHARACTER(20))'''

mangas = '''CREATE TABLE IF NOT EXISTS mangas
        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        manga CHARACTER(30),
        id_usuario INTEGER,
        FOREIGN KEY(id_usuario) REFERENCES usuarios(id))'''


# Criação do banco
def criar_db(comando, nome='usuarios.db', ):
    db = sqlite3.connect(nome)
    cursor = db.cursor()
    cursor.execute(comando)
    if __name__ == '__main__':    
        print(f'Banco criado com sucesso! O nome do banco é {nome}')


# Conexão com o banco
def conectar_db(nome='usuarios.db'):
    db = sqlite3.connect(nome)
    cursor = db.cursor()
    return db, cursor


# Buscar todos usuários
def buscar_usuarios():
    db, cursor = conectar_db()
    cursor.execute('SELECT id, usuario, senha FROM usuarios')
    print(cursor.fetchall())


# Alterar nome de usuário
def alterar_usuario(id, usuario):
    db, cursor = conectar_db()
    try:
        cursor.execute(f'UPDATE usuarios SET usuario = "{usuario}" WHERE id = {id}')
        db.commit()
        cursor.close()
        db.close()
        print(f'O nome do usuário referente ao id {id} foi alterado para {usuario}')
    except IntegrityError:
        print(f'ERRO! O nome {usuario} já pertence a outro usuário')


# Alterar senha de usuário
def alterar_senha_usuario(id, senha):
        db, cursor = conectar_db()
        cursor.execute(f'UPDATE usuarios SET senha = "{senha}" WHERE id = {id}')
        db.commit()
        cursor.close()
        db.close()
        print(f'A senha do usuário de id {id} foi alterada com sucesso!')


# Deletar o Banco
def deletar_db(nome='usuarios.db'):
    import os
    os.remove(nome) if os.path.exists(nome) else None
    return print('Banco deletado com sucesso!')


# Registrando usuário
def novo_usuario(usuario, senha):
    db, cursor = conectar_db()
    try:
        cursor.execute(f'INSERT INTO usuarios (usuario, senha) VALUES("{usuario}", "{senha}")')
        db.commit()
        cursor.close()
        db.close()
        print(f'Usuário {usuario} cadastrado com sucesso')
    except IntegrityError:
        print(f'O usuário {usuario} já está cadastrado, tente novamente com outro nome de usuário.')
    

if __name__ == '__main__':
    buscar_usuarios()
    
