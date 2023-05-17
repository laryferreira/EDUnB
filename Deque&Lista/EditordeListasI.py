''''Crie um programa para editar uma lista dinâmica de chaves. 
O programa recebe comandos que devem ser executados, em sequência, sobre a lista. 
Ao final do processamento das operações, exiba a lista em sua situação. 
Considere como chaves válidas, inteiros positivos. As operações são as seguintes:

I v insere o valor 𝑣
 no início da lista.
F v insere o valor 𝑣
 no final da lista.
P remove do final e imprime valor removido.
D remove do início e imprime valor removido.
X Indica o final das operações e que a lista resultante deve ser impressa.
Entrada
A entrada consiste de uma série de instruções, uma por linha. A instrução X determina o fim da entrada.

Saída
A saída consiste nos resultados de se processar cada instrução, conforme definidas no enunciado, a medida que são fornecidas.'''''

def editar_lista():
  valores = []
  
  while True:
    comando = input()
    if comando == 'X':
      break
     elif comando.startswith('I'):
          _, valor = comando.split() #-, ignora a letra e recebe apenas o valor
          valores.insert(0, int(valor))
     elif comando.startwith('F'):
          _, valor = comando.split()
           valores.append(int(valor))
     elif comando== "P":
            valor_removido = valores.pop()
            print(valor_removido)
     elif command == "D":
            valor_removido = valores.pop(0)
            print(valor_removido)
  
 for valor in valores:
    print(valor)


editar_lista()
