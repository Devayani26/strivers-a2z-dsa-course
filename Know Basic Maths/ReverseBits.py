def reverseBits(n):
    n=bin(n)[2:]
    n1=n.zfill(32)
    n1=n1[::-1]
    n1=int(n1,2)
    return n1
