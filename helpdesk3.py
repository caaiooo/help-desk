tecnicos = ["João", "Maria", "Pedro"]
chamados = [{"titulo": "Problema com o pc", "descricao": "O pc não está funcionando", "urgencia": "Alta"}]

print("Atribuição de chamados")
chamado = chamados[0]
tecnico = tecnicos.pop(0)
print("Chamado " + chamado["titulo"] + " atribuído ao técnico " + tecnico)