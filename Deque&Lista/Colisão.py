def tabela_dispersao(T, N, chaves):
    tabela = [[] for _ in range(T)]  # Cria uma tabela vazia com T listas vazias

    for chave in chaves:
        indice = chave % T  # Calcula o índice na tabela usando o operador módulo

        tabela[indice].append(chave)  # Adiciona a chave na lista correspondente ao índice

    for i, lista in enumerate(tabela):
        elementos = " -> ".join(str(x) for x in lista) if lista else "[x]"
        print(f"{i} - {elementos}")

# Leitura da entrada
T, N = map(int, input().split())
chaves = list(map(int, input().split())) if N > 0 else []

# Chamada da função para resolver o problema
tabela_dispersao(T, N, chaves)
