def frequencia(mensagem):
    freq = {}
    for c in mensagem:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    max_freq = 0
    max_char = ''
    for c in freq:
        if freq[c] > max_freq:
            max_freq = freq[c]
            max_char = c
    return max_char
