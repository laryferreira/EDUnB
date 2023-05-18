'''Elabore um programa que determine o tempo total gasto para que todos os N veículos passem pelo posto de pesagem da rodovia.
Os fiscais sempre começam o processo de abordagem a partir do primeiro veículo que passa pelo posto.

Entrada
A primeira linha da entrada contém três números inteiros separados por um espaço em branco 1≤N≤104
1 ≤ F ≤ 100, 1 ≤ P ≤ 103 indicando a quantidade de veículos, o fator de amostragem e o limite de peso (em kg) da rodovia, respectivamente.
A próxima linha contém N valores inteiros a1,...aN, em que cada 1≤ai≤103 está associado com o peso (em kg) do veículo i

Saída
Imprima um valor inteiro associado ao tempo total para que todos os N veículos passem pelo posto de pesagem.'''


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)

n, f, p = map(int, input().split())

# cria fila
Qtrucks = Queue()
for truck in input().split():
    Qtrucks.enqueue(int(truck))

time = i = 0
while not Qtrucks.isEmpty():
    # pega primeiro da fila
    fst = Qtrucks.dequeue()
    
    # verifica se deve ou nao ser abordado
    if i % f == 0:
        # se nao passar, vai pro final da fila com peso -2kg
        if fst > p:
            time += 10
            Qtrucks.enqueue(fst-2)
        else:
            time += 5
    else:
        time += 1
    i += 1
print(time)
