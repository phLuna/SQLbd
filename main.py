from fastapi import FastAPI
import uvicorn
import utills

app = FastAPI()

@app.get("/consultar_todos")
def consultar_cadastros():
    alunos = utills.listar_alunos()
    return {'Cadastros': alunos}

@app.post("/criar_perfil")
def criar_perfil(nome: str, nascimento: int, faixa: str):
    utills.create_aluno(nome, nascimento, faixa)
    return {'response': f"O perfil de {nome}, nascido em {nascimento} foi feito e salvo com sucesso!"}

@app.patch("/atualizar")
def atualizar_item(alvo, info, update):
    utills.atualizar_perfil(alvo, update, info)
    return {'response': f"O item foi atualizado!"}

@app.delete("/deletar")
def deletar_perfil(alvo):
    utills.deletar_perfil(alvo)
    return {'response': f"O alvo cuja PK é {alvo} foi deletado com sucesso!"}

if __name__ == '__main__':
    uvicorn.run(app)

#Rest: get (consultas), post (cadastro), pacht/put (atualizar), delete(deletar)