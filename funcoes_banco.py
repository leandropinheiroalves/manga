import sqlite3

# Criação do banco
def criar_db(nome='users.db'):
    db = sqlite3.connect(nome)
    cursor = db.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS usuarios '\
        '(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,'\
        'email CHARACTER(64), senha CHARACTER(20))')
    if __name__ == '__main__':    
        print(f'Banco criado com sucesso! O nome do banco é {nome}')

# Deletar o Banco
def deletar_db():
    import os
    os.remove('users.db') if os.path.exists('users.db') else None
    return print('Banco deletado com sucesso!')


# Registrando usuário
def registro():
    criar_db()
    db = sqlite3.connect('users.db')
    cursor = db.cursor()
    lista = list()
    cursor.execute('SELECT * FROM usuarios')
    
    for linha in cursor.fetchall():
        lista.append(linha[1])

    email = input('Digite seu email: ')

    while email in lista:
        print('Esse email já está cadastrado. Por favor digite outro email.')
        email = input('Digite seu email: ')

    senha1 = input('Digite sua senha: ')
    senha2 = input('Confirme sua senha: ')
        
    while senha1 != senha2:
        print('As senhas informadas não são iguais. Tente novamente.')
        senha1 = input('Digite sua senha: ')
        senha2 = input('Confirme sua senha: ')
    
    cursor.execute(f'INSERT INTO usuarios (email, senha)  VALUES("{email}", "{senha1}")')

    db.commit()
    cursor.close()
    db.close()

    return True


if __name__ == '__main__':
    #criar_db()
    #deletar_db()
    #inserir_valores()
    registro()
