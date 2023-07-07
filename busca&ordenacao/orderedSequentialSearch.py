deredSequentialSearch(alist, item):
    pos = 0
    found = False
    
    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
            
    return found

#a vantagem em uma lista ordenada está no caso em que nao ha o item na lista. assim que nao encontralo, a busca é encerrada
#ainda é O(N)
