interacoes = []
chamados = [{"titulo": "Problema com impressora", "descricao": "A impressora não está funcionando", "urgencia": "Alta"}]

print("Registro de interação")
chamado = chamados[0]
descricao = input("Digite a descrição da interação: ")

interacoes.append({"chamado": chamado, "descricao": descricao})

print("Interacao registrada com sucesso!")
