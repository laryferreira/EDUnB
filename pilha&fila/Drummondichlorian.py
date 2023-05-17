''''Como parte de seu treinamento, você deve identificar o comportamento dessa nova ferramenta! Dessa forma, dada a sequência de instruções de inserção/remoção em uma drummondichlorian, indique com qual ED tradicional ela se parece.

Entrada
A entrada contém 5 casos de teste. Para cada caso, a primeira linha apresenta um inteiro 𝑁
 (0≤𝑁≤100
) indicando a quantidade de instruções realizadas. As 𝑁
 linhas seguintes apresentam, cada uma, a instrução para a drummondichlorian no seguinte formato: I X, onde I indica se houve a inserção ("in") de um valor X ou houve a retirada ("out") de um valor (que é X). Considere que 0≤𝑋≤1000
.

Saída
Para cada caso de teste, analise o comportamento da drummondichlorian e diga com qual estrutura de dados se parece. 
As opções são: "LIFO", se ela se comportar como uma pilha, "FIFO", caso tenha o comportamento de uma fila, ou "AIPO" (de any in, priority out), 
caso pareça ser uma fila de prioridades. Caso o comportamento não seja equivalente a uma destas estruturas de dados tradicionais, informe ao Mestre D'Costa que "no hay!".
Se houver mais de uma possibilidade, questione-o com: "uai?"'''''

#criando a pilha
class Stack:
    def __init__(self):
       self.items = []
    def isEmpty(self):
       return self.items == []
    def push(self, item):
       self.items.append(item)
    def pop(self):
       return self.items.pop()
    def peek(self):
       return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)
     
#criando a fila
class Queue:
    def __init__(self):
        self.items = []
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0,item)
    def dequeue(self):
        return self.items.pop()
    def front(self):
        return self.items[len(self.items)-1]
    def size(self):
       return len(self.items)
     
#criando a fila de prioridade
class PriorityQueue:
    def __init__(self):
       self.items = []
    def isEmpty(self):
       return self.items == []
    def enqueue(self, item):
       self.items.insert(0, item)
    def dequeue(self):
       return self.items.sort()
       return self.items.pop()
    def front(self):
       return self.items[len(self.items)-1]
     
#executando os casos de teste:
for i in range(5):
   n = int(input())
   lifo = Stack()
   fifo = Queue()
   pfifo = PriorityQueue()
   
   p = f = pf = 1 #inicializando variaveis para comparação posterior
   for _ in range(n):
     op, elm = input().split()
     elm = int(elm)
     
     if op == 'in':
        lifo.push(elm)
        fifo.enqueue(elm)
        pfifo.enqueue(elm)
     elif op == 'out':
        if elm != lifo.peek():
            p = 0
        elif p == 1:
            lifo.pop()
        if elm != fifo.front()
            f = 0
        elif f == 1:
            fifo.dequeue()
        if pf == 1:
            x = pfifo.dequeue()
            if x != elm:
              pf = 0
             
  if p + f + pf > 1:
        print("uai?")
    elif p + f + pf == 0:
        print("no hay!")
    elif p == 1:
        print("LIFO")
    elif f == 1:
        print("FIFO")
    elif pf == 1:
        print("AIPO")
             
        
        
   
