def organizar_roupas(num_entradas, roupas):
  gaveta = []
  total_roupas = 0
  total_tempo = 0
  
  for i in range(num_entradas):
    entrada = roupas[i].split()
    tipo = entrada[0]
    cor = entrada[1]
    tempo = int(entrada[2])
    
    gaveta.append((tipo, cor))
    total_roupas += 1
    total_tempo += tempo
  
  gaveta.reverse()
  
 for roupa in gaveta:
    tipo, cor = roupa
    print(f"Tipo: {tipo}, Cor: {cor}")
  print(f"Total de roupas: {total_roupas}")
  print(f"Total de tempo: {total_tempo}")
  
  #chamar a função
  def main():
    num_entradas = int(input())
    roupas = []
    
    for _ in range(num_entradas):
        entrada = input()
        roupas.append(entrada)
        
        organizar_roupas(num_entradas, roupas)
        
 main()
