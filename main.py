from fastapi import FastAPI
import uvicorn
import utills

app = FastAPI()

@app.get("/consultar_todos")
def consultar_cadastros():
    alunos = utills.listar_alunos()
    return {'Cadastros': alunos}

@app.post("/items/")
def criar_perfil(nome: str, nascimento: int, faixa: str):
    utills.create_aluno(nome, nascimento, faixa)
    return {'response': f"O perfil de {nome}, nascido em {nascimento} foi feito e salvo com sucesso!"}

@app.patch("/items/")
def atualizar_item(item: str, nome: str):
    return {'response': f"Este é meu item, {nome}, {item}"}

@app.put("/items/")
def atualizar_completamente(item: str, nome: str):
    return {'response': f"Este é meu item, {nome}, {item}"}

@app.delete("/items/")
def deletar_perfil(item: str, nome: str):
    return {'response': f"Este é meu item, {nome}, {item}"}

if __name__ == '__main__':
    uvicorn.run(app)

#Rest: get (consultas), post (cadastro), pacht/put (atualizar), delete(deletar)