## Read input as specified in the question.
## Print output as specified in the question.
ch=input()
if ord(ch) in range(ord('A'),ord('Z')):
    print(1)
elif ord(ch) in range(ord('a'),ord('z')):
    print(0)
else:
    print(-1)
