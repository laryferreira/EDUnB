def lcs_length(str1, str2):
    m = len(str1)
    n = len(str2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    max_length = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                max_length = max(max_length, dp[i][j])

    return max_length

# Leitura da entrada
str1 = input().strip()
str2 = input().strip()

# Cálculo dos tamanhos dos trechos e do LCS
size1 = len(str1)
size2 = len(str2)
lcs_size = lcs_length(str1, str2)

# Impressão dos resultados
print(size1)
print(size2)
print(lcs_size)
