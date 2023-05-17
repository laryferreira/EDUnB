def inferno(fila, avancos):
  pessoas = fila.split()
  tamanho_fila = len(pessoas)
    # Calcula o número de avanços efetivos considerando o tamanho da fila
    avancos_efetivos = avancos % tamanho_fila

    # Avança a fila de acordo com o número de avanços efetivos
    pessoas = pessoas[avancos_efetivos:] + pessoas[:avancos_efetivos]

    pessoa_da_frente = pessoas[0]
    pessoa_do_fim = pessoas[-1]

    return pessoa_da_frente, pessoa_do_fim


# Processa múltiplas entradas e saídas
while True:
    try:
        fila_atual = input()
        numero_avancos = int(input())

        pessoa_frente, pessoa_fim = inferno(fila_atual, numero_avancos)

        print("Pessoa da frente:", pessoa_frente)
        print("Pessoa do fim:", pessoa_fim)
        print()  # Linha em branco para separar as saídas
    except EOFError:
        break
