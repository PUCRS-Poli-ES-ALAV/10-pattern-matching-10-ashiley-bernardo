import random, string, time

"""
## Enunciado 2

2. O algoritmo de Rabin-Karp utiliza uma função hash para resolver o problema de busca de padrões em string. O algoritmo está dado abaixo.
 
```javascript
private int search(String pat, String txt) {
   int M = pat.length();
   int N = txt.length();
   long patHash = hash(pat, M);

   for (int i = 0; i <= N - M; i++) {
      long txtHash = hash(txt.subtring(i, i+M), M);
      if (patHash == txtHash)
         return i; // ocorrência? colisão?
   }
   return N; // nenhuma ocorrência
}
```

O hash pode ser calculado utilizando o algoritmo de Horner.
Algoritmo de Horner para calcular o hash de uma string s[0..M-1]:

```javascript
//
//Notação: o padrão tem M caracteres, o texto tem N caracteres, o alfabeto tem R caracteres  (0 … R−1) 
//              Q é o módulo para o cálculo do Hash.
//              Qual o valor de Q?  Escolha Q igual a um primo grande para minimizar a chance de colisões.
//                       Por exemplo: o maior primo que possa ser representado com um int

private long hash(String s, int M) {
   long h = 0;
   for (int j = 0; j < M; j++)
      h = (h * R + s.charAt(j)) % Q;
   return h;
}
```
"""
def hash(s,m):
   h = 0;
   for i in range(0, m):
      h = (h * 21 + s[i]) % 7919
   return h

def search(pat, txt):
    m = len(pat)
    n = len(txt)
    pat_hash = hash(pat, m)

    for i in range(0, n - m + 1):
        txt_hash = hash(txt[i: i + m], m)
        if (pat_hash == txt_hash):
            return i
    return n

if __name__ == '__main__':
    print("-"*50)
    
    s1 = "ABCDCBDCBDACBDABDCBADF"
    s2 = "ADF"

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
    
    s1 = "ABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFOOOOOOO"
    s2 = "OOOOOOO"

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

    s1 = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"
    s2 = "AAAB"

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

    for i in range(5000):
        s1 += random.choice(string.ascii_letters)

    for i in range(5):
        s2 += random.choice(string.ascii_letters)

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