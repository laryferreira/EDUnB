#Uma letra significa a operação enqueue e um asterisco significa a operação dequeue. 

#criando a fila

class FiladeCaracteres:
  def __init__(self): #cria a fila vazia
    self.fila = []
  def enqueue(self, item): 
    self.fila.append(item) #adiciona item
  def dequeue(self):
    if self.fila:
      return self.fila.pop(0) #retira item do inicio da fila se existir
    else:
      return None #se não existir retorna none
    
    
#criando a função que usará os métodos da fila
    
def processa_sequencia(sequencia): 
  fila = FiladeCaracteres() #
  resultado = '' #inicializa string vazia
  
  for item in sequencia:
    if char == "*":
       resultado += fila.dequeue() or ''
    else:
      fila.enqueue(item)
      
      
#obter a entrada do usuario:
sequencia = input()

#usar a funcao processa_sequencia:
resultado = processa_sequencia(sequencia)

#imprimir o resultado
print(resultado)
