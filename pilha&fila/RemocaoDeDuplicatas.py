# pilha
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


n = int(input())

for _ in range(n):
    s = input()
    
    exp = Stack()
    simbs = {')':'(', ']':'[', '}':'{'}
        
    dupli = 0

    # registra o último tipo de simbolo fechado
    prev = ''
    
    # empilhamos a expressao, ate acharmos algum ')' ou ']' ou '}'
    for char in s:
        if char not in ')]}':
            exp.push(char)
        else:

            # contador de caracteres entre '))' ou ']]' ou '}}'
            els_inside = 0
            
            top = exp.pop()
            while top != simbs[char]:
                top = exp.pop()
                els_inside += 1
                
            # se nao ha caracteres entre '))' ou ']]' ou '}}'
            # temos uma duplicata
            if els_inside < 1 and char == prev:
                dupli = 1
            
            prev = char

            
    if dupli:
        print("A expressão possui duplicata.")
    else:
        print("A expressão não possui duplicata.")
