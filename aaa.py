import utills


print('Criar/Atualizar/Ler/Excluir')
operar = input('bem vindo! O que deseja fazer no momento? ').upper()
if operar == 'CRIAR':
    nome = input('Insira o nome: ').title()
    nascimento = int(input('Agora, a data de nascimento: '))
    faixa = input('Por último, a faixa: ').capitalize()
    utills.create_aluno(nome, nascimento, faixa)
    print('Aluno criado!')

elif operar == 'ATUALIZAR':
    operar = input('O que deseja atualizar? [Nome/Nascimento/Faixa]').upper()
    alvo = int(input('De que índice? '))
    utills.atualizar_perfil(operar, alvo)
    print('Atualizado!')

elif operar == 'LER':
    print('Todos/Faixa')
    operar = input('Deseja filtrar? Mostrar... ').upper()
    if operar == 'TODOS':
        alunos = utills.listar_alunos()
        for i in alunos:
            print(i)

    elif operar == 'FAIXA':
        filtro = input('Qual? ')
        perfis = utills.listar_aluno_por_faixas(filtro)
        for perfil in perfis:
            print(perfil)
            
elif operar == 'EXCLUIR':
    print('A')