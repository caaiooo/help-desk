chamados = []

print("Registro de chamados")
titulo = input("Digite o título do chamado: ")
descricao = input("Digite a descrição do chamado: ")
urgencia = input("Digite a urgência do chamado (Alta, Média, Baixa): ")

chamados.append({"titulo": titulo, "descricao": descricao, "urgencia": urgencia})

print("Chamado registrado com sucesso!")
