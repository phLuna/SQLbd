import utills


print('Criar/Atualizar/Ler/Excluir')
operar = input('bem vindo! O que deseja fazer no momento? ').upper()
if operar == 'CRIAR':
    nome = input('Insira o nome: ').title()
    nascimento = int(input('Agora, a data de nascimento: '))
    faixa = input('Por último, a faixa: ').capitalize()
    utills.create_aluno(nome, nascimento, faixa)
    print('Aluno criado! ')