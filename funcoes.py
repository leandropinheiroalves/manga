import sqlite3
from sqlite3.dbapi2 import IntegrityError

query_usuarios = '''CREATE TABLE IF NOT EXISTS usuarios 
        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        usuario CHARACTER(20) UNIQUE, senha CHARACTER(20))'''

query_mangas = '''CREATE TABLE IF NOT EXISTS mangas
        (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        manga CHARACTER(30),
        id_usuario INTEGER NOT NULL,
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


# fechar conexões com o banco
def fechar_db(db, cursor):
    db.commit()
    cursor.close()
    db.close()

# Deletar o Banco
def deletar_db(nome='usuarios.db'):
    import os
    os.remove(nome) if os.path.exists(nome) else None
    print('Banco deletado com sucesso!')


# Registrando novo usuário
def novo_usuario(usuario, senha):
    db, cursor = conectar_db()
    try:
        cursor.execute(f'INSERT INTO usuarios (usuario, senha) VALUES("{usuario}", "{senha}")')
        fechar_db(db, cursor)
        print(f'Usuário {usuario} cadastrado com sucesso')
    except IntegrityError:
        print(f'O usuário {usuario} já está cadastrado, tente novamente com outro nome de usuário.')


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
        fechar_db(db, cursor)
        print(f'O nome do usuário referente ao id {id} foi alterado para {usuario}')
    except IntegrityError:
        print(f'ERRO! O nome {usuario} já pertence a outro usuário')


# Alterar senha de usuário
def alterar_senha_usuario(id, senha):
        db, cursor = conectar_db()
        cursor.execute(f'UPDATE usuarios SET senha = "{senha}" WHERE id = {id}')
        fechar_db(db, cursor)
        print(f'A senha do usuário de id {id} foi alterada com sucesso!')


# Excluir usuário
def excluir_usuario(id):
    db, cursor = conectar_db()
    cursor.execute(f'DELETE FROM usuarios WHERE id = {id}')
    fechar_db(db, cursor)
    print(f'O usuário com o id {id} foi excluído')


# Registrando novo mangá
def novo_manga(manga, usuario):
    db, cursor = conectar_db()
    cursor.execute(f'''INSERT INTO mangas (manga, id_usuario) 
        VALUES("{manga}", (SELECT id FROM usuarios WHERE usuario = "{usuario}"))''')
    fechar_db(db, cursor)
    print(f'Manga "{manga}" adicionado aos mangás do usuário {usuario}.')


# Buscar todos mangas
def buscar_mangas():
    db, cursor = conectar_db()
    cursor.execute('SELECT * FROM mangas')
    print(cursor.fetchall())


# Buscas todos mangas por nome de usuario
def manga_por_usuario(usuario):
    db, cursor = conectar_db()
    cursor.execute(f'''SELECT manga FROM mangas 
        WHERE id_usuario = (SELECT id FROM usuarios WHERE usuario="{usuario}")''')
    print(cursor.fetchall())


# Alterar mangá
def alterar_manga(manga, novo_manga, usuario):
    db, cursor = conectar_db()
    cursor.execute(f'''UPDATE mangas SET manga = "{novo_manga}"
        WHERE manga = "{manga}" 
        AND id_usuario = (SELECT id FROM usuarios WHERE usuario = "{usuario}")''')
    fechar_db(db, cursor)
    mensagem = f'O mangá "{manga}" do usuário {usuario} foi alterado para '
    mensagem += f'{novo_manga} com sucesso.'
    print(mensagem)


# Remover mangá
def remover_manga(manga, usuario):
    db, cursor = conectar_db()
    cursor.execute(f'''DELETE FROM mangas WHERE manga = "{manga}"
        AND id_usuario = (SELECT id FROM usuarios WHERE usuario = "{usuario}")''')
    fechar_db(db, cursor)
    print(f'O mangá "{manga}" da lista do usuário {usuario} foi excluído com sucesso.')


if __name__ == '__main__':
    buscar_mangas()
    buscar_usuarios()
