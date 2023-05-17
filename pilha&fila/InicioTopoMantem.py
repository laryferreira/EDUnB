#Complete a classe Stack dada, definindo os métodos push e pop de modo que o comportamento seja LIFO.

class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.insert(0, item) #insere no inicio da lista
    def pop(self):
        if not self.isEmpty:
          return self.items.pop(0) #remove do inicio da lista
    def isEmpty(self):
        return len(self.items) == 0
    def peek(self):
        return self.items[len(self.items)-1]
    
     
