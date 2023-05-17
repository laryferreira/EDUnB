#As anilhas estão empilhadas, 
#e seu trabalho é simples: acompanhar a quantidade de anilhas que são retiradas até se pegar a anilha específica da série de exercícios.
#A entrada do programa consiste de uma quantidade indeterminada de valores inteiros positivos distintos, 
#um por linha e cada um representando o peso de uma anilha, na ordem em que foram empilhadas pelo último usuário. 
#O último valor dessa sequência será 0, indicando que todas as anilhas já foram informadas. 
#A seguir é fornecido o peso da anilha desejada, em uma linha.

pesos = []
pesototal = []
count = 0
# ler os pesos até que 0 seja encontrado (todas as anilhas já informadas)
while True:
  peso = int(input())
  if peso == 0:
    break
  pesos.append(peso)
  
peso_alvo: int(input())
  
#processar a retirada de pesos em ordem inversa
for peso in reversed(pesos):
  pesototal += peso
  count += 1
  print("Peso retirado:", peso)
  if peso == peso_alvo:
    break

#printar os resultados:
print("Anilhas retiradas:", count)
print("Peso total movimentado", pesototal)
