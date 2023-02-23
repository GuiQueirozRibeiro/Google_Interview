def rabinKarp(B, S):
    hash = []
    b = len(B)
    s = len(S)
    prevHashValue = 0
    hashValue = 0

    for i in range(s):
        prevHashValue = (128*prevHashValue + ord(S[i]))%11
        hashValue = (128*hashValue + ord(B[i]))%11

    for i in range(b-s+1):
        if hashValue == prevHashValue:
            match = True
            for j in range(s):
                if B[i+j] != S[j]:
                    match = False
                    break
            if match:
                hash = hash +[i]
        if i<b-s:
            hashValue = (128*(hashValue-ord(B[i]))+ord(B[i+s])) % 11

    return hash