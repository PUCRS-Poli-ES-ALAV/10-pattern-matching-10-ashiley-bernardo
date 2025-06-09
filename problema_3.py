
import random
import string
import time


global iterations


def KPMSearch(pat, txt):
    global iterations

    pat_len = len(pat)
    txt_len = len(txt)

    j = 0
    lps = pat_len * [0]

    computeLPSArray(pat, pat_len, lps)

    i = 0
    while i < txt_len:
        iterations += 1
        if pat[j] == txt[i]:
            i += 1
            j += 1

        if j == pat_len:
            print(f"Pattern found at index {i - j}")
            j = lps[j - 1]

        elif i < txt_len and pat[j] != txt[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


def computeLPSArray(pat, pat_len, lps):
    global iterations
    iterations = 0

    len = 0
    i = 1

    while i < pat_len:
        iterations += 1
        if pat[i] == pat[len]:
            len += 1
            lps[i] = len
            i += 1
        else:
            if len != 0:
                len = lps[len - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def run_test(text, pattern):
    global iterations
    iterations = 0

    lps = [0] * len(pattern)

    print("Text:", text)
    print("Pattern:", pattern)
    print("Length of Text:", len(text))
    print("Length of Pattern:", len(pattern))

    start = time.time()
    KPMSearch(pattern, text)
    end = time.time()

    print("Iterations:", iterations)
    print("Time:", end - start)

    print("LPS Array:", lps)
    computeLPSArray(pattern, len(pattern), lps)
    print("Computed LPS Array:", lps)
    print("-" * 50)


if __name__ == "__main__":
    text = "AABA"
    pattern = "AABA"
    run_test(text, pattern)

    text = "ABCDCBDCBDACBDABDCBADF"
    pattern = "ADF"
    run_test(text, pattern)

    text = "ABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFABCDCBDCBDACBDABDCBADFOOOOOOO"  # noqa
    pattern = "OOOOOOO"
    run_test(text, pattern)

    text = "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAB"
    pattern = "AAAB"
    run_test(text, pattern)

    text = ""
    pattern = ""

    for i in range(5000):
        text += random.choice(string.ascii_letters)

    for i in range(5):
        pattern += random.choice(string.ascii_letters)

    run_test(text, pattern)
