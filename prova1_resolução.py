#1) 
def enqueue(self, elemento): #complexidade O(n)
  self.fila = self.fila + (elemento,)
def dequeue(self): #complexidade O(n)
  if self.fila == ():
    raise ValueError("A fila está vazia.")
  elemento = self.fila[0]
  self.fila = self.fila[1:]
  return elemento
#3)
class filaprioridade:
  def __init__(self):
    self.fila = {}
  def enqueue (self, elemento, prioridade): #complexidade O(1)
    self.fila[elemento] = prioridade
  def dequeue(self): #complexidade O(n)
    if self.fila == {}:
      raise ValueError("Fila de prioridade vazia")
    elemento, prioridade = max(self.fila.items(), key = lambda, x:x[1])
    del self.fila[elemento]
    return elemento
#5)
#complexidade O(nˆk)
#complexidade O(log(n))
  
