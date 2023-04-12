''''Implemente a função divisores, que recebe um número inteiro e retorna todos os seus divisores inteiros (incluindo 1 e ele mesmo) em uma lista.

Entrada da Função
Um número inteiro 𝑛>0

Saída da Função
Uma lista com todos os divisores desse número

Observações: Implemente apenas a função, o código de teste se encarrega de ler a entrada, chamar a função e imprimir o resultado.''''
------------------------------------------
  
def divisores(n):
    d = []
    for i in range(1, n+1):
        if n % i == 0:
            d.append(i)
    return d
