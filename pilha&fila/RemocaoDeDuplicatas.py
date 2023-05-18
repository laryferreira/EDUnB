''' Sua tarefa é, dada uma lista de expressões algébricas válidas, verificar se há algum símbolo de prioridade duplicado dentro de cada expressão.
Entrada
A entrada é composta por várias linhas. A primeira linha possui um inteiro N
(1≤N≤100) que indica o número de expressões a serem verificadas. A seguir, as próximas N linhas possuem, cada uma, um string E

(de comprimento entre 4 e 1000, inclusive), sem espaços, que representa a expressão algébrica a ser analisada.

Saída
Para cada expressão, a saída deve ser "A expressão possui duplicata.", se houver um símbolo de prioridade duplicado
dentro da expressão ou "A expressão não possui duplicata." caso não haja um mesmo símbolo de prioridade duplicado 
dentro da expressão, de acordo com os exemplos.'''

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
