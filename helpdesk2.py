chamados = [{"titulo": "Problema com o pc", "descricao": "O pc não está funcionando", "urgencia": "Alta"}]

print("Priorização de chamados")
for chamado in chamados:
    print(chamado["titulo"] + " - " + chamado["urgencia"])