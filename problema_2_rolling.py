import random, string, time

def hash(word, length):
    h = 0;
    for i in range(0, length):
        char_hash = (256 + ord(word[i])) % 7919
        h = h + char_hash

    return h

def search(pat, txt):
    pat_length = len(pat)
    txt_length = len(txt)

    pat_hash = hash(pat, pat_length)

    # Calcular o hash do primeiro bloco
    i = 0
    part_of_txt = txt[i: i + pat_length]
    txt_hash = hash(part_of_txt, pat_length)

    if (pat_hash == txt_hash) and (part_of_txt == pat):
        return i
    else:
        end = txt_length - pat_length + 1

        for i in range(1, end):
            part_of_txt = txt[i: i + pat_length]
            removing_char = txt[i - 1]
            adding_char = txt[i + pat_length - 1]
            txt_hash = txt_hash - hash(removing_char, 1) + hash(adding_char, 1)
        
            if (pat_hash == txt_hash) and (part_of_txt == pat):
                return i
        return -1

if __name__ == '__main__':
    print("-"*50)
    
    s1 = "log"
    s2 = "otorrinolaringologista"

    print(f'S1 = "{s1}"')
    print(f'Lenght S1 = {len(s1)}')
    
    print(f'S2 = "{s2}"')
    print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = search(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)
    
    s1 = "OOOOOOO"
    s2 = "ABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFOOOOOOO"

    print(f'S1 = "{s1}"')
    print(f'Lenght S1 = {len(s1)}')
    
    print(f'S2 = "{s2}"')
    print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = search(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)

    s1 = "AAAB"
    s2 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"

    print(f'S1 = "{s1}"')
    print(f'Lenght S1 = {len(s1)}')
    
    print(f'S2 = "{s2}"')
    print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = search(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)

    s1 = ""
    s2 = ""

    for i in range(5):
        s1 += random.choice(string.ascii_letters)

    for i in range(500000):
        s2 += random.choice(string.ascii_letters)

    # print(f'S1 = "{s1}"')
    # print(f'Lenght S1 = {len(s1)}')
    
    # print(f'S2 = "{s2}"')
    # print(f'Length S2 = {len(s2)}')

    start = time.time()
    result = search(s1, s2)
    end = time.time()

    print(f'Result = {result}')
    print(f'Time = {end - start}')

    print("-"*50)