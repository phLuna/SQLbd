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

def atualizar_perfil(alvo, update, info):
    """Esta função atualiza informações de perfis existentes."""
    conn = sqlite3.connect('teste.db')
    cursor = conn.cursor()
    if info == 'NOME':
        cursor.execute(f'UPDATE aluno SET name = {update} WHERE pk = {alvo}')
    if info == 'NASCIMENTO':
        cursor.execute(f'UPDATE aluno SET data_birth = {update} WHERE pk = {alvo}')
    if info == 'FAIXA':
        cursor.execute(f'UPDATE aluno SET belt = "{update}" WHERE pk = {alvo}')
    conn.commit()
    conn.close()
    return 'Aluno atualizado!'

def deletar_perfil(alvo):
    """Deleta perfis da tabela."""
    conn = sqlite3.connect('teste.db')
    cursor = conn.cursor()
    cursor.execute('DELETE from aluno WHERE pk = ?', alvo)
    conn.commit()
    conn.close()
    return 'Perfil deletado!'