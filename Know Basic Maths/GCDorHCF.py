def calcGCD(n:int, m: int) -> int:
    # Write your code here
    if m==0:
        return n
    else:
        return calcGCD(m,n%m)

