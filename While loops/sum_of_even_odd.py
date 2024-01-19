def SumOddEven(n):
    even=0
    odd=0
    while n!=0:
        a=n%10
        if a%2==0:
            even=even+a
        else:
            odd=odd+a
        n=n//10
    return even,odd


n=int(input())
print(*SumOddEven(n))
