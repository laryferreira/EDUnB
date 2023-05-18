# pilha
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def top(self):
        return items[len(items)-1]
        
string = input()
pilha = Stack()

ans = ''
for char in string:
    if char == '*' and not pilha.isEmpty():
        ans += pilha.pop()
    elif char != '*':
        pilha.push(char)
        
print(ans)
