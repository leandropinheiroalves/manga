"""
A aula foi feita utilizando o PostgreSQL, então algumas adaptações foram necessárias para o uso em SQLite3.

A linguagem SQL não é case sensitive, não destinguindo entre maísculas e minúsculas.
Dessa forma os comandos funcionam das duas maneiras, no entanto, algumas empresas costuma utilizar os comandos SQL em maísculos, para melhorar a legibilidade, ainda mais ao utilizar linguagem SQL em conjunto com outras linguagens
"""

import sqlite3

# Conectando com o banco de dados teste.db e criando cursor
db = sqlite3.connect('aula_SQL/teste.db')
cursor = db.cursor()
    

def buscar(men):
    cursor.execute(men)
    return print(cursor.fetchall())


# Criando tabela TB_FUNC no banco de dados
tabela1 = '''CREATE TABLE TB_FUNC
        (id integer NOT NULL,
        estado_civil character varying(30),
        grau_instrucao character varying(30),
        numero_filhos integer,
        salario_hora double precision,
        idade integer,
        reg_procedencia character varying(30),
        PRIMARY KEY (id))'''
def criar_tabela(men):
    cursor.execute(men)
    print('Banco criado com sucesso!')

########## SELECT ##########
# Usando SELECT - seleciona os dados dentro do banco
mostrar_dados = 'SELECT * FROM TB_FUNC'
    
# Usando LIMIT - limita o número de dados selecionados
dados_limitados = 'SELECT * FROM TB_FUNC limit 10'
    
# Usando OFFSET - limita o número de dados selecionados apartir de uma posicão
offset = 'SELECT * FROM TB_FUNC LIMIT 10 OFFSET 10'
   
# Usando DISTINCT - remove os valores duplicados da seleção, só mostrando os valores únicos
dados_distintos = 'SELECT DISTINCT numero_filhos FROM TB_FUNC '
   
# Usando WHERE - só seleciona os dados que atenderem a condição
dados_por_idade = 'SELECT * FROM TB_FUNC WHERE idade = 30'
    
# Usando COUNT - conta o número de registro
contador = 'SELECT COUNT(*) FROM TB_FUNC'
  
# Operadores de comparação
# [1] - (=) : conta a quantidade de registro de pessoas com idade igual a 40
# [2] - (!=): conta a quantidade de registro de pessoas com idade diferente de 40
# [3] - (>) : conta a quantidade de registro de pessoas com idade maior que 40
# [4] - (>=): conta a quantidade de registro de pessoas com idade maior ou igual a 40
# [5] - (<) : conta a quantidade de registro de pessoas com idade menor que 40
# [6] - (<=): conta a quantidade de registro de pessoas com idade menor ou igual a 40
igual = 'SELECT COUNT(*) FROM TB_FUNC WHERE idade = 40'
diferente = 'SELECT COUNT(*) FROM TB_FUNC WHERE idade != 40'
maior = 'SELECT COUNT(*) FROM TB_FUNC WHERE idade > 40'
maior_igual = 'SELECT COUNT(*) FROM TB_FUNC WHERE idade >= 40'
menor = 'SELECT COUNT(*) FROM TB_FUNC WHERE idade < 40'
menor_igual = 'SELECT COUNT(*) FROM TB_FUNC WHERE idade <= 40'
    
# Operadores Lógicos - Possibilitam concatenar as operações de comparação
# AND   : retorna os dados se todos eles forem verdadeiros para todas as operação lógicas 
# OR    : retorna qualquer dado que for verdadeiro dentro das operação lógicas 
dados_e = 'SELECT * FROM TB_FUNC WHERE idade < 30 AND estado_civil = "viuvo"'
dados_ou = 'SELECT * FROM TB_FUNC WHERE idade < 30 OR estado_civil = "viuvo"'
    
# Operador de comparação BETWEEN - busca valores entre dois valores, incluindo os valores
dados_entre = 'SELECT * FROM TB_FUNC WHERE idade BETWEEN 30 and 35'

# Operador de comparação LIKE - busca valores que contenham algum dos valores passados quando utilizado com o coringa (%)
dados_parecidos = 'SELECT * FROM TB_FUNC WHERE grau_instrucao LIKE "%medio"'
    
# Operador de comparação IN - busca valores dentro de um conjunto
dados_dentro = 'SELECT * FROM TB_FUNC WHERE idade IN (20, 30, 40, 50)'

# Operador IS NULL - busca valores nulos
nulos = 'SELECT * FROM TB_FUNC where numero_filhos IS NULL'

# Usando UPDATE - Altera um valor já existente
def atualizar():
    cursor.execute('UPDATE TB_FUNC SET numero_filhos = NULL WHERE numero_filhos = "NA" ')
    db.commit()

# Usando DELETE - apaga a tabela
def deletar():
    cursor.execute('DELETE FROM TB_FUNC WHERE numero_filhos = "NA" ')
    db.commit()

# Usando INSERT - insere valores na tabela
valor_a_ser_adicionaro = '''INSERT INTO TB_FUNC
    (ID, estado_civil, grau_instrucao, numero_filhos, 
    salario_hora, idade, reg_procedencia) 
    VALUES (38, "casado", "ensino medio", 3, 4.50, 30, "capital"'''

def inserir(men):
    cursor.execute(men)
    print('Dados inseridos na tabela com sucesso!')
    db.commit()

# Usando ORDER BY - organiza os valores da tabela, por padrão ordena de forma crescente(ASC)
ordenados = 'SELECT * FROM TB_FUNC ORDER BY salario_hora DESC, reg_procedencia DESC'

# Usando as funções:
# MIN   : mostra o valor minimo
# MAX   : mostra o valor maximo
# AVG   : mostra a média
# COUNT : total de registros
# SUM   : soma os registros
minimo = 'SELECT MIN(salario_hora) FROM TB_FUNC'
maximo = 'SELECT MAX(salario_hora) FROM TB_FUNC'
media = 'SELECT AVG(salario_hora) FROM TB_FUNC'
total_registros = 'SELECT COUNT(*) FROM TB_FUNC'
soma = 'SELECT SUM(salario_hora) FROM TB_FUNC'

# Usando GROUP BY - agrupa os valores conforme um parametro
media_procedencia = 'SELECT ROUND(AVG(salario_hora)), reg_procedencia FROM TB_FUNC GROUP BY reg_procedencia'

# Exercício 1
# /* Crie uma instrução SQL que retorne a média de idade, número de filhos e grau de instrução dos funcionários cujo salario_hora estiver acima da média de todos os funcionário.
# 
# Retorne os dados somente de funcionários da capital e estado civil casado, com ordem decrescente da média de idade. */
exercicio1 = '''SELECT ROUND(AVG(idade)), numero_filhos, grau_instrucao 
FROM TB_FUNC
WHERE salario_hora > (SELECT AVG(salario_hora) FROM TB_FUNC)
    AND estado_civil = 'casado'
    AND reg_procedencia = 'capital'
GROUP BY numero_filhos, grau_instrucao
ORDER BY ROUND(AVG(idade)) DESC
'''

# Exercício 2
# /* Retorne todos os registros dos funcionários com 2 filhos. */
exercicio2 = 'SELECT * FROM TB_FUNC WHERE cast(numero_filhos as INTEGER) = 2'

# Exercício 3
# /* Juntar dados de tabelas diferentes, Retorne a média de salário por estado */
tabela2 = '''CREATE TABLE TB_ENDERECO
(
    "id_end" integer NOT NULL,
    "rua" character varying(30),
    "numero" character varying(30),
    "bairro" character varying(30),
    "cep" character varying(10),
    "estado" character varying(30),
    "pais" character varying(30),
    "id_func" integer,
    PRIMARY KEY ("id_end")
)'''

dados1 = '''INSERT INTO TB_ENDERECO(
	"id_end", "rua", "numero", "bairro", "cep", "estado", "pais", "id_func")
	VALUES (1001, 'Jaguar', 40, 'Tijuca', '24239-900', 'Rio de Janeiro', 'Brasil', 2)'''

dados2 = '''INSERT INTO TB_ENDERECO(
	"id_end", "rua", "numero", "bairro", "cep", "estado", "pais", "id_func")
	VALUES (1002, 'Mercedes Benz', 140, 'Centro', '12098-900', 'Minas Gerais', 'Brasil', 6)'''

dados3 = '''INSERT INTO TB_ENDERECO(
	"id_end", "rua", "numero", "bairro", "cep", "estado", "pais", "id_func")
	VALUES (1003, 'BMW', 20, 'Tijuca', '23232-900', 'Rio de Janeiro', 'Brasil', 3)'''
	
dados4 = '''INSERT INTO TB_ENDERECO(
	"id_end", "rua", "numero", "bairro", "cep", "estado", "pais", "id_func")
	VALUES (1004, 'Ferrari', 32, 'Centro', '99872-900', 'Minas Gerais', 'Brasil', 11)'''

dados5 = '''INSERT INTO TB_ENDERECO(
	"id_end", "rua", "numero", "bairro", "cep", "estado", "pais", "id_func")
	VALUES (1005, 'McLaren', 45, 'Centro', '43982-900', 'Minas Gerais', 'Brasil', 17)'''

# Exercício 3
# /* Retorne a média de salário por estado */

exercicio3 = '''SELECT ROUND(AVG(f.salario_hora)), e.estado
FROM TB_FUNC f, TB_ENDERECO e
WHERE f.id = e.id_func
GROUP BY e.estado
'''
