def compareStrings(a, b):
    if len(a) > len(b):
        for c, i in zip(b, range(len(b))):
            if ord(c) < ord(a[i]):
                return False
            elif ord(c) > ord(a[i]):
                return True
    else:
        for c, i in zip(a, range(len(a))):
            if ord(c) < ord(b[i]):
                return True
            elif ord(c) > ord(b[i]):
                return False

def compareWeights(w1, w2):
    absdiff = abs(w1 - 75) - abs(w2 - 75)
    
    closest = None
    if absdiff != 0:
        closest = w1 if absdiff < 0 else w2
    smaller = w1 if w1 < w2 else w2

    if closest:
        if closest != smaller:
            if closest <= 75:
                return True if closest == w1 else False
            else:
                return False if smaller == w2 else True
        else:
            return True if closest == w1 else False
    else:
        return True if smaller == w1 else False


def compare(h1, h2, m1, m2, sn1, sn2, n1, n2):
    dh = abs(h1-180) - abs(h2-180)

    if dh == 0 and m1 == m2:
        if sn1 != sn2:
            return compareStrings(sn1, sn2)
        else:
            return compareStrings(n1, n2)
    
    if dh != 0:
        return True if dh < 0 else False
    else:
        return compareWeights(m1, m2)


def mergeDictSort(a: list):
    if len(a) > 1:
        midpoint = len(a) // 2
        leftHalf = a[:midpoint]
        rightHalf = a[midpoint:]

        mergeDictSort(leftHalf)
        mergeDictSort(rightHalf)

        i, j, k = 0, 0, 0
        while i < len(leftHalf) and j < len(rightHalf):
            hl, hr = leftHalf[i]["height"], rightHalf[j]["height"]
            ml, mr = leftHalf[i]["mass"], rightHalf[j]["mass"]
            snl, snr = leftHalf[i]["surname"], rightHalf[j]["surname"]
            nl, nr = leftHalf[i]["name"], rightHalf[j]["name"]

            keepOrder = compare(hl, hr, ml, mr, snl, snr, nl, nr)
            if keepOrder:
                a[k] = leftHalf[i]
                i += 1
            else:
                a[k] = rightHalf[j]
                j += 1
            k += 1      
        
        while i < len(leftHalf):
            a[k] = leftHalf[i]
            i += 1
            k += 1
        
        while j < len(rightHalf):
            a[k] = rightHalf[j]
            j += 1
            k += 1

n = int(input())

guys = []
while (n > 0):
    name, surname, height, mass = input().split(" ")
    guys.append({
        "name": name,
        "surname": surname,
        "height": int(height),
        "mass": int(mass)
    })
    n -= 1

mergeDictSort(guys)
for guy in guys:
    print(guy["surname"], guy["name"], sep=", ")
