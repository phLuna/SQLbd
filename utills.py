import sqlite3

def abrir_conexao_db():
    conn = sqlite3.connect('teste.db')
    cursor = conn.cursor()
    return cursor, conn

def create_aluno(nome: str, nascimento: int, faixa: str):
    """Esta função cria perfis de acordo com os parâmetros passados."""
    cursor, conn = abrir_conexao_db()
    novo_item = (nome, nascimento, faixa)  # Substitua 'Novo Item' e 100 pelos valores que deseja inserir
    cursor.execute('INSERT INTO aluno (name, data_birth, belt) VALUES (?, ?, ?)', novo_item)
    conn.commit()
    conn.close()
    return 'Aluno criado!'

def listar_alunos() -> list:
    """Esta função retorna uma lista de tuplas com todos os perfis cadastrados."""
    cursor, conn = abrir_conexao_db()
    cursor.execute('SELECT * FROM aluno')
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def listar_aluno_por_faixas(faixa: str) -> list:
    """Esta função retorna perfis, filtrados por suas faixas."""
    cursor, conn = abrir_conexao_db()
    cursor.execute(f'SELECT * FROM aluno WHERE belt = {faixa}')
    resultados = cursor.fetchall()
    conn.close()
    return resultados

def atualizar_perfil():
    """Esta função atualiza informações de perfis existentes."""
    operar = input('O que deseja atualizar? [Nome/Nascimento/Faixa]').upper()
    alvo = input('De quem? ').title()
    if operar == 'NOME':
        nome_update = input('Insira o novo nome: ').title()
        cursor, conn = abrir_conexao_db()
        atualizacao = nome_update
        cursor.execute(f'UPDATE aluno SET name = {atualizacao} WHERE nome = {alvo}', atualizacao)
    conn.close()
    return 'Aluno atualizado!'

alunos = listar_alunos()
print(alunos)
print('-' * 15)
atualizar_perfil()
alunos1 = listar_alunos()