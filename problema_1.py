import random, string, time

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
    iterations = 0
    result = -1

    offset = 0
    index_s1 = 0
    index_s2 = 0
    while (index_s1 < len(s1)) and (index_s2 < len(s2)):
        iterations += 1

        if s1[index_s1] == s2[index_s2]:
            if result == -1:
                result = index_s1
            else:
                offset += 1
        else:
            result = -1
            index_s2 = -1
            index_s1 -= offset
            offset = 0

        index_s1 += 1
        index_s2 += 1

    print("Iterations:", iterations)
    return result

if __name__ == "__main__":
    
    print("-"*50)
    
    s1 = "ABCDCBDCBDACBDABDCBADF"
    s2 = "ADF"

    print(f'S1 = "{s1}"')
    print(f'Lenght S1 = {len(s1)}')
    
    print(f'S2 = "{s2}"')
    print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = find_substring(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)
    
    s1 = "ABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFOOOOOOO"
    s2 = "OOOOOOO"

    print(f'S1 = "{s1}"')
    print(f'Lenght S1 = {len(s1)}')
    
    print(f'S2 = "{s2}"')
    print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = find_substring(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)

    s1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"
    s2 = "AAAB"

    print(f'S1 = "{s1}"')
    print(f'Lenght S1 = {len(s1)}')
    
    print(f'S2 = "{s2}"')
    print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = find_substring(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)

    s1 = ""
    s2 = ""

    for i in range(5000):
        s1 += random.choice(string.ascii_letters)

    for i in range(5):
        s2 += random.choice(string.ascii_letters)

    print(f'S1 = "{s1}"')
    print(f'Lenght S1 = {len(s1)}')
    
    print(f'S2 = "{s2}"')
    print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = find_substring(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)
    