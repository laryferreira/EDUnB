#A implementação de pilha, apresentada no livro didático da disciplina, utiliza a lista do python para manter os elementos inseridos na estrutura. Por exemplo, a função peek é responsável por retornar o elemento que se encontra no topo da pilha. Sua implementação é a seguinte:

    #def peek(self):
        #return self.items[len(self.items) - 1]
#Dada a implementação, é possível perceber que se o método peek foi chamado em uma pilha sem elementos, um erro irá ocorrer. Dessa forma, sua tarefa é, dada a implementação de pilha abaixo, consertar os métodos que podem realizar consultas a sua estrutura e apresentar erros devido a inexistência de elemntos.
class Stack:
  def __init__(self):
    self.items = []
  def isEmpty(self):
    return len(self.items) == 0
  def push(self, item):
    self.items.append(item)
  def pop(self):
    if self.isEmpty():
      return None #retorna none quando a pilha está vazia
    else:
      return self.items.pop()
  def peek(self):
    if self.isEmpty():
      return None 
    else:
      return self.items[len(self.items)-1]
  def size(self):
    return len(self.items)
