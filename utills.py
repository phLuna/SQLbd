import sqlite3

def abrir_conexao_db():
    conn = sqlite3.connect('teste.db')
    cursor = conn.cursor()
    return cursor, conn

def create_aluno(nome: str, nascimento: int, faixa: str):
    """Esta função cria perfis de acordo com os parâmetros passados."""
    cursor, conn = abrir_conexao_db()
    novo_item = (nome, nascimento, faixa)
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

def atualizar_perfil(operar, alvo):
    """Esta função atualiza informações de perfis existentes."""
    if operar == 'NOME':
        nome_update = input('Insira o novo nome: ').title()
        cursor, conn = abrir_conexao_db()
        update = alvo, nome_update
        cursor.execute(f'UPDATE aluno SET name = ? WHERE pk = ?', update)
    conn.close()
    return 'Aluno atualizado!'