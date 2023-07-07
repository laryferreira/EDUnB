def sequentialSearch(alist, item):
    pos = 0
    found = False
    
    while pos < len(alist) and not found: #enquanto a posiçao esta presente na lista e o item nao foi encontrado
        if alist[pos] == item:
            found = True
        else:
            pos = pos+1
    
    return found


#analise O(n) em uma LISTA NAO ORDENADA
#item presente:
    #melhor caso: O(1)
    #pior caso: O(N)
    #caso medio: O(N/2)
    #geral: O(N)
#item nao presente:
    #geral: O(N)

