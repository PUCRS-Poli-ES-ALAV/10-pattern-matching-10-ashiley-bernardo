"""
## O problema

Dadas duas strings, s1 e s2, verificar a posição da primeira ocorrência de se s2 em s1, se existir.

Assim, se s1 = "ABCDCBDCBDACBDABDCBADF" e s1 = "ADF" o retorno seria 19.

## Enunciado 1

1. Faça um algortimo que resolva o problema acima.
   1. teste-o para strings de diversos tamanhos, até strings grandes (ambas as strings >500.000 caracteres). Conte o número de iterações e de instruções.
   1. qual a complexidade, no pior caso?

"""
def find_substring(s1, s2):
    result = -1

    index_s1 = 0
    index_s2 = 0
    while (index_s1 < len(s1) - 1) and (index_s2 < len(s2) - 1):
        if s1[index_s1] == s2[index_s2]:
            if result == -1:
                result = index_s1
        else:
            result = -1
            index_s2 = 0

        index_s1 += 1
        index_s2 += 1

    return result

if __name__ == "__main__":
    s1 = "ABCDCBDCBDACBDABDCBADF"
    s2 = "ADF"

    result = find_substring(s1, s2)
    print(f'S1 = "{s2}", S2 "{s1}" : {result}')
    